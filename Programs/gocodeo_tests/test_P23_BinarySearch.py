import pytest
from unittest import mock
from Programs.P23_BinarySearch import binarySearch

@pytest.fixture
def mock_binary_search():
    with mock.patch('Programs.P23_BinarySearch.binarySearch') as mock_search:
        yield mock_search

# happy path - binarySearch - Test that target is found at the beginning of the list
def test_target_at_beginning(mock_binary_search):
    mock_binary_search.return_value = 0
    result = binarySearch(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14])
    assert result == 0
    mock_binary_search.assert_called_once_with(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14])


# happy path - binarySearch - Test that target is found at the end of the list
def test_target_at_end(mock_binary_search):
    mock_binary_search.return_value = 12
    result = binarySearch(14, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14])
    assert result == 12
    mock_binary_search.assert_called_once_with(14, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14])


# happy path - binarySearch - Test that target is found in the middle of the list
def test_target_in_middle(mock_binary_search):
    mock_binary_search.return_value = 6
    result = binarySearch(7, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14])
    assert result == 6
    mock_binary_search.assert_called_once_with(7, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14])


# happy path - binarySearch - Test that target is found in a list with two elements
def test_target_in_two_element_list(mock_binary_search):
    mock_binary_search.return_value = 1
    result = binarySearch(2, [1, 2])
    assert result == 1
    mock_binary_search.assert_called_once_with(2, [1, 2])


# happy path - binarySearch - Test that target is found in a list with repeated elements
def test_target_in_repeated_elements(mock_binary_search):
    mock_binary_search.return_value = 2
    result = binarySearch(3, [1, 2, 3, 3, 3, 4, 5])
    assert result == 2
    mock_binary_search.assert_called_once_with(3, [1, 2, 3, 3, 3, 4, 5])


# edge case - binarySearch - Test that target is not found in an empty list
def test_target_in_empty_list(mock_binary_search):
    mock_binary_search.return_value = -1
    result = binarySearch(5, [])
    assert result == -1
    mock_binary_search.assert_called_once_with(5, [])


# edge case - binarySearch - Test that target is not found when it is less than all elements
def test_target_less_than_all(mock_binary_search):
    mock_binary_search.return_value = -1
    result = binarySearch(0, [1, 2, 3, 4, 5])
    assert result == -1
    mock_binary_search.assert_called_once_with(0, [1, 2, 3, 4, 5])


# edge case - binarySearch - Test that target is not found when it is greater than all elements
def test_target_greater_than_all(mock_binary_search):
    mock_binary_search.return_value = -1
    result = binarySearch(10, [1, 2, 3, 4, 5])
    assert result == -1
    mock_binary_search.assert_called_once_with(10, [1, 2, 3, 4, 5])


# edge case - binarySearch - Test that target is not found in a list with one element not matching
def test_target_not_in_single_element_list(mock_binary_search):
    mock_binary_search.return_value = -1
    result = binarySearch(2, [1])
    assert result == -1
    mock_binary_search.assert_called_once_with(2, [1])


# edge case - binarySearch - Test that target is not found in a list with all elements the same but different from target
def test_target_not_in_uniform_list(mock_binary_search):
    mock_binary_search.return_value = -1
    result = binarySearch(5, [3, 3, 3, 3, 3])
    assert result == -1
    mock_binary_search.assert_called_once_with(5, [3, 3, 3, 3, 3])


