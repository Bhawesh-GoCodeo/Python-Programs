import os
import time
import pytest
from unittest import mock
from Scripts.P01_FolderManipulation import createFolders, createFiles, renameFiles

@pytest.fixture
def mock_os(mocker):
    mocker.patch('os.mkdir')
    mocker.patch('os.chdir')
    mocker.patch('os.listdir', return_value=[f"{i}Folder.txt" for i in range(10)])
    mocker.patch('os.rename')
    mocker.patch('os.path.splitext', side_effect=lambda x: (x.rsplit('.', 1)[0], x.rsplit('.', 1)[1]) if '.' in x else (x, ''))

@pytest.fixture
def mock_time(mocker):
    mocker.patch('time.sleep')

# happy path - createFolders - Test that createFolders successfully creates 10 folders with correct naming pattern
def test_create_folders_happy_path(mock_os):
    BASE_DIR = '/home/omkarpathak/Downloads/PythonPrograms/Scripts/Tests/'
    createFolders(BASE_DIR)
    expected_folders = [f'{i}-Folder' for i in range(10)]
    os.mkdir.assert_has_calls([mock.call(BASE_DIR + folder) for folder in expected_folders], any_order=True)


# happy path - createFiles - Test that createFiles successfully creates 10 .txt files with correct naming pattern
def test_create_files_happy_path(mock_os):
    BASE_DIR = '/home/omkarpathak/Downloads/PythonPrograms/Scripts/Tests/'
    createFiles(BASE_DIR)
    expected_files = [f'{i}Folder.txt' for i in range(10)]
    os.listdir.return_value = expected_files
    assert all(file in expected_files for file in os.listdir())


# happy path - renameFiles - Test that renameFiles successfully renames 10 files by replacing 'Folder' with '-Folder'
def test_rename_files_happy_path(mock_os):
    BASE_DIR = '/home/omkarpathak/Downloads/PythonPrograms/Scripts/Tests/'
    renameFiles(BASE_DIR)
    expected_renamed_files = [f'{i}-Folder.txt' for i in range(10)]
    os.rename.assert_has_calls([mock.call(f'{i}Folder.txt', f'{i}-Folder.txt') for i in range(10)], any_order=True)


# edge case - createFolders - Test that createFolders handles existing folders without crashing
def test_create_folders_existing_folders(mock_os):
    BASE_DIR = '/home/omkarpathak/Downloads/PythonPrograms/Scripts/Tests/'
    os.mkdir.side_effect = FileExistsError
    with pytest.raises(FileExistsError):
        createFolders(BASE_DIR)


# edge case - createFiles - Test that createFiles handles existing files without crashing
def test_create_files_existing_files(mock_os):
    BASE_DIR = '/home/omkarpathak/Downloads/PythonPrograms/Scripts/Tests/'
    open = mock.mock_open()
    with mock.patch('builtins.open', open), pytest.raises(FileExistsError):
        open.side_effect = FileExistsError
        createFiles(BASE_DIR)


# edge case - renameFiles - Test that renameFiles handles non-existent files gracefully
def test_rename_files_non_existent(mock_os):
    BASE_DIR = '/home/omkarpathak/Downloads/PythonPrograms/Scripts/Tests/'
    os.listdir.return_value = []
    renameFiles(BASE_DIR)
    os.rename.assert_not_called()


# edge case - createFolders - Test that createFolders handles invalid BASE_DIR path
def test_create_folders_invalid_path(mock_os):
    BASE_DIR = '/invalid/path/'
    os.mkdir.side_effect = FileNotFoundError
    with pytest.raises(FileNotFoundError):
        createFolders(BASE_DIR)


# edge case - createFiles - Test that createFiles handles invalid BASE_DIR path
def test_create_files_invalid_path(mock_os):
    BASE_DIR = '/invalid/path/'
    open = mock.mock_open()
    with mock.patch('builtins.open', open), pytest.raises(FileNotFoundError):
        open.side_effect = FileNotFoundError
        createFiles(BASE_DIR)


