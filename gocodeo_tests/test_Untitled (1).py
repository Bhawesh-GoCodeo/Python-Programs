import pytest
from unittest import mock
import os

@pytest.fixture
def mock_file_operations():
    # Mocking open function
    mock_open = mock.mock_open(read_data='This is a test file.\nIt contains multiple lines.\n')

    with mock.patch('builtins.open', mock_open):
        yield mock_open

@pytest.fixture
def mock_os_operations():
    with mock.patch('os.getcwd', return_value='/home/omkarpathak/Documents/PythonLecture'):
        with mock.patch('os.chdir') as mock_chdir:
            with mock.patch('os.listdir', return_value=['file1.txt', 'file2.txt']):
                with mock.patch('os.path.isfile', side_effect=lambda x: x in ['/home/omkarpathak/Documents/PythonLecture/file1.txt']):
                    with mock.patch('os.path.isdir', side_effect=lambda x: x in ['/home/omkarpathak/Documents/PythonLecture']):
                        yield mock_chdir

@pytest.fixture
def mock_string_operations():
    with mock.patch('str.lower', side_effect=lambda s: s.lower()):
        yield

@pytest.fixture
def mock_input():
    with mock.patch('builtins.input', side_effect=['a']):
        yield

@pytest.fixture
def mock_os_mkdir():
    with mock.patch('os.mkdir') as mock_mkdir:
        yield mock_mkdir

@pytest.fixture
def mock_os_path_exists():
    with mock.patch('os.path.exists', return_value=False):
        yield

# happy path - open - Test that the file is closed after reading using open and close methods.
def test_file_closed_after_reading(mock_file_operations):
    file = open('social.txt', 'r')
    data = file.read()
    file.close()
    assert file.closed == True


# happy path - open - Test that the file is closed after reading using context manager.
def test_file_closed_with_context_manager(mock_file_operations):
    with open('social.txt', 'r') as file:
        data = file.read()
    assert file.closed == True


# happy path - open - Test that appending text to a file works correctly.
def test_append_text_to_file(mock_file_operations):
    with open('something.txt', 'a') as file:
        file.write('MMCOE - yethe bahutanche hith!')
    
    mock_file_operations().write.assert_called_once_with('MMCOE - yethe bahutanche hith!')


# happy path - open - Test that reading specific number of characters from a file works correctly.
def test_read_specific_number_of_characters(mock_file_operations):
    with open('social.txt', 'r') as file:
        data = file.read(6)
    
    assert data == 'This i'  # Assuming 'This i' is the expected output for the first 6 characters


# happy path - os.chdir - Test that changing the current directory works correctly.
def test_change_current_directory(mock_os_operations):
    os.chdir('/home/omkarpathak/Documents/Notebooks')
    mock_os_operations.assert_called_once_with('/home/omkarpathak/Documents/Notebooks')


# edge case - open - Test that reading a non-existent file raises an error.
def test_read_non_existent_file():
    with pytest.raises(FileNotFoundError):
        with open('non_existent.txt', 'r') as file:
            data = file.read()


# edge case - open - Test that writing to a read-only file raises an error.
def test_write_to_read_only_file(mock_file_operations):
    mock_file_operations.side_effect = PermissionError
    with pytest.raises(PermissionError):
        with open('social.txt', 'w') as file:
            file.write('This should fail.')


# edge case - os.mkdir - Test that creating a directory that already exists raises an error.
def test_create_existing_directory(mock_os_mkdir, mock_os_path_exists):
    mock_os_path_exists.return_value = True
    with pytest.raises(FileExistsError):
        os.mkdir('existing_directory')


# edge case - open - Test that counting a character in an empty file returns zero.
def test_count_character_in_empty_file(mock_file_operations):
    mock_file_operations.return_value.read_data = ''
    with open('empty.txt', 'r') as file:
        data = file.read()
    count = data.lower().count('a')
    assert count == 0


# edge case - os.listdir - Test that listing files in an empty directory returns an empty list.
def test_list_files_in_empty_directory(mock_os_operations):
    mock_os_operations.return_value = []
    files = os.listdir('empty_directory')
    assert files == []


