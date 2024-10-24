import pytest
from unittest import mock
from Programs.P01_hello import justPrint

@pytest.fixture
def mock_print(mocker):
    mocker.patch('builtins.print')

def test_print_simple_string(mock_print):
    justPrint('Hello, World!')
    mock_print.assert_called_once_with('Hello, World!')

def test_print_number_string(mock_print):
    justPrint('12345')
    mock_print.assert_called_once_with('12345')

def test_print_long_string(mock_print):
    justPrint('This is a very long string used to test the print functionality.')
    mock_print.assert_called_once_with('This is a very long string used to test the print functionality.')

def test_print_special_characters(mock_print):
    justPrint("!@#$%^&*()_+-=[]{}|;':,.<>/?`~")
    mock_print.assert_called_once_with("!@#$%^&*()_+-=[]{}|;':,.<>/?`~")

def test_print_newline_characters(mock_print):
    justPrint('Line 1\nLine 2\nLine 3')
    mock_print.assert_called_once_with('Line 1\nLine 2\nLine 3')

def test_print_empty_string(mock_print):
    justPrint('')
    mock_print.assert_called_once_with('')

def test_print_whitespace_string(mock_print):
    justPrint('     ')
    mock_print.assert_called_once_with('     ')

def test_print_single_character(mock_print):
    justPrint('A')
    mock_print.assert_called_once_with('A')

def test_print_unicode_string(mock_print):
    justPrint('こんにちは世界')
    mock_print.assert_called_once_with('こんにちは世界')

def test_print_none_value(mock_print):
    justPrint(str(None))
    mock_print.assert_called_once_with('None')

# happy path - justPrint - Test that the function prints a simple string correctly.
def test_print_simple_string(mock_print):
    justPrint('Hello, World!')
    mock_print.assert_called_once_with('Hello, World!')


# happy path - justPrint - Test that the function prints a number as a string correctly.
def test_print_number_string(mock_print):
    justPrint('12345')
    mock_print.assert_called_once_with('12345')


# happy path - justPrint - Test that the function prints a long string correctly.
def test_print_long_string(mock_print):
    justPrint('This is a very long string used to test the print functionality.')
    mock_print.assert_called_once_with('This is a very long string used to test the print functionality.')


# happy path - justPrint - Test that the function prints a string with special characters.
def test_print_special_characters(mock_print):
    justPrint("!@#$%^&*()_+-=[]{}|;':,.<>/?`~")
    mock_print.assert_called_once_with("!@#$%^&*()_+-=[]{}|;':,.<>/?`~")


# happy path - justPrint - Test that the function prints a string with newline characters.
def test_print_newline_characters(mock_print):
    justPrint('Line 1\nLine 2\nLine 3')
    mock_print.assert_called_once_with('Line 1\nLine 2\nLine 3')


# edge case - justPrint - Test that the function prints an empty string.
def test_print_empty_string(mock_print):
    justPrint('')
    mock_print.assert_called_once_with('')


# edge case - justPrint - Test that the function prints a string with only whitespace.
def test_print_whitespace_string(mock_print):
    justPrint('     ')
    mock_print.assert_called_once_with('     ')


# edge case - justPrint - Test that the function prints a string with a single character.
def test_print_single_character(mock_print):
    justPrint('A')
    mock_print.assert_called_once_with('A')


# edge case - justPrint - Test that the function prints a string with Unicode characters.
def test_print_unicode_string(mock_print):
    justPrint('こんにちは世界')
    mock_print.assert_called_once_with('こんにちは世界')


# edge case - justPrint - Test that the function prints a None value as a string representation of None.
def test_print_none_value(mock_print):
    justPrint(str(None))
    mock_print.assert_called_once_with('None')


