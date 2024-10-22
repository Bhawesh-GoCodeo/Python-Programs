import pytest
from unittest import mock
import os
from Scripts.P04_FindIfAFileExists import searchFile

@pytest.fixture
def mock_os_walk():
    with mock.patch('os.walk') as mock_walk:
        yield mock_walk

@pytest.fixture
def mock_print(capsys):
    with mock.patch('builtins.print') as mock_print:
        yield mock_print

@pytest.fixture
def mock_exit():
    with mock.patch('sys.exit') as mock_exit:
        yield mock_exit

# happy path - searchFile - Test that a file is found when it exists in the specified directory
def test_file_found(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', [], ['6-Folder.txt', 'otherfile.txt'])
    ]
    searchFile('6-Folder.txt')
    mock_print.assert_any_call('6-Folder.txt Found')


# happy path - searchFile - Test that a file is found when it exists in a subdirectory
def test_file_found_in_subdirectory(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', ['subdir'], []),
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/subdir', [], ['subfile.txt'])
    ]
    searchFile('subfile.txt')
    mock_print.assert_any_call('subfile.txt Found')


# happy path - searchFile - Test that a file with special characters in its name is found
def test_special_characters_file_found(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', [], ['special@file!.txt'])
    ]
    searchFile('special@file!.txt')
    mock_print.assert_any_call('special@file!.txt Found')


# happy path - searchFile - Test that a file with spaces in its name is found
def test_file_with_spaces_found(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', [], ['file with spaces.txt'])
    ]
    searchFile('file with spaces.txt')
    mock_print.assert_any_call('file with spaces.txt Found')


# happy path - searchFile - Test that a file with a similar name is found
def test_similar_name_file_found(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', [], ['simfile.txt'])
    ]
    searchFile('simfile.txt')
    mock_print.assert_any_call('simfile.txt Found')


# edge case - searchFile - Test that no output is given when the file does not exist
def test_file_not_found(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', [], ['otherfile.txt'])
    ]
    searchFile('nonexistent.txt')
    mock_print.assert_not_called()


# edge case - searchFile - Test that search handles empty file name gracefully
def test_empty_file_name(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', [], ['anyfile.txt'])
    ]
    searchFile('')
    mock_print.assert_not_called()


# edge case - searchFile - Test that search handles very long file names without crashing
def test_very_long_file_name(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', [], ['shortfile.txt'])
    ]
    searchFile('a_very_long_file_name_that_might_cause_problems_due_to_length.txt')
    mock_print.assert_not_called()


# edge case - searchFile - Test that search handles directory traversal characters safely
def test_directory_traversal_characters(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', [], ['traversal.txt'])
    ]
    searchFile('../../traversal.txt')
    mock_print.assert_not_called()


# edge case - searchFile - Test that search behaves correctly when the directory is empty
def test_empty_directory(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', [], [])
    ]
    searchFile('anyfile.txt')
    mock_print.assert_not_called()


