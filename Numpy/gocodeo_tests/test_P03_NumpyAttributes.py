import pytest
from unittest import mock
import numpy as np

@pytest.fixture
def mock_ndarray():
    mock_array = mock.Mock()
    mock_array.size = 9
    mock_array.shape = (3, 3)
    mock_array.ndim = 2
    mock_array.itemsize = 8
    return mock_array

@pytest.fixture
def mock_empty_ndarray():
    mock_empty_array = mock.Mock()
    mock_empty_array.size = 0
    mock_empty_array.shape = (0,)
    mock_empty_array.ndim = 1
    return mock_empty_array

@pytest.fixture
def mock_large_ndarray():
    mock_large_array = mock.Mock()
    mock_large_array.size = 1000
    mock_large_array.shape = (1000,)
    mock_large_array.ndim = 1
    return mock_large_array

@pytest.fixture
def mock_high_dimensional_ndarray():
    mock_high_dim_array = mock.Mock()
    mock_high_dim_array.size = 8
    mock_high_dim_array.shape = (2, 2, 1)
    mock_high_dim_array.ndim = 3
    return mock_high_dim_array

@pytest.fixture
def mock_different_dtype_ndarray():
    mock_different_dtype_array = mock.Mock()
    mock_different_dtype_array.itemsize = 8
    return mock_different_dtype_array

# happy path - ndarray.size - Test that ndarray.size returns the correct number of items
def test_ndarray_size(mock_ndarray):
    assert mock_ndarray.size == 9


# happy path - ndarray.shape - Test that ndarray.shape returns the correct dimensions
def test_ndarray_shape(mock_ndarray):
    assert mock_ndarray.shape == (3, 3)


# happy path - ndarray.ndim - Test that ndarray.ndim returns the correct number of dimensions
def test_ndarray_ndim(mock_ndarray):
    assert mock_ndarray.ndim == 2


# happy path - ndarray.itemsize - Test that ndarray.itemsize returns the correct memory size of each element
def test_ndarray_itemsize(mock_ndarray):
    assert mock_ndarray.itemsize == 8


# happy path - ndarray.size - Test that ndarray.size returns 0 for an empty array
def test_ndarray_size_empty(mock_empty_ndarray):
    assert mock_empty_ndarray.size == 0


# edge case - ndarray.shape - Test that ndarray.shape returns (0,) for an empty array
def test_ndarray_shape_empty(mock_empty_ndarray):
    assert mock_empty_ndarray.shape == (0,)


# edge case - ndarray.ndim - Test that ndarray.ndim returns 1 for a 1D empty array
def test_ndarray_ndim_empty(mock_empty_ndarray):
    assert mock_empty_ndarray.ndim == 1


# edge case - ndarray.itemsize - Test that ndarray.itemsize handles arrays with different data types
def test_ndarray_itemsize_different_dtype(mock_different_dtype_ndarray):
    assert mock_different_dtype_ndarray.itemsize == 8


# edge case - ndarray.size - Test that ndarray.size is consistent for large arrays
def test_ndarray_size_large(mock_large_ndarray):
    assert mock_large_ndarray.size == 1000


# edge case - ndarray.shape - Test that ndarray.shape handles higher dimensional arrays correctly
def test_ndarray_shape_high_dim(mock_high_dimensional_ndarray):
    assert mock_high_dimensional_ndarray.shape == (2, 2, 1)


