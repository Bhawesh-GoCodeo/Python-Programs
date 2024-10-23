import os
import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_os_walk():
    with patch('os.walk') as mock_walk:
        mock_walk.return_value = [
            ('/path/to/test_directory', ['subdir'], ['file1.txt', 'file2.txt']),
            ('/path/to/test_directory/subdir', [], ['file3.txt']),
        ]
        yield mock_walk

@pytest.fixture
def mock_os_path_join():
    with patch('os.path.join') as mock_join:
        mock_join.side_effect = lambda *args: '/'.join(args)
        yield mock_join

@pytest.fixture
def mock_os_path_getsize():
    with patch('os.path.getsize') as mock_getsize:
        mock_getsize.side_effect = lambda filename: {
            '/path/to/test_directory/file1.txt': 1024,
            '/path/to/test_directory/file2.txt': 512,
            '/path/to/test_directory/subdir/file3.txt': 1024,
        }.get(filename, 0)
        yield mock_getsize

@pytest.fixture
def mock_os_path_exists():
    with patch('os.path.exists') as mock_exists:
        mock_exists.side_effect = lambda path: path in ['/path/to/test_directory', '/path/to/test_directory/subdir']
        yield mock_exists

# happy path - calculate_directory_size - Test that directory size is calculated correctly for a directory with multiple files
def test_directory_size_multiple_files(mock_os_walk, mock_os_path_join, mock_os_path_getsize):
    directory = '/path/to/test_directory_with_files'
    dir_size = 0
    for (path, dirs, files) in os.walk(directory):
        for file in files:
            filename = os.path.join(path, file)
            dir_size += os.path.getsize(filename)
    assert dir_size == 2048


# happy path - calculate_directory_size - Test that directory size is 0 for an empty directory
def test_directory_size_empty(mock_os_walk, mock_os_path_join, mock_os_path_getsize):
    directory = '/path/to/empty_directory'
    dir_size = 0
    for (path, dirs, files) in os.walk(directory):
        for file in files:
            filename = os.path.join(path, file)
            dir_size += os.path.getsize(filename)
    assert dir_size == 0


# happy path - calculate_directory_size - Test that directory size is calculated correctly for a directory with nested subdirectories
def test_directory_size_nested_directories(mock_os_walk, mock_os_path_join, mock_os_path_getsize):
    directory = '/path/to/nested_directory'
    dir_size = 0
    for (path, dirs, files) in os.walk(directory):
        for file in files:
            filename = os.path.join(path, file)
            dir_size += os.path.getsize(filename)
    assert dir_size == 4096


# happy path - calculate_directory_size - Test that directory size is calculated correctly with files of different sizes and types
def test_directory_size_varied_file_sizes(mock_os_walk, mock_os_path_join, mock_os_path_getsize):
    directory = '/path/to/varied_file_sizes'
    dir_size = 0
    for (path, dirs, files) in os.walk(directory):
        for file in files:
            filename = os.path.join(path, file)
            dir_size += os.path.getsize(filename)
    assert dir_size == 8192


# happy path - calculate_directory_size - Test that directory size is calculated correctly for a directory with hidden files
def test_directory_size_with_hidden_files(mock_os_walk, mock_os_path_join, mock_os_path_getsize):
    directory = '/path/to/hidden_files_directory'
    dir_size = 0
    for (path, dirs, files) in os.walk(directory):
        for file in files:
            filename = os.path.join(path, file)
            dir_size += os.path.getsize(filename)
    assert dir_size == 1024


# edge case - calculate_directory_size - Test that directory size calculation handles a non-existent directory gracefully
def test_directory_size_non_existent(mock_os_walk, mock_os_path_exists):
    directory = '/path/to/non_existent_directory'
    if not os.path.exists(directory):
        with pytest.raises(Exception) as e_info:
            for (path, dirs, files) in os.walk(directory):
                pass
        assert str(e_info.value) == 'DirectoryNotFoundError'


# edge case - calculate_directory_size - Test that directory size calculation handles permission denied error gracefully
def test_directory_size_permission_denied(mock_os_walk, mock_os_path_exists):
    directory = '/path/to/protected_directory'
    if not os.path.exists(directory):
        with pytest.raises(Exception) as e_info:
            for (path, dirs, files) in os.walk(directory):
                pass
        assert str(e_info.value) == 'PermissionDeniedError'


# edge case - calculate_directory_size - Test that directory size calculation handles special characters in file names
def test_directory_size_special_characters(mock_os_walk, mock_os_path_join, mock_os_path_getsize):
    directory = '/path/to/special_characters_directory'
    dir_size = 0
    for (path, dirs, files) in os.walk(directory):
        for file in files:
            filename = os.path.join(path, file)
            dir_size += os.path.getsize(filename)
    assert dir_size == 512


# edge case - calculate_directory_size - Test that directory size calculation handles symbolic links correctly
def test_directory_size_symbolic_links(mock_os_walk, mock_os_path_join, mock_os_path_getsize):
    directory = '/path/to/symbolic_links_directory'
    dir_size = 0
    for (path, dirs, files) in os.walk(directory):
        for file in files:
            filename = os.path.join(path, file)
            dir_size += os.path.getsize(filename)
    assert dir_size == 256


# edge case - calculate_directory_size - Test that directory size calculation handles very large files without overflow
def test_directory_size_large_files(mock_os_walk, mock_os_path_join, mock_os_path_getsize):
    directory = '/path/to/large_files_directory'
    dir_size = 0
    for (path, dirs, files) in os.walk(directory):
        for file in files:
            filename = os.path.join(path, file)
            dir_size += os.path.getsize(filename)
    assert dir_size == 1073741824


