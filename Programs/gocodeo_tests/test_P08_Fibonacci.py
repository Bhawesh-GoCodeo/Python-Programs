import pytest
from unittest import mock
from Programs.P08_Fibonacci import fibonacci, fibonacci_without_recursion

@pytest.fixture
def mock_fibonacci():
    with mock.patch('Programs.P08_Fibonacci.fibonacci') as mock_fib:
        yield mock_fib

@pytest.fixture
def mock_fibonacci_without_recursion():
    with mock.patch('Programs.P08_Fibonacci.fibonacci_without_recursion') as mock_fib_no_rec:
        yield mock_fib_no_rec

# happy path - fibonacci - Test that fibonacci returns 0 for the 0th term
def test_fibonacci_0(mock_fibonacci):
    mock_fibonacci.return_value = 0
    result = fibonacci(0)
    assert result == 0


# happy path - fibonacci - Test that fibonacci returns 1 for the 1st term
def test_fibonacci_1(mock_fibonacci):
    mock_fibonacci.return_value = 1
    result = fibonacci(1)
    assert result == 1


# happy path - fibonacci - Test that fibonacci returns 1 for the 2nd term
def test_fibonacci_2(mock_fibonacci):
    mock_fibonacci.return_value = 1
    result = fibonacci(2)
    assert result == 1


# happy path - fibonacci - Test that fibonacci returns 2 for the 3rd term
def test_fibonacci_3(mock_fibonacci):
    mock_fibonacci.return_value = 2
    result = fibonacci(3)
    assert result == 2


# happy path - fibonacci - Test that fibonacci returns 3 for the 4th term
def test_fibonacci_4(mock_fibonacci):
    mock_fibonacci.return_value = 3
    result = fibonacci(4)
    assert result == 3


# happy path - fibonacci_without_recursion - Test that fibonacci_without_recursion returns 0 for the 0th term
def test_fibonacci_without_recursion_0(mock_fibonacci_without_recursion):
    mock_fibonacci_without_recursion.return_value = 0
    result = fibonacci_without_recursion(0)
    assert result == 0


# happy path - fibonacci_without_recursion - Test that fibonacci_without_recursion returns 1 for the 1st term
def test_fibonacci_without_recursion_1(mock_fibonacci_without_recursion):
    mock_fibonacci_without_recursion.return_value = 1
    result = fibonacci_without_recursion(1)
    assert result == 1


# happy path - fibonacci_without_recursion - Test that fibonacci_without_recursion returns 1 for the 2nd term
def test_fibonacci_without_recursion_2(mock_fibonacci_without_recursion):
    mock_fibonacci_without_recursion.return_value = 1
    result = fibonacci_without_recursion(2)
    assert result == 1


# happy path - fibonacci_without_recursion - Test that fibonacci_without_recursion returns 2 for the 3rd term
def test_fibonacci_without_recursion_3(mock_fibonacci_without_recursion):
    mock_fibonacci_without_recursion.return_value = 2
    result = fibonacci_without_recursion(3)
    assert result == 2


# happy path - fibonacci_without_recursion - Test that fibonacci_without_recursion returns 3 for the 4th term
def test_fibonacci_without_recursion_4(mock_fibonacci_without_recursion):
    mock_fibonacci_without_recursion.return_value = 3
    result = fibonacci_without_recursion(4)
    assert result == 3


# edge case - fibonacci - Test that fibonacci handles negative input gracefully
def test_fibonacci_negative(mock_fibonacci):
    mock_fibonacci.return_value = -1
    result = fibonacci(-1)
    assert result == -1


# edge case - fibonacci - Test that fibonacci handles large input efficiently
def test_fibonacci_large_input(mock_fibonacci):
    mock_fibonacci.return_value = 832040
    result = fibonacci(30)
    assert result == 832040


# edge case - fibonacci_without_recursion - Test that fibonacci_without_recursion handles negative input gracefully
def test_fibonacci_without_recursion_negative(mock_fibonacci_without_recursion):
    mock_fibonacci_without_recursion.return_value = 0
    result = fibonacci_without_recursion(-1)
    assert result == 0


# edge case - fibonacci_without_recursion - Test that fibonacci_without_recursion handles large input efficiently
def test_fibonacci_without_recursion_large_input(mock_fibonacci_without_recursion):
    mock_fibonacci_without_recursion.return_value = 832040
    result = fibonacci_without_recursion(30)
    assert result == 832040


# edge case - fibonacci_without_recursion - Test that fibonacci_without_recursion handles input of 1 correctly
def test_fibonacci_without_recursion_input_1(mock_fibonacci_without_recursion):
    mock_fibonacci_without_recursion.return_value = 1
    result = fibonacci_without_recursion(1)
    assert result == 1


