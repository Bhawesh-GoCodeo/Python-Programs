import os
import pytest
from unittest import mock

@pytest.fixture
def mock_os_walk():
    with mock.patch('os.walk') as mock_walk:
        yield mock_walk

@pytest.fixture
def mock_print():
    with mock.patch('builtins.print') as mock_print_func:
        yield mock_print_func

# happy path - os.walk - Test that the function counts files and directories correctly in a directory with mixed content
def test_count_files_and_dirs_mixed_content(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/path/to/mixed_content_directory', ['dir1', 'dir2', 'dir3'], ['file1', 'file2', 'file3', 'file4', 'file5'])
    ]
    exec(open('Scripts/P02_FileCount.py').read())
    mock_print.assert_any_call('Number of files', 5)
    mock_print.assert_any_call('Number of Directories', 3)
    mock_print.assert_any_call('Total:', 8)


# happy path - os.walk - Test that the function counts only files correctly when no directories are present
def test_count_only_files(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/path/to/files_only_directory', [], ['file1', 'file2', 'file3', 'file4', 'file5', 'file6', 'file7', 'file8', 'file9', 'file10'])
    ]
    exec(open('Scripts/P02_FileCount.py').read())
    mock_print.assert_any_call('Number of files', 10)
    mock_print.assert_any_call('Number of Directories', 0)
    mock_print.assert_any_call('Total:', 10)


# happy path - os.walk - Test that the function counts only directories correctly when no files are present
def test_count_only_dirs(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/path/to/dirs_only_directory', ['dir1', 'dir2', 'dir3', 'dir4', 'dir5'], [])
    ]
    exec(open('Scripts/P02_FileCount.py').read())
    mock_print.assert_any_call('Number of files', 0)
    mock_print.assert_any_call('Number of Directories', 5)
    mock_print.assert_any_call('Total:', 5)


# happy path - os.walk - Test that the function returns zero counts for an empty directory
def test_empty_directory(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/path/to/empty_directory', [], [])
    ]
    exec(open('Scripts/P02_FileCount.py').read())
    mock_print.assert_any_call('Number of files', 0)
    mock_print.assert_any_call('Number of Directories', 0)
    mock_print.assert_any_call('Total:', 0)


# happy path - os.walk - Test that the function handles a directory with nested subdirectories and files
def test_nested_directories(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/path/to/nested_directory', ['dir1', 'dir2'], ['file1', 'file2']),
        ('/path/to/nested_directory/dir1', ['dir3'], ['file3']),
        ('/path/to/nested_directory/dir1/dir3', [], ['file4', 'file5']),
        ('/path/to/nested_directory/dir2', [], ['file6', 'file7', 'file8', 'file9', 'file10']),
        ('/path/to/nested_directory/dir2/dir4', [], ['file11', 'file12', 'file13', 'file14', 'file15']),
        ('/path/to/nested_directory/dir2/dir5', [], ['file16', 'file17', 'file18', 'file19', 'file20'])
    ]
    exec(open('Scripts/P02_FileCount.py').read())
    mock_print.assert_any_call('Number of files', 20)
    mock_print.assert_any_call('Number of Directories', 10)
    mock_print.assert_any_call('Total:', 30)


# happy path - os.walk - Test that the function works with a directory containing special character filenames
def test_special_character_filenames(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/path/to/special_character_directory', ['dir1', 'dir2'], ['file@1', 'file#2', 'file&3'])
    ]
    exec(open('Scripts/P02_FileCount.py').read())
    mock_print.assert_any_call('Number of files', 3)
    mock_print.assert_any_call('Number of Directories', 2)
    mock_print.assert_any_call('Total:', 5)


# edge case - os.walk - Test that the function handles a non-existent directory path gracefully
def test_non_existent_directory(mock_os_walk, mock_print):
    mock_os_walk.return_value = []
    exec(open('Scripts/P02_FileCount.py').read())
    mock_print.assert_any_call('Number of files', 0)
    mock_print.assert_any_call('Number of Directories', 0)
    mock_print.assert_any_call('Total:', 0)


# edge case - os.walk - Test that the function handles directory paths with permission issues
def test_permission_issue_directory(mock_os_walk, mock_print):
    mock_os_walk.side_effect = PermissionError
    exec(open('Scripts/P02_FileCount.py').read())
    mock_print.assert_any_call('Number of files', 0)
    mock_print.assert_any_call('Number of Directories', 0)
    mock_print.assert_any_call('Total:', 0)


# edge case - os.walk - Test that the function handles a directory path that is a file instead of a directory
def test_file_instead_of_directory(mock_os_walk, mock_print):
    mock_os_walk.return_value = []
    exec(open('Scripts/P02_FileCount.py').read())
    mock_print.assert_any_call('Number of files', 0)
    mock_print.assert_any_call('Number of Directories', 0)
    mock_print.assert_any_call('Total:', 0)


# edge case - os.walk - Test that the function handles a directory with symbolic links
def test_directory_with_symlinks(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/path/to/symlink_directory', ['dir1', 'dir2'], ['file1', 'file2', 'file3']),
        ('/path/to/symlink_directory/dir1', [], ['file4', 'file5'])
    ]
    exec(open('Scripts/P02_FileCount.py').read())
    mock_print.assert_any_call('Number of files', 5)
    mock_print.assert_any_call('Number of Directories', 3)
    mock_print.assert_any_call('Total:', 8)


# edge case - os.walk - Test that the function handles a directory with very large number of files and directories
def test_large_number_of_files_and_dirs(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/path/to/large_directory', ['dir{}'.format(i) for i in range(500)], ['file{}'.format(i) for i in range(1000)])
    ]
    exec(open('Scripts/P02_FileCount.py').read())
    mock_print.assert_any_call('Number of files', 1000)
    mock_print.assert_any_call('Number of Directories', 500)
    mock_print.assert_any_call('Total:', 1500)


# edge case - os.walk - Test that the function handles a directory with hidden files and directories
def test_hidden_files_and_dirs(mock_os_walk, mock_print):
    mock_os_walk.return_value = [
        ('/path/to/hidden_directory', ['.hidden_dir'], ['.hidden_file1', '.hidden_file2'])
    ]
    exec(open('Scripts/P02_FileCount.py').read())
    mock_print.assert_any_call('Number of files', 2)
    mock_print.assert_any_call('Number of Directories', 1)
    mock_print.assert_any_call('Total:', 3)


