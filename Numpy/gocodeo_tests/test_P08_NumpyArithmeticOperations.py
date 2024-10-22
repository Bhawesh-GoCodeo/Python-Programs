import numpy as np
import pytest
from unittest import mock

@pytest.fixture
def mock_numpy_operations():
    with mock.patch('Numpy.P08_NumpyArithmeticOperations.np.arange') as mock_arange, \
         mock.patch('Numpy.P08_NumpyArithmeticOperations.np.add') as mock_add, \
         mock.patch('Numpy.P08_NumpyArithmeticOperations.np.subtract') as mock_subtract, \
         mock.patch('Numpy.P08_NumpyArithmeticOperations.np.multiply') as mock_multiply, \
         mock.patch('Numpy.P08_NumpyArithmeticOperations.np.divide') as mock_divide, \
         mock.patch('Numpy.P08_NumpyArithmeticOperations.np.power') as mock_power:
        
        # Mocking np.arange
        mock_arange.side_effect = lambda x: np.array(range(x))
        
        # Mocking np.add
        mock_add.side_effect = np.add
        
        # Mocking np.subtract
        mock_subtract.side_effect = np.subtract
        
        # Mocking np.multiply
        mock_multiply.side_effect = np.multiply
        
        # Mocking np.divide
        mock_divide.side_effect = np.divide
        
        # Mocking np.power
        mock_power.side_effect = np.power
        
        yield {
            'mock_arange': mock_arange,
            'mock_add': mock_add,
            'mock_subtract': mock_subtract,
            'mock_multiply': mock_multiply,
            'mock_divide': mock_divide,
            'mock_power': mock_power
        }

# happy path - np.add - Test that adding two arrays of compatible shapes returns correct result
def test_add_arrays(mock_numpy_operations):
    first_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
    second_array = np.array([0, 1, 2, 3])
    expected_result = np.array([[0, 2, 4, 6], [4, 6, 8, 10], [8, 10, 12, 14]])
    result = np.add(first_array, second_array)
    assert np.array_equal(result, expected_result)


# happy path - np.subtract - Test that subtracting two arrays of compatible shapes returns correct result
def test_subtract_arrays(mock_numpy_operations):
    first_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
    second_array = np.array([0, 1, 2, 3])
    expected_result = np.array([[0, 0, 0, 0], [4, 4, 4, 4], [8, 8, 8, 8]])
    result = np.subtract(first_array, second_array)
    assert np.array_equal(result, expected_result)


# happy path - np.multiply - Test that multiplying two arrays of compatible shapes returns correct result
def test_multiply_arrays(mock_numpy_operations):
    first_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
    second_array = np.array([0, 1, 2, 3])
    expected_result = np.array([[0, 1, 4, 9], [0, 5, 12, 21], [0, 9, 20, 33]])
    result = np.multiply(first_array, second_array)
    assert np.array_equal(result, expected_result)


# happy path - np.divide - Test that dividing two arrays of compatible shapes returns correct result
def test_divide_arrays(mock_numpy_operations):
    first_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
    second_array = np.array([1, 1, 1, 1])
    expected_result = np.array([[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0], [8.0, 9.0, 10.0, 11.0]])
    result = np.divide(first_array, second_array)
    assert np.array_equal(result, expected_result)


# happy path - np.power - Test that raising array elements to a power returns correct result
def test_power_array(mock_numpy_operations):
    array = np.array([1, 2, 3])
    power = 2
    expected_result = np.array([1, 4, 9])
    result = np.power(array, power)
    assert np.array_equal(result, expected_result)


# edge case - np.add - Test that adding arrays with incompatible shapes raises an error
def test_add_incompatible_arrays(mock_numpy_operations):
    first_array = np.array([[0, 1, 2]])
    second_array = np.array([0, 1, 2, 3])
    with pytest.raises(ValueError):
        np.add(first_array, second_array)


# edge case - np.subtract - Test that subtracting arrays with incompatible shapes raises an error
def test_subtract_incompatible_arrays(mock_numpy_operations):
    first_array = np.array([[0, 1, 2]])
    second_array = np.array([0, 1, 2, 3])
    with pytest.raises(ValueError):
        np.subtract(first_array, second_array)


# edge case - np.multiply - Test that multiplying arrays with incompatible shapes raises an error
def test_multiply_incompatible_arrays(mock_numpy_operations):
    first_array = np.array([[0, 1, 2]])
    second_array = np.array([0, 1, 2, 3])
    with pytest.raises(ValueError):
        np.multiply(first_array, second_array)


# edge case - np.divide - Test that dividing by zero raises an error
def test_divide_by_zero(mock_numpy_operations):
    first_array = np.array([[0, 1, 2, 3]])
    second_array = np.array([0, 0, 0, 0])
    with pytest.raises(ZeroDivisionError):
        np.divide(first_array, second_array)


# edge case - np.power - Test that power function with negative exponent raises an error
def test_power_negative_exponent(mock_numpy_operations):
    array = np.array([1, 2, 3])
    power = -1
    with pytest.raises(ValueError):
        np.power(array, power)


