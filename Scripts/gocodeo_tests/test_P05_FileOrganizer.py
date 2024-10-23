import os
import pytest
from unittest import mock
from pathlib import Path
from Scripts.P05_FileOrganizer import organize_junk

@pytest.fixture
def mock_os_scandir():
    with mock.patch('os.scandir') as mock_scandir:
        yield mock_scandir

@pytest.fixture
def mock_os_mkdir():
    with mock.patch('os.mkdir') as mock_mkdir:
        yield mock_mkdir

@pytest.fixture
def mock_os_rmdir():
    with mock.patch('os.rmdir') as mock_rmdir:
        yield mock_rmdir

@pytest.fixture
def mock_os_rename():
    with mock.patch('os.rename') as mock_rename:
        yield mock_rename

@pytest.fixture
def mock_os_getcwd():
    with mock.patch('os.getcwd', return_value='/mock/current/directory') as mock_getcwd:
        yield mock_getcwd

@pytest.fixture
def mock_path_mkdir():
    with mock.patch.object(Path, 'mkdir') as mock_mkdir:
        yield mock_mkdir

@pytest.fixture
def mock_path_suffix():
    with mock.patch.object(Path, 'suffix', new_callable=mock.PropertyMock) as mock_suffix:
        yield mock_suffix

@pytest.fixture
def mock_path_joinpath():
    with mock.patch.object(Path, 'joinpath') as mock_joinpath:
        yield mock_joinpath

@pytest.fixture
def mock_path_exists():
    with mock.patch('pathlib.Path.exists', return_value=False) as mock_exists:
        yield mock_exists

# happy path - organize_junk - Test that files are moved to their respective directories based on file extension
def test_files_moved_to_respective_directories(mock_os_scandir, mock_path_mkdir, mock_os_rename, mock_path_suffix, mock_path_joinpath):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=False), name='test.jpg'),
        mock.Mock(is_dir=mock.Mock(return_value=False), name='document.pdf')
    ]
    mock_path_suffix.side_effect = ['.jpg', '.pdf']
    organize_junk()
    mock_path_mkdir.assert_any_call(exist_ok=True)
    mock_os_rename.assert_any_call('/mock/current/directory/test.jpg', '/mock/current/directory/IMAGES/test.jpg')
    mock_os_rename.assert_any_call('/mock/current/directory/document.pdf', '/mock/current/directory/PDF/document.pdf')


# happy path - organize_junk - Test that the OTHER-FILES directory is created when there are files with unknown extensions
def test_other_files_directory_created(mock_os_scandir, mock_os_mkdir, mock_os_rename):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=False), name='unknownfile.xyz')
    ]
    organize_junk()
    mock_os_mkdir.assert_called_with('OTHER-FILES')
    mock_os_rename.assert_called_with('/mock/current/directory/unknownfile.xyz', '/mock/current/directory/OTHER-FILES/unknownfile.xyz')


# happy path - organize_junk - Test that empty directories are removed after organizing
def test_empty_directories_removed(mock_os_scandir, mock_os_rmdir):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=True), name='emptydir')
    ]
    organize_junk()
    mock_os_rmdir.assert_called_with('emptydir')


# happy path - organize_junk - Test that no exception occurs when directories already exist
def test_no_exception_on_existing_directories(mock_os_scandir, mock_path_mkdir):
    mock_os_scandir.return_value = []
    organize_junk()
    mock_path_mkdir.assert_called()
    # Check that no exception is raised by ensuring the test completes without errors.


# happy path - organize_junk - Test that files with uppercase extensions are handled correctly
def test_uppercase_extensions_handled(mock_os_scandir, mock_path_mkdir, mock_os_rename, mock_path_suffix):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=False), name='IMAGE.JPG')
    ]
    mock_path_suffix.side_effect = ['.JPG']
    organize_junk()
    mock_path_mkdir.assert_called_with(exist_ok=True)
    mock_os_rename.assert_called_with('/mock/current/directory/IMAGE.JPG', '/mock/current/directory/IMAGES/IMAGE.JPG')


# edge case - organize_junk - Test that no error occurs when there are no files to organize
def test_no_files_to_organize(mock_os_scandir):
    mock_os_scandir.return_value = []
    organize_junk()
    # Ensure the function completes without errors.


# edge case - organize_junk - Test that no error occurs when a file cannot be moved due to permission issues
def test_permission_issue_handling(mock_os_scandir, mock_os_rename):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=False), name='protectedfile.txt')
    ]
    mock_os_rename.side_effect = PermissionError
    organize_junk()
    # Ensure the function completes without errors despite the permission error.


# edge case - organize_junk - Test that files with no extension are moved to OTHER-FILES
def test_files_with_no_extension(mock_os_scandir, mock_os_mkdir, mock_os_rename):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=False), name='filewithoutextension')
    ]
    organize_junk()
    mock_os_mkdir.assert_called_with('OTHER-FILES')
    mock_os_rename.assert_called_with('/mock/current/directory/filewithoutextension', '/mock/current/directory/OTHER-FILES/filewithoutextension')


# edge case - organize_junk - Test that directories with similar names to file extensions are not incorrectly removed
def test_similar_named_directories_not_removed(mock_os_scandir, mock_os_rmdir):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=True), name='txt')
    ]
    organize_junk()
    mock_os_rmdir.assert_not_called()


# edge case - organize_junk - Test that an error is handled when trying to move a file to a non-writable directory
def test_non_writable_directory_error_handling(mock_os_scandir, mock_path_mkdir, mock_os_rename):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=False), name='readonlyfile.txt')
    ]
    mock_path_mkdir.side_effect = PermissionError
    organize_junk()
    # Ensure the function completes without errors despite the permission error.


