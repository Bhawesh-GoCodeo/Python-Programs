import pytest
import numpy as np
from unittest import mock

@pytest.fixture
def mock_numpy_functions():
    with mock.patch('numpy.arange') as mock_arange, \
         mock.patch('numpy.reshape') as mock_reshape, \
         mock.patch('numpy.ndarray.flat', new_callable=mock.PropertyMock) as mock_flat, \
         mock.patch('numpy.ndarray.flatten') as mock_flatten, \
         mock.patch('numpy.transpose') as mock_transpose, \
         mock.patch('numpy.swapaxes') as mock_swapaxes, \
         mock.patch('numpy.rollaxis') as mock_rollaxis, \
         mock.patch('numpy.resize') as mock_resize, \
         mock.patch('numpy.append') as mock_append:
        
        # Mock behaviors
        mock_arange.return_value = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])
        mock_reshape.return_value = np.array([[0, 2, 4], [6, 8, 10], [12, 14, 16], [18, 20, 22], [24, 26, 28]])
        mock_flat.side_effect = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]).flat
        mock_flatten.return_value = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])
        mock_transpose.return_value = np.array([[0, 6, 12, 18, 24], [2, 8, 14, 20, 26], [4, 10, 16, 22, 28]])
        mock_swapaxes.return_value = np.array([[[0, 4], [2, 6]], [[1, 5], [3, 7]]])
        mock_rollaxis.return_value = np.array([[[0, 2], [4, 6]], [[1, 3], [5, 7]]])
        mock_resize.return_value = np.array([[1, 2], [3, 4], [5, 6]])
        mock_append.return_value = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        
        yield {
            'mock_arange': mock_arange,
            'mock_reshape': mock_reshape,
            'mock_flat': mock_flat,
            'mock_flatten': mock_flatten,
            'mock_transpose': mock_transpose,
            'mock_swapaxes': mock_swapaxes,
            'mock_rollaxis': mock_rollaxis,
            'mock_resize': mock_resize,
            'mock_append': mock_append
        }

# happy path - reshape - Test that numpy.reshape reshapes an array to a specified shape
def test_reshape_to_5x3(mock_numpy_functions):
    mock_reshape = mock_numpy_functions['mock_reshape']
    array_to_reshape = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])
    new_shape = (5, 3)
    reshaped_array = array_to_reshape.reshape(new_shape)
    np.testing.assert_array_equal(reshaped_array, mock_reshape.return_value)
    mock_reshape.assert_called_once_with(array_to_reshape, new_shape)


# happy path - flat - Test that numpy.ndarray.flat returns the correct element at a specified flat index
def test_flat_index_5(mock_numpy_functions):
    mock_flat = mock_numpy_functions['mock_flat']
    array = np.arange(0, 30, 2)
    index = 5
    element = array.flat[index]
    assert element == mock_flat.return_value[index]
    assert element == 10


# happy path - flatten - Test that numpy.ndarray.flatten converts a reshaped array back to 1-D
def test_flatten_reshaped_array(mock_numpy_functions):
    mock_flatten = mock_numpy_functions['mock_flatten']
    array = np.array([[0, 2, 4], [6, 8, 10], [12, 14, 16], [18, 20, 22], [24, 26, 28]])
    flattened_array = array.flatten()
    np.testing.assert_array_equal(flattened_array, mock_flatten.return_value)
    mock_flatten.assert_called_once()


# happy path - transpose - Test that numpy.transpose transposes a 2-D array correctly
def test_transpose_2d_array(mock_numpy_functions):
    mock_transpose = mock_numpy_functions['mock_transpose']
    array = np.array([[0, 2, 4], [6, 8, 10], [12, 14, 16], [18, 20, 22], [24, 26, 28]])
    transposed_array = array.transpose()
    np.testing.assert_array_equal(transposed_array, mock_transpose.return_value)
    mock_transpose.assert_called_once()


# happy path - swapaxes - Test that numpy.swapaxes swaps two axes of a 3-D array
def test_swapaxes_3d_array(mock_numpy_functions):
    mock_swapaxes = mock_numpy_functions['mock_swapaxes']
    array = np.arange(8).reshape(2, 2, 2)
    swapped_array = np.swapaxes(array, 2, 0)
    np.testing.assert_array_equal(swapped_array, mock_swapaxes.return_value)
    mock_swapaxes.assert_called_once_with(array, 2, 0)


