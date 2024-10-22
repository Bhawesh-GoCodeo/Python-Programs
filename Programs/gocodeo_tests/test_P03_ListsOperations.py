import pytest
from unittest import mock
from Programs.P03_ListsOperations import myList

@pytest.fixture
def mock_myList():
    with mock.patch('Programs.P03_ListsOperations.myList', new=myList) as mocked_list:
        yield mocked_list

@pytest.fixture
def mock_append():
    with mock.patch.object(myList, 'append', return_value=None) as mocked_append:
        yield mocked_append

@pytest.fixture
def mock_index():
    with mock.patch.object(myList, 'index', side_effect=lambda x: myList.index(x) if x in myList else ValueError) as mocked_index:
        yield mocked_index

@pytest.fixture
def mock_sort():
    with mock.patch.object(myList, 'sort', return_value=None) as mocked_sort:
        yield mocked_sort

@pytest.fixture
def mock_pop():
    with mock.patch.object(myList, 'pop', side_effect=lambda: myList.pop() if myList else IndexError) as mocked_pop:
        yield mocked_pop

@pytest.fixture
def mock_remove():
    with mock.patch.object(myList, 'remove', side_effect=lambda x: myList.remove(x) if x in myList else ValueError) as mocked_remove:
        yield mocked_remove

@pytest.fixture
def mock_insert():
    with mock.patch.object(myList, 'insert', return_value=None) as mocked_insert:
        yield mocked_insert

@pytest.fixture
def mock_count():
    with mock.patch.object(myList, 'count', side_effect=lambda x: myList.count(x)) as mocked_count:
        yield mocked_count

@pytest.fixture
def mock_extend():
    with mock.patch.object(myList, 'extend', return_value=None) as mocked_extend:
        yield mocked_extend

@pytest.fixture
def mock_reverse():
    with mock.patch.object(myList, 'reverse', return_value=None) as mocked_reverse:
        yield mocked_reverse

# happy path - print - Test that the first element of the list is correctly accessed
def test_first_element_access(mock_myList):
    assert mock_myList[0] == 1


# happy path - append - Test that an element is correctly appended to the list
def test_append_element(mock_myList, mock_append):
    mock_myList.append(10)
    mock_append.assert_called_once_with(10)
    assert mock_myList[-1] == 10


# happy path - index - Test that the index of a particular element is correctly found
def test_find_index(mock_myList, mock_index):
    index = mock_myList.index(6)
    mock_index.assert_called_once_with(6)
    assert index == 5


# happy path - sort - Test that a list is correctly sorted
def test_sort_list(mock_myList, mock_sort):
    mock_myList.sort()
    mock_sort.assert_called_once()
    assert mock_myList == [1, 2, 3, 4, 5, 6, 7, 8, 9]


# happy path - remove - Test that an element is correctly removed by name from the list
def test_remove_element(mock_myList, mock_remove):
    mock_myList.remove(6)
    mock_remove.assert_called_once_with(6)
    assert 6 not in mock_myList


# edge case - print - Test that accessing an element from an empty list raises an error
def test_access_element_empty_list(mock_myList):
    with pytest.raises(IndexError):
        _ = mock_myList[0]


# edge case - remove - Test that removing a non-existent element raises an error
def test_remove_non_existent_element(mock_myList, mock_remove):
    with pytest.raises(ValueError):
        mock_myList.remove(10)


# edge case - pop - Test that popping from an empty list raises an error
def test_pop_empty_list(mock_myList, mock_pop):
    mock_myList.clear()
    with pytest.raises(IndexError):
        mock_myList.pop()


# edge case - insert - Test that inserting an element at an index out of range raises an error
def test_insert_out_of_range(mock_myList, mock_insert):
    with pytest.raises(IndexError):
        mock_myList.insert(10, 4)


# edge case - count - Test that counting occurrences of an element not in the list returns zero
def test_count_non_existent_element(mock_myList, mock_count):
    count = mock_myList.count(6)
    mock_count.assert_called_once_with(6)
    assert count == 0


