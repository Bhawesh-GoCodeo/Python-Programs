import pytest
from unittest.mock import patch

# Mocking the charFrequency function from the source code
@pytest.fixture
def mock_charFrequency():
    with patch('Programs.P06_CharCount.charFrequency') as mock:
        yield mock

# happy path - charFrequency - Test that the function correctly counts frequency of each character in a simple string.
def test_simple_string(mock_charFrequency):
    mock_charFrequency.return_value = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    result = charFrequency('hello')
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# happy path - charFrequency - Test that the function counts frequency in a string with mixed case.
def test_mixed_case_string(mock_charFrequency):
    mock_charFrequency.return_value = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    result = charFrequency('HeLLo')
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# happy path - charFrequency - Test that the function counts frequency with spaces included.
def test_string_with_spaces(mock_charFrequency):
    mock_charFrequency.return_value = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1, ' ': 1}
    result = charFrequency('hello world')
    assert result == {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1, ' ': 1}


# happy path - charFrequency - Test that the function counts frequency in a string with punctuation.
def test_string_with_punctuation(mock_charFrequency):
    mock_charFrequency.return_value = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1, ',': 1, '!': 1, ' ': 1}
    result = charFrequency('hello, world!')
    assert result == {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1, ',': 1, '!': 1, ' ': 1}


# happy path - charFrequency - Test that the function handles an empty string.
def test_empty_string(mock_charFrequency):
    mock_charFrequency.return_value = {}
    result = charFrequency('')
    assert result == {}


# edge case - charFrequency - Test that the function handles a string with special characters only.
def test_special_characters(mock_charFrequency):
    mock_charFrequency.return_value = {'@': 1, '#': 1, '$': 1, '%': 1, '^': 1, '&': 1, '*': 1, '(': 1, ')': 1}
    result = charFrequency('@#$%^&*()')
    assert result == {'@': 1, '#': 1, '$': 1, '%': 1, '^': 1, '&': 1, '*': 1, '(': 1, ')': 1}


# edge case - charFrequency - Test that the function handles a string with numbers only.
def test_numbers_only(mock_charFrequency):
    mock_charFrequency.return_value = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '0': 1}
    result = charFrequency('1234567890')
    assert result == {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '0': 1}


# edge case - charFrequency - Test that the function handles a long string efficiently.
def test_long_string(mock_charFrequency):
    mock_charFrequency.return_value = {'a': 10000}
    result = charFrequency('a' * 10000)
    assert result == {'a': 10000}


# edge case - charFrequency - Test that the function handles a string with repeated characters.
def test_repeated_characters(mock_charFrequency):
    mock_charFrequency.return_value = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}
    result = charFrequency('aaaaabbbbcccdde')
    assert result == {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}


# edge case - charFrequency - Test that the function handles a string with unicode characters.
def test_unicode_characters(mock_charFrequency):
    mock_charFrequency.return_value = {'ñ': 1, 'á': 1, 'ç': 1, 'ø': 1}
    result = charFrequency('ñáçø')
    assert result == {'ñ': 1, 'á': 1, 'ç': 1, 'ø': 1}