# happy path - rollaxis - Test that numpy.rollaxis rolls the specified axis backwards
def test_rollaxis_3d_array(mock_numpy_functions):
    mock_rollaxis = mock_numpy_functions['mock_rollaxis']
    array = np.arange(8).reshape(2, 2, 2)
    rolled_array = np.rollaxis(array, 2)
    np.testing.assert_array_equal(rolled_array, mock_rollaxis.return_value)
    mock_rollaxis.assert_called_once_with(array, 2)


# happy path - resize - Test that numpy.resize resizes an array to a specified shape
def test_resize_array_to_3x2(mock_numpy_functions):
    mock_resize = mock_numpy_functions['mock_resize']
    array = np.array([[1, 2, 3], [4, 5, 6]])
    resized_array = np.resize(array, (3, 2))
    np.testing.assert_array_equal(resized_array, mock_resize.return_value)
    mock_resize.assert_called_once_with(array, (3, 2))


# happy path - append - Test that numpy.append appends elements to an array
def test_append_elements_to_array(mock_numpy_functions):
    mock_append = mock_numpy_functions['mock_append']
    array = np.array([[1, 2, 3], [4, 5, 6]])
    appended_array = np.append(array, [7, 8, 9])
    np.testing.assert_array_equal(appended_array, mock_append.return_value)
    mock_append.assert_called_once_with(array, [7, 8, 9])


# edge case - reshape - Test that numpy.reshape raises an error when reshaping to an incompatible shape
def test_reshape_incompatible_shape(mock_numpy_functions):
    mock_reshape = mock_numpy_functions['mock_reshape']
    array_to_reshape = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])
    new_shape = (4, 4)
    with pytest.raises(ValueError):
        array_to_reshape.reshape(new_shape)
    mock_reshape.assert_called_once_with(array_to_reshape, new_shape)


# edge case - flat - Test that numpy.ndarray.flat raises an error for out-of-bound index
def test_flat_out_of_bound_index(mock_numpy_functions):
    mock_flat = mock_numpy_functions['mock_flat']
    array = np.arange(0, 30, 2)
    index = 20
    with pytest.raises(IndexError):
        _ = array.flat[index]
    mock_flat.assert_called_once()


# edge case - flatten - Test that numpy.ndarray.flatten works on already flat arrays
def test_flatten_already_flat_array(mock_numpy_functions):
    mock_flatten = mock_numpy_functions['mock_flatten']
    array = np.arange(0, 30, 2)
    flattened_array = array.flatten()
    np.testing.assert_array_equal(flattened_array, mock_flatten.return_value)
    mock_flatten.assert_called_once()


# edge case - swapaxes - Test that numpy.swapaxes raises an error for invalid axis numbers
def test_swapaxes_invalid_axis(mock_numpy_functions):
    mock_swapaxes = mock_numpy_functions['mock_swapaxes']
    array = np.arange(8).reshape(2, 2, 2)
    with pytest.raises(np.AxisError):
        np.swapaxes(array, 3, 0)
    mock_swapaxes.assert_not_called()


# edge case - rollaxis - Test that numpy.rollaxis raises an error for invalid axis numbers
def test_rollaxis_invalid_axis(mock_numpy_functions):
    mock_rollaxis = mock_numpy_functions['mock_rollaxis']
    array = np.arange(8).reshape(2, 2, 2)
    with pytest.raises(np.AxisError):
        np.rollaxis(array, 3)
    mock_rollaxis.assert_not_called()


# edge case - resize - Test that numpy.resize works with zero dimensions
def test_resize_to_zero_dimensions(mock_numpy_functions):
    mock_resize = mock_numpy_functions['mock_resize']
    array = np.array([[1, 2, 3], [4, 5, 6]])
    resized_array = np.resize(array, (0, 2))
    np.testing.assert_array_equal(resized_array, np.array([]))
    mock_resize.assert_called_once_with(array, (0, 2))


