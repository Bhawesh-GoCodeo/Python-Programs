import os
from pathlib import Path
import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_os_scandir():
    with patch('os.scandir') as mock:
        yield mock

@pytest.fixture
def mock_os_mkdir():
    with patch('os.mkdir') as mock:
        yield mock

@pytest.fixture
def mock_os_rmdir():
    with patch('os.rmdir') as mock:
        yield mock

@pytest.fixture
def mock_os_rename():
    with patch('os.rename') as mock:
        yield mock

@pytest.fixture
def mock_os_getcwd():
    with patch('os.getcwd', return_value='/mock/current/directory') as mock:
        yield mock

@pytest.fixture
def mock_pathlib_path():
    with patch('pathlib.Path') as mock:
        mock_instance = MagicMock()
        mock_instance.suffix.lower.return_value = '.mock'
        mock_instance.name = 'mock_file.mock'
        mock_instance.joinpath.return_value = mock_instance
        mock_instance.mkdir = MagicMock()
        yield mock_instance

@pytest.fixture
def mock_path_instance():
    with patch('pathlib.Path') as mock:
        yield mock

@pytest.fixture
def mock_os_path():
    with patch('os.path') as mock:
        yield mock

@pytest.fixture
def mock_os_dir_entry():
    mock_entry = MagicMock()
    mock_entry.is_dir.return_value = False
    mock_entry.name = 'mock_file.txt'
    return mock_entry

# happy path - organize_junk - Test that files are moved to respective directories based on their extensions
def test_files_moved_to_correct_directories(mock_os_scandir, mock_path_instance, mock_os_rename):
    mock_entry = MagicMock()
    mock_entry.is_dir.return_value = False
    mock_entry.name = 'example.html'
    mock_os_scandir.return_value = [mock_entry]
    mock_path_instance().suffix.lower.return_value = '.html'

    organize_junk()

    mock_path_instance().joinpath.assert_called_with(mock_path_instance())
    mock_os_rename.assert_called()


# happy path - organize_junk - Test that non-matching files are moved to OTHER-FILES directory
def test_non_matching_files_moved_to_other_files(mock_os_scandir, mock_os_mkdir, mock_os_rename):
    mock_entry = MagicMock()
    mock_entry.is_dir.return_value = False
    mock_entry.name = 'example.unknown'
    mock_os_scandir.return_value = [mock_entry]

    organize_junk()

    mock_os_mkdir.assert_called_with('OTHER-FILES')
    mock_os_rename.assert_called()


# happy path - organize_junk - Test that directories are not treated as files and skipped
def test_directories_are_skipped(mock_os_scandir):
    mock_entry = MagicMock()
    mock_entry.is_dir.return_value = True
    mock_os_scandir.return_value = [mock_entry]

    organize_junk()

    mock_entry.is_dir.assert_called()


# happy path - organize_junk - Test that existing directories are not recreated
def test_existing_directories_not_recreated(mock_os_scandir, mock_path_instance):
    mock_entry = MagicMock()
    mock_entry.is_dir.return_value = False
    mock_entry.name = 'example.txt'
    mock_os_scandir.return_value = [mock_entry]

    mock_path_instance().mkdir.side_effect = FileExistsError

    organize_junk()

    mock_path_instance().mkdir.assert_called()


# happy path - organize_junk - Test that organize_junk runs without exceptions
def test_organize_junk_runs_without_exceptions(mock_os_scandir):
    mock_entry = MagicMock()
    mock_entry.is_dir.return_value = False
    mock_entry.name = 'example.txt'
    mock_os_scandir.return_value = [mock_entry]

    try:
        organize_junk()
        assert True
    except Exception:
        assert False


# edge case - organize_junk - Test that no files are moved if directory is empty
def test_no_files_moved_if_directory_empty(mock_os_scandir, mock_os_rename):
    mock_os_scandir.return_value = []

    organize_junk()

    mock_os_rename.assert_not_called()


# edge case - organize_junk - Test that hidden files are ignored
def test_hidden_files_ignored(mock_os_scandir, mock_os_rename):
    mock_entry = MagicMock()
    mock_entry.is_dir.return_value = False
    mock_entry.name = '.hiddenfile'
    mock_os_scandir.return_value = [mock_entry]

    organize_junk()

    mock_os_rename.assert_not_called()


# edge case - organize_junk - Test that files with no extension are moved to OTHER-FILES
def test_files_with_no_extension_moved_to_other_files(mock_os_scandir, mock_os_mkdir, mock_os_rename):
    mock_entry = MagicMock()
    mock_entry.is_dir.return_value = False
    mock_entry.name = 'file'
    mock_os_scandir.return_value = [mock_entry]

    organize_junk()

    mock_os_mkdir.assert_called_with('OTHER-FILES')
    mock_os_rename.assert_called()


# edge case - organize_junk - Test that files with uppercase extensions are handled correctly
def test_uppercase_extensions_handled_correctly(mock_os_scandir, mock_path_instance, mock_os_rename):
    mock_entry = MagicMock()
    mock_entry.is_dir.return_value = False
    mock_entry.name = 'example.JPG'
    mock_os_scandir.return_value = [mock_entry]
    mock_path_instance().suffix.lower.return_value = '.jpg'

    organize_junk()

    mock_path_instance().joinpath.assert_called_with(mock_path_instance())
    mock_os_rename.assert_called()


# edge case - organize_junk - Test that organize_junk handles permission errors gracefully
def test_permission_errors_handled_gracefully(mock_os_scandir, mock_os_mkdir):
    mock_entry = MagicMock()
    mock_entry.is_dir.return_value = False
    mock_entry.name = 'example.txt'
    mock_os_scandir.return_value = [mock_entry]
    mock_os_mkdir.side_effect = PermissionError

    try:
        organize_junk()
        assert True
    except PermissionError:
        assert False


