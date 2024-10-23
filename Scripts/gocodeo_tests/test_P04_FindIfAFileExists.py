import pytest
from unittest import mock
import os
from Scripts.P04_FindIfAFileExists import searchFile

@pytest.fixture
def mock_os_walk():
    with mock.patch('os.walk') as mock_walk:
        yield mock_walk

@pytest.fixture
def mock_print():
    with mock.patch('builtins.print') as mock_print_func:
        yield mock_print_func

@pytest.fixture
def mock_exit():
    with mock.patch('sys.exit') as mock_exit_func:
        yield mock_exit_func

@pytest.fixture
def setup_mocks(mock_os_walk, mock_print, mock_exit):
    # Mocking the os.walk return value
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', ('Tests',), ('6-Folder.txt',)),
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests', (), ('subdir-file.txt',))
    ]

# happy path - searchFile - Test that the file is found when it exists in the root directory of the PATH
def test_file_found_in_root(setup_mocks):
    searchFile('6-Folder.txt')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts')
    setup_mocks[1].assert_any_call('6-Folder.txt Found')


# happy path - searchFile - Test that the search continues in subdirectories until the file is found
def test_file_found_in_subdirectory(setup_mocks):
    searchFile('subdir-file.txt')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests')
    setup_mocks[1].assert_any_call('subdir-file.txt Found')


# happy path - searchFile - Test that the function prints 'Looking in:' for each directory it searches
def test_print_looking_in_each_directory(setup_mocks):
    searchFile('anyfile.txt')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests')


# happy path - searchFile - Test that the function returns when the file is found and doesn't continue searching
def test_exit_after_finding_file(setup_mocks):
    searchFile('6-Folder.txt')
    setup_mocks[1].assert_any_call('6-Folder.txt Found')
    setup_mocks[2].assert_not_called()


# happy path - searchFile - Test that the function handles multiple files with similar names and finds the correct one
def test_similar_file_names(setup_mocks):
    setup_mocks[0].return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', ('Tests',), ('6-Folder.txt', '6-Folder-1.txt'))
    ]
    searchFile('6-Folder.txt')
    setup_mocks[1].assert_any_call('6-Folder.txt Found')


# edge case - searchFile - Test that the function behaves correctly when the file does not exist
def test_file_not_found(setup_mocks):
    searchFile('nonexistent.txt')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests')
    setup_mocks[1].assert_not_called_with('nonexistent.txt Found')


# edge case - searchFile - Test that the function handles an empty file name input gracefully
def test_empty_file_name(setup_mocks):
    searchFile('')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests')
    setup_mocks[1].assert_not_called_with(' Found')


# edge case - searchFile - Test that the function handles special characters in the file name
def test_special_characters_in_file_name(setup_mocks):
    searchFile('spécial.txt')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests')
    setup_mocks[1].assert_not_called_with('spécial.txt Found')


# edge case - searchFile - Test that the function handles a very long file name
def test_very_long_file_name(setup_mocks):
    searchFile('a_very_long_file_name_that_probably_does_not_exist.txt')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests')
    setup_mocks[1].assert_not_called_with('a_very_long_file_name_that_probably_does_not_exist.txt Found')


# edge case - searchFile - Test that the function does not crash or hang when the PATH is very large
def test_large_directory_path(setup_mocks):
    setup_mocks[0].return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', ('Tests',), ('6-Folder.txt',)),
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests', (), ('subdir-file.txt',)),
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests/SubTests', (), ('6-Folder.txt',))
    ]
    searchFile('6-Folder.txt')
    setup_mocks[1].assert_any_call('6-Folder.txt Found')


