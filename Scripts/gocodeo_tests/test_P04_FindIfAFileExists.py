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
    # Mocking os.walk to simulate file structure
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', ('Tests',), ('6-Folder.txt',)),
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests', (), ())
    ]

# happy path - searchFile - Test that the file is found in the root directory.
def test_file_found_in_root_directory(setup_mocks):
    searchFile('6-Folder.txt')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts')
    setup_mocks[1].assert_any_call('6-Folder.txt', 'Found')


# happy path - searchFile - Test that the file is found in a subdirectory.
def test_file_found_in_subdirectory(setup_mocks, mock_os_walk):
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', ('Tests',), ()),
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests', (), ('subfile.txt',))
    ]
    searchFile('subfile.txt')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests')
    setup_mocks[1].assert_any_call('subfile.txt', 'Found')


# happy path - searchFile - Test that the function prints the correct directory being searched.
def test_correct_directory_printed(setup_mocks):
    searchFile('6-Folder.txt')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts')


# happy path - searchFile - Test that the function breaks after finding the file.
def test_function_breaks_after_finding(setup_mocks):
    searchFile('6-Folder.txt')
    setup_mocks[1].assert_any_call('6-Folder.txt', 'Found')
    setup_mocks[2].assert_not_called()


# happy path - searchFile - Test that the function does not throw an exception when file is found.
def test_no_exception_on_file_found(setup_mocks):
    searchFile('6-Folder.txt')
    setup_mocks[2].assert_not_called()


# edge case - searchFile - Test that the function handles non-existent file gracefully.
def test_non_existent_file(setup_mocks):
    searchFile('nonexistent.txt')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests')
    setup_mocks[2].assert_not_called()


# edge case - searchFile - Test that the function handles directories with no files.
def test_empty_directory(setup_mocks, mock_os_walk):
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', ('Tests',), ()),
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests', (), ())
    ]
    searchFile('6-Folder.txt')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts')
    setup_mocks[1].assert_any_call('Looking in:', '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests')
    setup_mocks[2].assert_not_called()


# edge case - searchFile - Test that the function handles special characters in file name.
def test_special_characters_in_file_name(setup_mocks, mock_os_walk):
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', ('Tests',), ('special@file#name.txt',)),
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests', (), ())
    ]
    searchFile('special@file#name.txt')
    setup_mocks[1].assert_any_call('special@file#name.txt', 'Found')


# edge case - searchFile - Test that the function handles very large file names.
def test_large_file_name(setup_mocks, mock_os_walk):
    mock_os_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', ('Tests',), ('a_very_large_file_name_that_exceeds_normal_length.txt',)),
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests', (), ())
    ]
    searchFile('a_very_large_file_name_that_exceeds_normal_length.txt')
    setup_mocks[1].assert_any_call('a_very_large_file_name_that_exceeds_normal_length.txt', 'Found')


# edge case - searchFile - Test that the function handles permission denied directories gracefully.
def test_permission_denied_directory(setup_mocks, mock_os_walk):
    mock_os_walk.side_effect = PermissionError
    searchFile('6-Folder.txt')
    setup_mocks[2].assert_called_once()


