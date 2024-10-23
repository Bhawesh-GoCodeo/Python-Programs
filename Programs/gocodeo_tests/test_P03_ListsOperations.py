import pytest
from unittest.mock import patch

@pytest.fixture
def mock_list_operations():
    with patch('Programs.P03_ListsOperations.myList', return_value=[1, 2, 3, 4, 5, 6, 7, 8, 9]) as mock_list:
        yield mock_list

    with patch('Programs.P03_ListsOperations.myList.append') as mock_append:
        yield mock_append

    with patch('Programs.P03_ListsOperations.myList.index') as mock_index:
        yield mock_index

    with patch('Programs.P03_ListsOperations.myList.sort') as mock_sort:
        yield mock_sort

    with patch('Programs.P03_ListsOperations.myList.pop') as mock_pop:
        yield mock_pop

    with patch('Programs.P03_ListsOperations.myList.remove') as mock_remove:
        yield mock_remove

    with patch('Programs.P03_ListsOperations.myList.insert') as mock_insert:
        yield mock_insert

    with patch('Programs.P03_ListsOperations.myList.count') as mock_count:
        yield mock_count

    with patch('Programs.P03_ListsOperations.myList.extend') as mock_extend:
        yield mock_extend

    with patch('Programs.P03_ListsOperations.myList.reverse') as mock_reverse:
        yield mock_reverse

# happy path - print - Test that the first element of the list is accessed correctly
def test_first_element_access(mock_list_operations):
    mock_list = mock_list_operations
    assert mock_list[0] == 1


# happy path - append - Test that appending an element adds it to the end of the list
def test_append_element(mock_list_operations):
    mock_list = mock_list_operations
    mock_append = mock_list.append
    mock_append(10)
    assert mock_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# happy path - sort - Test that sorting the list rearranges elements in ascending order
def test_sort_list(mock_list_operations):
    mock_list = [3, 1, 2]
    mock_sort = mock_list_operations
    mock_sort.sort()
    assert mock_list == [1, 2, 3]


# happy path - pop - Test that popping an element removes and returns the last element
def test_pop_element(mock_list_operations):
    mock_list = [1, 2, 3, 4, 5]
    mock_pop = mock_list_operations
    popped_element = mock_pop.pop()
    assert popped_element == 5
    assert mock_list == [1, 2, 3, 4]


# happy path - insert - Test that inserting an element at a specified index adds it to that position
def test_insert_element(mock_list_operations):
    mock_list = [1, 2, 3, 4, 5]
    mock_insert = mock_list_operations
    mock_insert.insert(2, 6)
    assert mock_list == [1, 2, 6, 3, 4, 5]


# happy path - extend - Test that extending a list adds multiple elements at the end
def test_extend_list(mock_list_operations):
    mock_list = [1, 2, 3]
    mock_extend = mock_list_operations
    mock_extend.extend([4, 5])
    assert mock_list == [1, 2, 3, 4, 5]


# edge case - print - Test that accessing an index out of range raises an IndexError
def test_access_out_of_range(mock_list_operations):
    mock_list = [1, 2, 3]
    try:
        _ = mock_list[5]
        assert False, "Expected IndexError"
    except IndexError:
        assert True


# edge case - remove - Test that removing a non-existent element raises a ValueError
def test_remove_non_existent_element(mock_list_operations):
    mock_list = [1, 2, 3]
    mock_remove = mock_list_operations
    try:
        mock_remove.remove(4)
        assert False, "Expected ValueError"
    except ValueError:
        assert True


# edge case - pop - Test that popping from an empty list raises an IndexError
def test_pop_empty_list(mock_list_operations):
    mock_list = []
    mock_pop = mock_list_operations
    try:
        mock_pop.pop()
        assert False, "Expected IndexError"
    except IndexError:
        assert True


# edge case - insert - Test that inserting at a negative index places the element correctly
def test_insert_negative_index(mock_list_operations):
    mock_list = [1, 2, 3]
    mock_insert = mock_list_operations
    mock_insert.insert(-1, 4)
    assert mock_list == [1, 2, 4, 3]


# edge case - count - Test that counting an element not in the list returns zero
def test_count_non_existent_element(mock_list_operations):
    mock_list = [1, 2, 3]
    mock_count = mock_list_operations
    count = mock_count.count(4)
    assert count == 0


