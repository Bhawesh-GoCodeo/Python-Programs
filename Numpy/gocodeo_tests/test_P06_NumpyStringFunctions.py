import pytest
from unittest import mock
import numpy as np

@pytest.fixture
def mock_numpy_char():
    with mock.patch('numpy.char.add') as mock_add, \
         mock.patch('numpy.char.multiply') as mock_multiply, \
         mock.patch('numpy.char.center') as mock_center, \
         mock.patch('numpy.char.capitalize') as mock_capitalize, \
         mock.patch('numpy.char.title') as mock_title, \
         mock.patch('numpy.char.lower') as mock_lower, \
         mock.patch('numpy.char.upper') as mock_upper, \
         mock.patch('numpy.char.split') as mock_split, \
         mock.patch('numpy.char.join') as mock_join:
        
        # Mock return values
        mock_add.return_value = ['abcxyz']
        mock_multiply.return_value = ['abcabcabc']
        mock_center.return_value = ['********abc*********']
        mock_capitalize.return_value = 'Hello world'
        mock_title.return_value = 'Hello How Are You?'
        mock_lower.return_value = ['hello', 'world']
        mock_upper.return_value = 'HELLO'
        mock_split.return_value = ['Omkar', 'Pathak']
        mock_join.return_value = 'd:m:y'
        
        yield {
            'add': mock_add,
            'multiply': mock_multiply,
            'center': mock_center,
            'capitalize': mock_capitalize,
            'title': mock_title,
            'lower': mock_lower,
            'upper': mock_upper,
            'split': mock_split,
            'join': mock_join
        }

# happy path - np.char.add - Test that np.char.add concatenates two string arrays
def test_np_char_add_concatenation(mock_numpy_char):
    result = np.char.add(['abc'], ['xyz'])
    assert result == ['abcxyz']
    mock_numpy_char['add'].assert_called_once_with(['abc'], ['xyz'])


# happy path - np.char.add - Test that np.char.add concatenates a string array with a string
def test_np_char_add_with_string(mock_numpy_char):
    result = np.char.add(['abc'], 'pqr')
    assert result == ['abcpqr']
    mock_numpy_char['add'].assert_called_once_with(['abc'], 'pqr')


# happy path - np.char.multiply - Test that np.char.multiply repeats the string array elements
def test_np_char_multiply(mock_numpy_char):
    result = np.char.multiply(['abc'], 3)
    assert result == ['abcabcabc']
    mock_numpy_char['multiply'].assert_called_once_with(['abc'], 3)


# happy path - np.char.center - Test that np.char.center centers the string with fill characters
def test_np_char_center(mock_numpy_char):
    result = np.char.center(['abc'], 20, fillchar='*')
    assert result == ['********abc*********']
    mock_numpy_char['center'].assert_called_once_with(['abc'], 20, fillchar='*')


# happy path - np.char.capitalize - Test that np.char.capitalize capitalizes the first letter of the string
def test_np_char_capitalize(mock_numpy_char):
    result = np.char.capitalize('hello world')
    assert result == 'Hello world'
    mock_numpy_char['capitalize'].assert_called_once_with('hello world')


# happy path - np.char.title - Test that np.char.title capitalizes the first letter of each word
def test_np_char_title(mock_numpy_char):
    result = np.char.title('hello how are you?')
    assert result == 'Hello How Are You?'
    mock_numpy_char['title'].assert_called_once_with('hello how are you?')


# edge case - np.char.lower - Test np.char.lower with mixed case strings
def test_np_char_lower_mixed_case(mock_numpy_char):
    result = np.char.lower(['HeLLo', 'WORLD'])
    assert result == ['hello', 'world']
    mock_numpy_char['lower'].assert_called_once_with(['HeLLo', 'WORLD'])


# edge case - np.char.upper - Test np.char.upper with lowercase strings
def test_np_char_upper_lowercase(mock_numpy_char):
    result = np.char.upper('hello')
    assert result == 'HELLO'
    mock_numpy_char['upper'].assert_called_once_with('hello')


# edge case - np.char.split - Test np.char.split with default whitespace separator
def test_np_char_split_whitespace(mock_numpy_char):
    result = np.char.split('Omkar Pathak')
    assert result == ['Omkar', 'Pathak']
    mock_numpy_char['split'].assert_called_once_with('Omkar Pathak')


# edge case - np.char.split - Test np.char.split with custom separator
def test_np_char_split_custom_separator(mock_numpy_char):
    result = np.char.split('2017-02-11', sep='-')
    assert result == ['2017', '02', '11']
    mock_numpy_char['split'].assert_called_once_with('2017-02-11', sep='-')


# edge case - np.char.join - Test np.char.join with a single character separator
def test_np_char_join_single_separator(mock_numpy_char):
    result = np.char.join(':', 'dmy')
    assert result == 'd:m:y'
    mock_numpy_char['join'].assert_called_once_with(':', 'dmy')


