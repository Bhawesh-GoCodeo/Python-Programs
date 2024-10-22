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
    with mock.patch('os.getcwd', return_value='/mock/current/dir') as mock_getcwd:
        yield mock_getcwd

@pytest.fixture
def mock_path_mkdir():
    with mock.patch.object(Path, 'mkdir') as mock_mkdir:
        yield mock_mkdir

@pytest.fixture
def mock_path_rename():
    with mock.patch.object(Path, 'rename') as mock_rename:
        yield mock_rename

@pytest.fixture
def mock_path_suffix():
    with mock.patch.object(Path, 'suffix', new_callable=mock.PropertyMock) as mock_suffix:
        yield mock_suffix

# happy path - organize_junk - Test that files are moved to their respective directories based on file extension
def test_files_moved_to_respective_directories(mock_os_scandir, mock_path_suffix, mock_path_mkdir, mock_path_rename):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=False), name='file1.html'),
        mock.Mock(is_dir=mock.Mock(return_value=False), name='image1.jpg'),
        mock.Mock(is_dir=mock.Mock(return_value=False), name='document1.pdf')
    ]
    mock_path_suffix.side_effect = ['.html', '.jpg', '.pdf']
    organize_junk()
    mock_path_mkdir.assert_any_call(exist_ok=True)
    mock_path_rename.assert_any_call(Path('HTML/file1.html'))
    mock_path_rename.assert_any_call(Path('IMAGES/image1.jpg'))
    mock_path_rename.assert_any_call(Path('PDF/document1.pdf'))


# happy path - organize_junk - Test that a directory is created for each file type if it doesn't exist
def test_directory_created_if_not_exists(mock_os_scandir, mock_path_suffix, mock_path_mkdir):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=False), name='file1.html'),
        mock.Mock(is_dir=mock.Mock(return_value=False), name='image1.jpg')
    ]
    mock_path_suffix.side_effect = ['.html', '.jpg']
    organize_junk()
    mock_path_mkdir.assert_any_call(exist_ok=True)
    mock_path_mkdir.assert_any_call(exist_ok=True)


# happy path - organize_junk - Test that other files are moved to OTHER-FILES directory
def test_other_files_moved_to_other_files_directory(mock_os_scandir, mock_os_mkdir, mock_os_rename):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=False), name='unknownfile.xyz')
    ]
    organize_junk()
    mock_os_mkdir.assert_called_once_with('OTHER-FILES')
    mock_os_rename.assert_called_once_with('/mock/current/dir/unknownfile.xyz', '/mock/current/dir/OTHER-FILES/unknownfile.xyz')


# happy path - organize_junk - Test that no error is raised when the directory already exists
def test_no_error_if_directory_exists(mock_os_scandir, mock_path_mkdir):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=False), name='file1.html')
    ]
    mock_path_mkdir.side_effect = FileExistsError
    organize_junk()
    mock_path_mkdir.assert_called_once_with(exist_ok=True)


# happy path - organize_junk - Test that empty directories are removed
def test_empty_directories_removed(mock_os_scandir, mock_os_rmdir):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=True), name='EMPTY_DIR')
    ]
    organize_junk()
    mock_os_rmdir.assert_called_once_with(mock_os_scandir.return_value[0])


# edge case - organize_junk - Test that the function handles files with no extension
def test_files_with_no_extension_handling(mock_os_scandir, mock_os_rename):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=False), name='file_without_extension')
    ]
    organize_junk()
    mock_os_rename.assert_called_once_with('/mock/current/dir/file_without_extension', '/mock/current/dir/OTHER-FILES/file_without_extension')


# edge case - organize_junk - Test that the function handles hidden files
def test_hidden_files_handling(mock_os_scandir):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=False), name='.hiddenfile')
    ]
    organize_junk()
    # Assuming hidden files are ignored, no rename should be called
    assert not mock_os_rename.called


# edge case - organize_junk - Test that the function handles very large files
def test_large_files_handling(mock_os_scandir, mock_path_suffix, mock_path_rename):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=False), name='largefile.mp4')
    ]
    mock_path_suffix.return_value = '.mp4'
    organize_junk()
    mock_path_rename.assert_called_once_with(Path('VIDEOS/largefile.mp4'))


# edge case - organize_junk - Test that the function handles files with unusual characters in the name
def test_files_with_unusual_characters(mock_os_scandir, mock_path_suffix, mock_path_rename):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=False), name='unusual@#$.docx')
    ]
    mock_path_suffix.return_value = '.docx'
    organize_junk()
    mock_path_rename.assert_called_once_with(Path('DOCUMENTS/unusual@#$.docx'))


# edge case - organize_junk - Test that the function handles symbolic links
def test_symbolic_links_handling(mock_os_scandir):
    mock_os_scandir.return_value = [
        mock.Mock(is_dir=mock.Mock(return_value=False), name='symlink', is_symlink=mock.Mock(return_value=True))
    ]
    organize_junk()
    # Assuming symbolic links are ignored, no rename should be called
    assert not mock_os_rename.called


