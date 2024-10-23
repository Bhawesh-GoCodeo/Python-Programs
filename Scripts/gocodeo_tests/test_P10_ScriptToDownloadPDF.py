import pytest
from unittest import mock
import urllib.request
from Scripts.P10_ScriptToDownloadPDF import download

@pytest.fixture
def mock_download_setup():
    with mock.patch('urllib.request.urlopen') as mock_urlopen:
        mock_urlopen.return_value.read.return_value = b'%PDF-1.4...'
        
        with mock.patch('builtins.open', mock.mock_open()) as mock_open:
            with mock.patch('builtins.print') as mock_print:
                yield mock_urlopen, mock_open, mock_print

def test_download_valid_tutorial(mock_download_setup):
    tutorialName = 'python'
    download(tutorialName)
    mock_download_setup[0].assert_called_once_with('https://www.tutorialspoint.com/python/python_tutorial.pdf')
    mock_download_setup[1].assert_called_once_with('/home/omkarpathak/Downloads/python.pdf', 'wb')
    mock_download_setup[2].assert_called_once_with('Downloaded!')

# happy path - download - Test that a valid tutorial name downloads the correct PDF file
def test_download_valid_tutorial(mock_download_setup):
    tutorialName = 'python'
    download(tutorialName)
    mock_download_setup[0].assert_called_once_with('https://www.tutorialspoint.com/python/python_tutorial.pdf')
    mock_download_setup[1].assert_called_once_with('/home/omkarpathak/Downloads/python.pdf', 'wb')
    mock_download_setup[2].assert_called_once_with('Downloaded!')


# happy path - download - Test that a tutorial name with special characters downloads the correct PDF
def test_download_special_characters(mock_download_setup):
    tutorialName = 'c++'
    download(tutorialName)
    mock_download_setup[0].assert_called_once_with('https://www.tutorialspoint.com/c++/c++_tutorial.pdf')
    mock_download_setup[1].assert_called_once_with('/home/omkarpathak/Downloads/c++.pdf', 'wb')
    mock_download_setup[2].assert_called_once_with('Downloaded!')


# happy path - download - Test that a tutorial name with numbers downloads the correct PDF
def test_download_with_numbers(mock_download_setup):
    tutorialName = 'java8'
    download(tutorialName)
    mock_download_setup[0].assert_called_once_with('https://www.tutorialspoint.com/java8/java8_tutorial.pdf')
    mock_download_setup[1].assert_called_once_with('/home/omkarpathak/Downloads/java8.pdf', 'wb')
    mock_download_setup[2].assert_called_once_with('Downloaded!')


# happy path - download - Test that a tutorial name with mixed case downloads the correct PDF
def test_download_mixed_case(mock_download_setup):
    tutorialName = 'Python'
    download(tutorialName)
    mock_download_setup[0].assert_called_once_with('https://www.tutorialspoint.com/Python/Python_tutorial.pdf')
    mock_download_setup[1].assert_called_once_with('/home/omkarpathak/Downloads/Python.pdf', 'wb')
    mock_download_setup[2].assert_called_once_with('Downloaded!')


# happy path - download - Test that a valid tutorial name with spaces downloads the correct PDF
def test_download_with_spaces(mock_download_setup):
    tutorialName = 'data science'
    download(tutorialName)
    mock_download_setup[0].assert_called_once_with('https://www.tutorialspoint.com/data science/data science_tutorial.pdf')
    mock_download_setup[1].assert_called_once_with('/home/omkarpathak/Downloads/data science.pdf', 'wb')
    mock_download_setup[2].assert_called_once_with('Downloaded!')


# edge case - download - Test that an empty tutorial name raises an error
def test_download_empty_tutorial(mock_download_setup):
    tutorialName = ''
    with pytest.raises(ValueError, match='Invalid tutorial name'):
        download(tutorialName)


# edge case - download - Test that a non-existent tutorial name raises an error
def test_download_non_existent_tutorial(mock_download_setup):
    tutorialName = 'nonexistent'
    mock_download_setup[0].side_effect = urllib.error.HTTPError(url='', code=404, msg='Not Found', hdrs=None, fp=None)
    with pytest.raises(urllib.error.HTTPError, match='404 Not Found'):
        download(tutorialName)


# edge case - download - Test that a tutorial name with only special characters raises an error
def test_download_only_special_characters(mock_download_setup):
    tutorialName = '$$$'
    with pytest.raises(ValueError, match='Invalid tutorial name'):
        download(tutorialName)


# edge case - download - Test that a very long tutorial name raises an error
def test_download_very_long_name(mock_download_setup):
    tutorialName = 'a_very_long_tutorial_name_exceeding_limits'
    with pytest.raises(ValueError, match='Tutorial name too long'):
        download(tutorialName)


# edge case - download - Test that a tutorial name with path traversal raises an error
def test_download_path_traversal(mock_download_setup):
    tutorialName = '../etc/passwd'
    with pytest.raises(SecurityError, match='Invalid tutorial name'):
        download(tutorialName)


