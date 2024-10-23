import pytest
from unittest.mock import patch
from Programs.P01_hello import justPrint

@pytest.fixture
def mock_print():
    with patch('builtins.print') as mock:
        yield mock

def test_just_print_simple_string(mock_print):
    justPrint('Hello, World!')
    mock_print.assert_called_once_with('Hello, World!')

def test_just_print_empty_string(mock_print):
    justPrint('')
    mock_print.assert_called_once_with('')

def test_just_print_special_characters(mock_print):
    justPrint('@#$%^&*()_+')
    mock_print.assert_called_once_with('@#$%^&*()_+')

def test_just_print_numbers(mock_print):
    justPrint('1234567890')
    mock_print.assert_called_once_with('1234567890')

def test_just_print_multiline_string(mock_print):
    justPrint('Hello\nWorld')
    mock_print.assert_called_once_with('Hello\nWorld')

def test_just_print_none(mock_print):
    justPrint(None)
    mock_print.assert_called_once_with(None)

def test_just_print_long_string(mock_print):
    long_string = 'a' * 1000
    justPrint(long_string)
    mock_print.assert_called_once_with(long_string)

def test_just_print_escape_sequences(mock_print):
    justPrint('Line1\nLine2\tTabbed')
    mock_print.assert_called_once_with('Line1\nLine2\tTabbed')

def test_just_print_unicode(mock_print):
    justPrint('こんにちは')
    mock_print.assert_called_once_with('こんにちは')

def test_just_print_mixed_content(mock_print):
    justPrint('1234!@#$abcd')
    mock_print.assert_called_once_with('1234!@#$abcd')

# happy path - justPrint - Test that justPrint prints a simple string
def test_just_print_simple_string(mock_print):
    justPrint('Hello, World!')
    mock_print.assert_called_once_with('Hello, World!')


# happy path - justPrint - Test that justPrint prints an empty string
def test_just_print_empty_string(mock_print):
    justPrint('')
    mock_print.assert_called_once_with('')


# happy path - justPrint - Test that justPrint prints a string with special characters
def test_just_print_special_characters(mock_print):
    justPrint('@#$%^&*()_+')
    mock_print.assert_called_once_with('@#$%^&*()_+')


# happy path - justPrint - Test that justPrint prints a string with numbers
def test_just_print_numbers(mock_print):
    justPrint('1234567890')
    mock_print.assert_called_once_with('1234567890')


# happy path - justPrint - Test that justPrint prints a multiline string
def test_just_print_multiline_string(mock_print):
    justPrint('Hello\nWorld')
    mock_print.assert_called_once_with('Hello\nWorld')


# edge case - justPrint - Test that justPrint handles None as input
def test_just_print_none(mock_print):
    justPrint(None)
    mock_print.assert_called_once_with(None)


# edge case - justPrint - Test that justPrint prints a very long string
def test_just_print_long_string(mock_print):
    long_string = 'a' * 1000
    justPrint(long_string)
    mock_print.assert_called_once_with(long_string)


# edge case - justPrint - Test that justPrint handles a string with escape sequences
def test_just_print_escape_sequences(mock_print):
    justPrint('Line1\nLine2\tTabbed')
    mock_print.assert_called_once_with('Line1\nLine2\tTabbed')


# edge case - justPrint - Test that justPrint prints a string with unicode characters
def test_just_print_unicode(mock_print):
    justPrint('こんにちは')
    mock_print.assert_called_once_with('こんにちは')


# edge case - justPrint - Test that justPrint handles a string with mixed content
def test_just_print_mixed_content(mock_print):
    justPrint('1234!@#$abcd')
    mock_print.assert_called_once_with('1234!@#$abcd')


