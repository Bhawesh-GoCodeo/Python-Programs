import pytest
from unittest import mock
import os

# Mocking os.walk
@mock.patch('os.walk')
# Mocking os.path.join
@mock.patch('os.path.join')
# Mocking os.path.getsize
@mock.patch('os.path.getsize')
def mock_setup(mock_getsize, mock_join, mock_walk):
    # Setup mock for os.walk
    mock_walk.return_value = [
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts', ['subdir1'], ['file1.txt', 'file2.txt']),
        ('/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/subdir1', [], ['file3.txt'])
    ]
    
    # Setup mock for os.path.join
    mock_join.side_effect = lambda *args: "/".join(args)
    
    # Setup mock for os.path.getsize
    mock_getsize.side_effect = lambda filename: 123456 if filename == '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/file1.txt' else 789012 if filename == '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/file2.txt' else 345678 if filename == '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts/subdir1/file3.txt' else 0

@pytest.fixture
def setup_mocks():
    with mock.patch('os.walk') as mock_walk, \
         mock.patch('os.path.join') as mock_join, \
         mock.patch('os.path.getsize') as mock_getsize:
        mock_setup(mock_getsize, mock_join, mock_walk)
        yield

# happy path - calculate_directory_size - Test that the function calculates the correct directory size in bytes.
def test_calculate_directory_size_bytes(setup_mocks):
    directory = '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts'
    expected_size = 123456 + 789012 + 345678
    assert calculate_directory_size(directory) == expected_size


# happy path - calculate_directory_size - Test that the function calculates the correct directory size in kilobytes.
def test_calculate_directory_size_kilobytes(setup_mocks):
    directory = '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts'
    expected_size_kb = round((123456 + 789012 + 345678) / 1024, 2)
    assert calculate_directory_size(directory, unit='Kilobytes') == expected_size_kb


# happy path - calculate_directory_size - Test that the function calculates the correct directory size in megabytes.
def test_calculate_directory_size_megabytes(setup_mocks):
    directory = '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts'
    expected_size_mb = round((123456 + 789012 + 345678) / (1024 * 1024), 2)
    assert calculate_directory_size(directory, unit='Megabytes') == expected_size_mb


# happy path - calculate_directory_size - Test that the function calculates the correct directory size in gigabytes.
def test_calculate_directory_size_gigabytes(setup_mocks):
    directory = '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts'
    expected_size_gb = round((123456 + 789012 + 345678) / (1024 * 1024 * 1024), 2)
    assert calculate_directory_size(directory, unit='Gigabytes') == expected_size_gb


# happy path - calculate_directory_size - Test that the function returns zero size for an empty directory.
def test_calculate_directory_size_empty(setup_mocks):
    directory = '/home/omkarpathak/Documents/GITs/EmptyDirectory'
    assert calculate_directory_size(directory) == 0


# edge case - calculate_directory_size - Test that the function handles a non-existent directory gracefully.
def test_calculate_directory_size_non_existent(setup_mocks):
    directory = '/non/existent/directory'
    with pytest.raises(DirectoryNotFoundError):
        calculate_directory_size(directory)


# edge case - calculate_directory_size - Test that the function handles directories with no read permission.
def test_calculate_directory_size_no_permission(setup_mocks):
    directory = '/home/omkarpathak/Documents/NoPermissionDirectory'
    with pytest.raises(PermissionError):
        calculate_directory_size(directory)


# edge case - calculate_directory_size - Test that the function handles a directory with a large number of small files.
def test_calculate_directory_size_many_files(setup_mocks):
    directory = '/home/omkarpathak/Documents/LargeNumberOfFiles'
    expected_size = 987654321
    assert calculate_directory_size(directory) == expected_size


# edge case - calculate_directory_size - Test that the function handles symbolic links correctly.
def test_calculate_directory_size_symlinks(setup_mocks):
    directory = '/home/omkarpathak/Documents/SymlinksDirectory'
    expected_size = 456789
    assert calculate_directory_size(directory) == expected_size


# edge case - calculate_directory_size - Test that the function handles directories with special characters in the name.
def test_calculate_directory_size_special_chars(setup_mocks):
    directory = '/home/omkarpathak/Documents/Special!@#$%^&*()'
    expected_size = 123456
    assert calculate_directory_size(directory) == expected_size


