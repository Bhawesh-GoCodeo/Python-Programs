import pytest
from unittest import mock
import builtins
import os

@pytest.fixture
def mock_file_operations():
    mock_open = mock.mock_open(read_data='This is a test data for social.txt')
    
    with mock.patch('builtins.open', mock_open):
        yield mock_open

@pytest.fixture
def mock_os_operations():
    with mock.patch('os.getcwd', return_value='/home/omkarpathak/Documents/PythonLecture'), \
         mock.patch('os.chdir'), \
         mock.patch('os.listdir', return_value=['social.txt', 'something.txt']), \
         mock.patch('os.path.isfile', side_effect=lambda x: x in ['social.txt', 'something.txt']), \
         mock.patch('os.path.isdir', side_effect=lambda x: x not in ['social.txt', 'something.txt']):
        yield

@pytest.fixture
def mock_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'M')

# happy path - open - Test that file is closed after reading using context manager
def test_file_closed_after_reading(mock_file_operations):
    with open('social.txt', 'r') as file:
        data = file.read()
    assert file.closed == True


# happy path - open - Test that file is written to and closed using context manager
def test_file_written_and_closed(mock_file_operations):
    with open('something.txt', 'a') as file:
        file.write('Test writing data')
    assert file.closed == True


# happy path - open - Test that correct number of characters are read from file
def test_read_specific_characters(mock_file_operations):
    with open('social.txt', 'r') as file:
        data = file.read(6)
    assert data == 'This i'


# happy path - os.chdir - Test that current directory is changed successfully
def test_change_directory(mock_os_operations):
    os.chdir('/home/omkarpathak/Documents/Notebooks')
    assert os.getcwd() == '/home/omkarpathak/Documents/Notebooks'


# happy path - os.mkdir - Test that directories are created and navigated correctly
def test_create_and_navigate_directories(mock_os_operations):
    base_path = '/home/omkarpathak/Documents/PythonLecture/Naruto/Directory0'
    for i in range(10):
        os.mkdir('Directory' + str(i) + str(i))
        os.chdir('Directory' + str(i) + str(i))
    assert os.getcwd() == base_path


# edge case - open - Test that reading a non-existent file raises an error
def test_read_non_existent_file(mock_file_operations):
    with pytest.raises(FileNotFoundError):
        open('non_existent.txt', 'r')


# edge case - os.chdir - Test that changing to a non-existent directory raises an error
def test_change_to_non_existent_directory(mock_os_operations):
    with pytest.raises(FileNotFoundError):
        os.chdir('/non_existent_directory')


# edge case - open - Test that writing to a read-only file raises an error
def test_write_to_read_only_file(mock_file_operations):
    with pytest.raises(PermissionError):
        open('read_only.txt', 'w')


# edge case - open - Test that reading more characters than in file returns available characters
def test_read_more_characters_than_exist(mock_file_operations):
    with open('social.txt', 'r') as file:
        data = file.read(1000)
    assert data == 'This is a test data for social.txt'


# edge case - os.listdir - Test that os.listdir() returns empty list for empty directory
def test_list_empty_directory(mock_os_operations):
    with mock.patch('os.listdir', return_value=[]):
        files = os.listdir('/empty_directory')
    assert files == []


