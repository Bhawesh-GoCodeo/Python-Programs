import pytest
from unittest import mock
import os

@pytest.fixture
def mock_file_operations():
    mock_open = mock.mock_open(read_data='sample data\nhilarious\nmore data')
    with mock.patch('builtins.open', mock_open):
        yield mock_open

@pytest.fixture
def mock_os_operations():
    with mock.patch('os.getcwd', return_value='/home/omkarpathak/Documents/PythonLecture'), \
         mock.patch('os.chdir'), \
         mock.patch('os.listdir', return_value=['file1.txt', 'file2.txt', 'existing_directory']), \
         mock.patch('os.path.isfile', side_effect=lambda x: x in ['/home/omkarpathak/Documents/PythonLecture/file1.txt', '/home/omkarpathak/Documents/PythonLecture/file2.txt']), \
         mock.patch('os.path.isdir', side_effect=lambda x: x in ['/home/omkarpathak/Documents/PythonLecture/existing_directory']):
        yield

@pytest.fixture
def mock_string_operations():
    with mock.patch('str.count', side_effect=lambda self, sub: self.lower().count(sub.lower())):
        yield

@pytest.fixture
def mock_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'a')

@pytest.fixture
def setup_all_mocks(mock_file_operations, mock_os_operations, mock_string_operations, mock_input):
    pass

# happy path - open - Test that file is closed after reading using context manager.
def test_file_closed_after_reading(setup_all_mocks):
    with open('social.txt', 'r') as file:
        data = file.read()
    assert file.closed


# happy path - open - Test that file is written to using append mode.
def test_file_written_in_append_mode(setup_all_mocks):
    with open('something.txt', 'a') as file:
        file.write('MMCOE - yethe bahutanche hith!')
    assert file.closed


# happy path - open - Test that specific number of characters are read from the file.
def test_read_specific_characters(setup_all_mocks):
    with open('social.txt', 'r') as fd:
        data = fd.read(6)
    assert data == 'sample'


# happy path - os.getcwd - Test that the current working directory is printed correctly.
def test_get_current_working_directory(setup_all_mocks):
    current_directory = os.getcwd()
    assert current_directory == '/home/omkarpathak/Documents/PythonLecture'


# happy path - os.mkdir - Test that a new directory is created and navigated into.
def test_create_and_navigate_directory(setup_all_mocks):
    os.mkdir('Directory00')
    os.chdir('Directory00')
    current_directory = os.getcwd()
    assert current_directory.endswith('Directory00')


# edge case - open - Test that reading a non-existent file raises an error.
def test_read_non_existent_file(setup_all_mocks):
    with pytest.raises(FileNotFoundError):
        with open('non_existent.txt', 'r') as file:
            data = file.read()


# edge case - open - Test that writing to a file in a non-existent directory raises an error.
def test_write_to_file_in_non_existent_directory(setup_all_mocks):
    with pytest.raises(FileNotFoundError):
        with open('non_existent_dir/something.txt', 'w') as file:
            file.write('Text')


# edge case - os.chdir - Test that changing to a non-existent directory raises an error.
def test_change_to_non_existent_directory(setup_all_mocks):
    with pytest.raises(FileNotFoundError):
        os.chdir('/non_existent_directory')


# edge case - open - Test that counting a character in an empty file returns zero.
def test_count_character_in_empty_file(setup_all_mocks):
    with open('empty.txt', 'r') as file:
        data = file.read()
    count = data.lower().count('a')
    assert count == 0


# edge case - os.mkdir - Test that creating a directory with an existing name raises an error.
def test_create_existing_directory(setup_all_mocks):
    with pytest.raises(FileExistsError):
        os.mkdir('existing_directory')


