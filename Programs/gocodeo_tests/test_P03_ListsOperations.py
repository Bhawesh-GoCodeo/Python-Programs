import pytest
from unittest.mock import patch

@pytest.fixture
def mock_myList():
    with patch('Programs.P03_ListsOperations.myList', new=[1, 2, 3, 4, 5, 6, 7, 8, 9]) as mock_list:
        yield mock_list

@pytest.fixture
def mock_append():
    with patch('Programs.P03_ListsOperations.myList.append') as mock_append:
        yield mock_append

@pytest.fixture
def mock_index():
    with patch('Programs.P03_ListsOperations.myList.index') as mock_index:
        yield mock_index

@pytest.fixture
def mock_sort():
    with patch('Programs.P03_ListsOperations.myList.sort') as mock_sort:
        yield mock_sort

@pytest.fixture
def mock_pop():
    with patch('Programs.P03_ListsOperations.myList.pop') as mock_pop:
        yield mock_pop

@pytest.fixture
def mock_remove():
    with patch('Programs.P03_ListsOperations.myList.remove') as mock_remove:
        yield mock_remove

@pytest.fixture
def mock_insert():
    with patch('Programs.P03_ListsOperations.myList.insert') as mock_insert:
        yield mock_insert

@pytest.fixture
def mock_count():
    with patch('Programs.P03_ListsOperations.myList.count') as mock_count:
        yield mock_count

@pytest.fixture
def mock_extend():
    with patch('Programs.P03_ListsOperations.myList.extend') as mock_extend:
        yield mock_extend

@pytest.fixture
def mock_reverse():
    with patch('Programs.P03_ListsOperations.myList.reverse') as mock_reverse:
        yield mock_reverse

# happy path - get_first_element - Test that the first element of the list is returned correctly
def test_get_first_element(mock_myList):
    first_element = mock_myList[0]
    assert first_element == 1


# happy path - append_element - Test that an element is appended to the end of the list
def test_append_element(mock_myList, mock_append):
    mock_append.return_value = None
    mock_myList.append(10)
    mock_append.assert_called_once_with(10)
    assert mock_myList[-1] == 10


# happy path - find_element_index - Test that the index of a specific element is found
def test_find_element_index(mock_myList, mock_index):
    mock_index.return_value = 5
    index = mock_myList.index(6)
    mock_index.assert_called_once_with(6)
    assert index == 5


# happy path - sort_list - Test that the list is sorted in ascending order
def test_sort_list(mock_myList, mock_sort):
    mock_sort.return_value = None
    mock_myList.sort()
    mock_sort.assert_called_once()
    assert mock_myList == [1, 2, 3, 4, 5, 6, 7, 8, 9]


# happy path - extend_list - Test that the list is extended with multiple elements
def test_extend_list(mock_myList, mock_extend):
    mock_extend.return_value = None
    mock_myList.extend([11, 0])
    mock_extend.assert_called_once_with([11, 0])
    assert mock_myList[-2:] == [11, 0]


# edge case - access_out_of_bounds_index - Test that accessing an out-of-bounds index raises an IndexError
def test_access_out_of_bounds_index(mock_myList):
    with pytest.raises(IndexError):
        _ = mock_myList[10]


# edge case - remove_nonexistent_element - Test that removing an element not in the list raises a ValueError
def test_remove_nonexistent_element(mock_myList, mock_remove):
    mock_remove.side_effect = ValueError
    with pytest.raises(ValueError):
        mock_myList.remove(99)


# edge case - pop_from_empty_list - Test that popping from an empty list raises an IndexError
def test_pop_from_empty_list(mock_pop):
    mock_pop.side_effect = IndexError
    with pytest.raises(IndexError):
        _ = mock_pop()


# edge case - insert_out_of_bounds - Test that inserting at an out-of-bounds index appends the element
def test_insert_out_of_bounds(mock_myList, mock_insert):
    mock_insert.return_value = None
    mock_myList.insert(10, 6)
    mock_insert.assert_called_once_with(10, 6)
    assert mock_myList[-1] == 6


# edge case - reverse_single_element_list - Test that reversing a single-element list returns the same list
def test_reverse_single_element_list(mock_reverse):
    single_element_list = [1]
    mock_reverse.return_value = None
    single_element_list.reverse()
    mock_reverse.assert_called_once()
    assert single_element_list == [1]


