import pytest
from unittest import mock
from Programs.P06_CharCount import charFrequency

@pytest.fixture
def mock_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'hello')

@pytest.fixture
def mock_lower():
    with mock.patch('Programs.P06_CharCount.str.lower', return_value='hello') as mock_lower:
        yield mock_lower

@pytest.fixture
def mock_dict():
    with mock.patch('Programs.P06_CharCount.dict', {}) as mock_dict:
        yield mock_dict

@pytest.fixture
def mock_keys():
    with mock.patch('Programs.P06_CharCount.dict.keys', return_value=mock.Mock()) as mock_keys:
        yield mock_keys

# happy path - charFrequency - Test that the function correctly calculates frequency for a simple string
def test_char_frequency_simple_string(mock_input, mock_lower, mock_dict, mock_keys):
    result = charFrequency('hello')
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# happy path - charFrequency - Test that the function correctly calculates frequency for a string with mixed case
def test_char_frequency_mixed_case(mock_input, mock_lower, mock_dict, mock_keys):
    result = charFrequency('HeLLo')
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# happy path - charFrequency - Test that the function correctly calculates frequency for a string with spaces
def test_char_frequency_with_spaces(mock_input, mock_lower, mock_dict, mock_keys):
    result = charFrequency('hello world')
    assert result == {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1, ' ': 1}


# happy path - charFrequency - Test that the function correctly calculates frequency for a string with numbers
def test_char_frequency_with_numbers(mock_input, mock_lower, mock_dict, mock_keys):
    result = charFrequency('hello123')
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1, '1': 1, '2': 1, '3': 1}


# happy path - charFrequency - Test that the function correctly calculates frequency for a string with special characters
def test_char_frequency_with_special_characters(mock_input, mock_lower, mock_dict, mock_keys):
    result = charFrequency('hello@world!')
    assert result == {'h': 1, 'e': 1, 'l': 3, 'o': 2, '@': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}


# edge case - charFrequency - Test that the function handles an empty string
def test_char_frequency_empty_string(mock_input, mock_lower, mock_dict, mock_keys):
    result = charFrequency('')
    assert result == {}


# edge case - charFrequency - Test that the function handles a string with all same characters
def test_char_frequency_all_same_characters(mock_input, mock_lower, mock_dict, mock_keys):
    result = charFrequency('aaaaa')
    assert result == {'a': 5}


# edge case - charFrequency - Test that the function handles a string with only spaces
def test_char_frequency_only_spaces(mock_input, mock_lower, mock_dict, mock_keys):
    result = charFrequency('     ')
    assert result == {' ': 5}


# edge case - charFrequency - Test that the function handles a string with non-ASCII characters
def test_char_frequency_non_ascii(mock_input, mock_lower, mock_dict, mock_keys):
    result = charFrequency('héllo')
    assert result == {'h': 1, 'é': 1, 'l': 2, 'o': 1}


# edge case - charFrequency - Test that the function handles a very long string
def test_char_frequency_long_string(mock_input, mock_lower, mock_dict, mock_keys):
    long_string = 'a' * 1000
    result = charFrequency(long_string)
    assert result == {'a': 1000}


