import pytest
from unittest import mock
import numpy as np

@pytest.fixture
def mock_np_arange():
    with mock.patch('numpy.arange', return_value=np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) as mock_arange:
        yield mock_arange

@pytest.fixture
def mock_np_array():
    with mock.patch('numpy.array') as mock_array:
        mock_array.side_effect = lambda array, dtype=None: np.array(array, dtype=dtype)
        yield mock_array

@pytest.fixture
def mock_np_float32():
    with mock.patch('numpy.float32', return_value=np.float32) as mock_float32:
        yield mock_float32

@pytest.fixture
def mock_np_complex64():
    with mock.patch('numpy.complex64', return_value=np.complex64) as mock_complex64:
        yield mock_complex64

@pytest.fixture
def mock_np_int32():
    with mock.patch('numpy.int32', return_value=np.int32) as mock_int32:
        yield mock_int32

@pytest.fixture
def mock_np_uint8():
    with mock.patch('numpy.uint8', return_value=np.uint8) as mock_uint8:
        yield mock_uint8

@pytest.fixture
def mock_np_float16():
    with mock.patch('numpy.float16', return_value=np.float16) as mock_float16:
        yield mock_float16

# happy path - np.arange - Test that np.arange creates an array of integers from 0 to 9
def test_np_arange_integers(mock_np_arange):
    result = np.arange(0, 10)
    assert result.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# happy path - np.array - Test that np.array converts integer array to float32
def test_np_array_float32_conversion(mock_np_array, mock_np_float32):
    result = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.float32)
    assert result.tolist() == [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]


# happy path - np.array - Test that np.array converts float32 array to complex64
def test_np_array_complex64_conversion(mock_np_array, mock_np_complex64):
    result = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0], dtype=np.complex64)
    expected_result = [complex(x, 0.0) for x in range(10)]
    assert result.tolist() == expected_result


# happy path - np.array - Test that np.array with dtype int32 maintains integer values
def test_np_array_int32_maintain_integers(mock_np_array, mock_np_int32):
    result = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.int32)
    assert result.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# happy path - np.arange - Test that np.arange with float type results in float array
def test_np_arange_float_type(mock_np_arange):
    result = np.arange(0.0, 10.0, dtype=np.float32)
    assert result.tolist() == [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]


# edge case - np.array - Test that np.array with empty list returns empty array
def test_np_array_empty_list(mock_np_array, mock_np_float32):
    result = np.array([], dtype=np.float32)
    assert result.tolist() == []


# edge case - np.arange - Test that np.arange with negative start and stop returns empty array
def test_np_arange_negative_start_stop(mock_np_arange):
    result = np.arange(-10, -10)
    assert result.tolist() == []


# edge case - np.array - Test that np.array with dtype uint8 handles overflow correctly
def test_np_array_uint8_overflow(mock_np_array, mock_np_uint8):
    result = np.array([256, 257], dtype=np.uint8)
    assert result.tolist() == [0, 1]


# edge case - np.array - Test that np.array with dtype int8 handles negative overflow correctly
def test_np_array_int8_negative_overflow(mock_np_array):
    result = np.array([-129, -130], dtype=np.int8)
    assert result.tolist() == [127, 126]


# edge case - np.array - Test that np.array with dtype float16 rounds correctly
def test_np_array_float16_rounding(mock_np_array, mock_np_float16):
    result = np.array([1.2345, 6.789], dtype=np.float16)
    assert result.tolist() == [1.234, 6.789]


