import pytest
from unittest import mock
import os

@pytest.fixture
def mock_open_file():
    m = mock.mock_open(read_data='This is a test file.\nIt contains multiple lines.\n')
    with mock.patch('builtins.open', m):
        yield m

@pytest.fixture
def mock_os_getcwd():
    with mock.patch('os.getcwd', return_value='/mock/current/directory'):
        yield

@pytest.fixture
def mock_os_chdir():
    with mock.patch('os.chdir') as mock_chdir:
        yield mock_chdir

@pytest.fixture
def mock_os_listdir():
    with mock.patch('os.listdir', return_value=['file1.txt', 'file2.txt', 'directory1']):
        yield

@pytest.fixture
def mock_os_path_isfile():
    with mock.patch('os.path.isfile', side_effect=lambda x: x in ['file1.txt', 'file2.txt']):
        yield

@pytest.fixture
def mock_os_path_isdir():
    with mock.patch('os.path.isdir', side_effect=lambda x: x == 'directory1'):
        yield

@pytest.fixture
def mock_os_mkdir():
    with mock.patch('os.mkdir') as mock_mkdir:
        yield mock_mkdir

@pytest.fixture
def mock_input():
    with mock.patch('builtins.input', return_value='M'):
        yield

@pytest.fixture
def mock_string_count():
    with mock.patch.object(str, 'count', return_value=2):
        yield

# happy path - open - Test that file is closed after reading with open()
def test_file_closed_after_reading(mock_open_file):
    file = open('social.txt', 'r')
    data = file.read()
    file.close()
    assert file.closed == True


# happy path - open - Test that file is closed after reading with context manager
def test_file_closed_with_context_manager(mock_open_file):
    with open('social.txt', 'r') as file:
        data = file.read()
    assert file.closed == True


# happy path - open - Test that writing to a file in append mode works
def test_write_append_mode(mock_open_file):
    with open('something.txt', 'a') as file:
        file.write('MMCOE - yethe bahutanche hith!')
    mock_open_file().write.assert_called_once_with('MMCOE - yethe bahutanche hith!')


# happy path - open - Test that reading a specific number of bytes from a file works
def test_read_specific_bytes(mock_open_file):
    with open('social.txt', 'r') as fd:
        data = fd.read(6)
    assert data == 'This i'


# happy path - os.getcwd - Test that current working directory is printed correctly
def test_print_current_working_directory(mock_os_getcwd):
    directory = os.getcwd()
    assert directory == '/mock/current/directory'


# edge case - open - Test that reading a non-existent file raises an error
def test_read_non_existent_file():
    with pytest.raises(FileNotFoundError):
        open('non_existent.txt', 'r')


# edge case - os.chdir - Test that changing to a non-existent directory raises an error
def test_change_non_existent_directory():
    with pytest.raises(FileNotFoundError):
        os.chdir('/non/existent/directory')


# edge case - os.mkdir - Test that creating a directory that already exists raises an error
def test_create_existing_directory(mock_os_mkdir):
    mock_os_mkdir.side_effect = FileExistsError
    with pytest.raises(FileExistsError):
        os.mkdir('existing_directory')


# edge case - str.count - Test that counting a character not in file returns zero
def test_count_character_not_in_file(mock_open_file):
    with open('social.txt', 'r') as file:
        data = file.read()
    count = data.lower().count('z')
    assert count == 0


# edge case - os.listdir - Test that listing files in a non-existent directory raises an error
def test_list_files_non_existent_directory():
    with pytest.raises(FileNotFoundError):
        os.listdir('/non/existent/directory')


