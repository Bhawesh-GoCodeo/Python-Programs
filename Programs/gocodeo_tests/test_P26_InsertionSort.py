import pytest
from unittest import mock
from Programs.P26_InsertionSort import insertionSort

@pytest.fixture
def mock_insertion_sort():
    with mock.patch('Programs.P26_InsertionSort.insertionSort', wraps=insertionSort) as mock_sort:
        yield mock_sort

# happy path - insertionSort - Test that insertionSort correctly sorts an unsorted list of integers.
def test_insertion_sort_unsorted_list(mock_insertion_sort):
    unsorted_list = [3, 4, 2, 6, 5, 7, 1, 9]
    expected_result = [1, 2, 3, 4, 5, 6, 7, 9]
    result = insertionSort(unsorted_list)
    assert result == expected_result
    mock_insertion_sort.assert_called_once_with(unsorted_list)


# happy path - insertionSort - Test that insertionSort correctly sorts an already sorted list of integers.
def test_insertion_sort_sorted_list(mock_insertion_sort):
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = insertionSort(sorted_list)
    assert result == expected_result
    mock_insertion_sort.assert_called_once_with(sorted_list)


# happy path - insertionSort - Test that insertionSort correctly sorts a list with repeated elements.
def test_insertion_sort_repeated_elements(mock_insertion_sort):
    list_with_repeats = [3, 1, 2, 3, 3, 2, 1]
    expected_result = [1, 1, 2, 2, 3, 3, 3]
    result = insertionSort(list_with_repeats)
    assert result == expected_result
    mock_insertion_sort.assert_called_once_with(list_with_repeats)


# happy path - insertionSort - Test that insertionSort correctly sorts a list with a single element.
def test_insertion_sort_single_element(mock_insertion_sort):
    single_element_list = [5]
    expected_result = [5]
    result = insertionSort(single_element_list)
    assert result == expected_result
    mock_insertion_sort.assert_called_once_with(single_element_list)


# happy path - insertionSort - Test that insertionSort correctly sorts a list with two elements.
def test_insertion_sort_two_elements(mock_insertion_sort):
    two_element_list = [2, 1]
    expected_result = [1, 2]
    result = insertionSort(two_element_list)
    assert result == expected_result
    mock_insertion_sort.assert_called_once_with(two_element_list)


# edge case - insertionSort - Test that insertionSort returns an empty list when given an empty list.
def test_insertion_sort_empty_list(mock_insertion_sort):
    empty_list = []
    expected_result = []
    result = insertionSort(empty_list)
    assert result == expected_result
    mock_insertion_sort.assert_called_once_with(empty_list)


# edge case - insertionSort - Test that insertionSort correctly sorts a list with negative numbers.
def test_insertion_sort_negative_numbers(mock_insertion_sort):
    negative_numbers = [-3, -1, -2, -5, -4]
    expected_result = [-5, -4, -3, -2, -1]
    result = insertionSort(negative_numbers)
    assert result == expected_result
    mock_insertion_sort.assert_called_once_with(negative_numbers)


# edge case - insertionSort - Test that insertionSort correctly sorts a list with both negative and positive numbers.
def test_insertion_sort_mixed_numbers(mock_insertion_sort):
    mixed_numbers = [-1, 3, -2, 5, 0]
    expected_result = [-2, -1, 0, 3, 5]
    result = insertionSort(mixed_numbers)
    assert result == expected_result
    mock_insertion_sort.assert_called_once_with(mixed_numbers)


# edge case - insertionSort - Test that insertionSort correctly handles a list with all elements the same.
def test_insertion_sort_identical_elements(mock_insertion_sort):
    identical_elements = [7, 7, 7, 7, 7]
    expected_result = [7, 7, 7, 7, 7]
    result = insertionSort(identical_elements)
    assert result == expected_result
    mock_insertion_sort.assert_called_once_with(identical_elements)


# edge case - insertionSort - Test that insertionSort correctly sorts a list with floating point numbers.
def test_insertion_sort_floating_numbers(mock_insertion_sort):
    floating_numbers = [3.1, 2.4, 1.5, 4.2]
    expected_result = [1.5, 2.4, 3.1, 4.2]
    result = insertionSort(floating_numbers)
    assert result == expected_result
    mock_insertion_sort.assert_called_once_with(floating_numbers)


