import pytest
from unittest import mock
from Programs.P25_BubbleSort import bubbleSort

@pytest.fixture
def mock_bubble_sort():
    with mock.patch('Programs.P25_BubbleSort.bubbleSort') as mock_sort:
        yield mock_sort

# happy path - bubbleSort - Test that bubbleSort correctly sorts a list of integers in ascending order
def test_bubble_sort_sorted_list(mock_bubble_sort):
    mock_bubble_sort.return_value = [1, 2, 3, 4, 5, 6, 7, 9]
    result = bubbleSort([3, 4, 2, 6, 5, 7, 1, 9])
    assert result == [1, 2, 3, 4, 5, 6, 7, 9]


# happy path - bubbleSort - Test that bubbleSort correctly handles an already sorted list
def test_bubble_sort_already_sorted(mock_bubble_sort):
    mock_bubble_sort.return_value = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = bubbleSort([1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]


# happy path - bubbleSort - Test that bubbleSort correctly handles a list with duplicate elements
def test_bubble_sort_with_duplicates(mock_bubble_sort):
    mock_bubble_sort.return_value = [1, 1, 2, 3, 5, 5, 8, 8]
    result = bubbleSort([5, 3, 8, 5, 2, 8, 1, 1])
    assert result == [1, 1, 2, 3, 5, 5, 8, 8]


# happy path - bubbleSort - Test that bubbleSort correctly sorts a list with negative integers
def test_bubble_sort_with_negatives(mock_bubble_sort):
    mock_bubble_sort.return_value = [-2, -1, 0, 3, 5, 6]
    result = bubbleSort([-1, 3, -2, 6, 0, 5])
    assert result == [-2, -1, 0, 3, 5, 6]


# happy path - bubbleSort - Test that bubbleSort correctly handles a list with one element
def test_bubble_sort_single_element(mock_bubble_sort):
    mock_bubble_sort.return_value = [1]
    result = bubbleSort([1])
    assert result == [1]


# edge case - bubbleSort - Test that bubbleSort correctly handles an empty list
def test_bubble_sort_empty_list(mock_bubble_sort):
    mock_bubble_sort.return_value = []
    result = bubbleSort([])
    assert result == []


# edge case - bubbleSort - Test that bubbleSort correctly handles a list with all identical elements
def test_bubble_sort_identical_elements(mock_bubble_sort):
    mock_bubble_sort.return_value = [7, 7, 7, 7, 7]
    result = bubbleSort([7, 7, 7, 7, 7])
    assert result == [7, 7, 7, 7, 7]


# edge case - bubbleSort - Test that bubbleSort correctly handles a list with large numbers
def test_bubble_sort_large_numbers(mock_bubble_sort):
    mock_bubble_sort.return_value = [999999, 1000000, 1000001]
    result = bubbleSort([1000000, 999999, 1000001])
    assert result == [999999, 1000000, 1000001]


# edge case - bubbleSort - Test that bubbleSort correctly handles a list with negative and positive numbers
def test_bubble_sort_mixed_sign_numbers(mock_bubble_sort):
    mock_bubble_sort.return_value = [-10, -5, 0, 5, 10]
    result = bubbleSort([-10, 0, 10, -5, 5])
    assert result == [-10, -5, 0, 5, 10]


# edge case - bubbleSort - Test that bubbleSort correctly handles a list with a single negative number
def test_bubble_sort_single_negative(mock_bubble_sort):
    mock_bubble_sort.return_value = [-1]
    result = bubbleSort([-1])
    assert result == [-1]


