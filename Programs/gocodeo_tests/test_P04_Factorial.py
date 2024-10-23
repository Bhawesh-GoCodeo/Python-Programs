import pytest
from unittest import mock
from Programs.P04_Factorial import factorial

@pytest.fixture
def mock_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')  # Mocking user input

@pytest.fixture
def mock_print(monkeypatch):
    mock_print = mock.Mock()
    monkeypatch.setattr('builtins.print', mock_print)  # Mocking print function
    return mock_print

@pytest.fixture
def mock_factorial():
    with mock.patch('Programs.P04_Factorial.factorial') as mocked_factorial:
        yield mocked_factorial

# happy path - factorial - Test that factorial of 5 returns 120
def test_factorial_of_5():
    result = factorial(5)
    assert result == 120


# happy path - factorial - Test that factorial of 0 returns 1
def test_factorial_of_0():
    result = factorial(0)
    assert result == 1


# happy path - factorial - Test that factorial of 1 returns 1
def test_factorial_of_1():
    result = factorial(1)
    assert result == 1


# happy path - factorial - Test that factorial of 3 returns 6
def test_factorial_of_3():
    result = factorial(3)
    assert result == 6


# happy path - factorial - Test that factorial of 4 returns 24
def test_factorial_of_4():
    result = factorial(4)
    assert result == 24


# edge case - factorial - Test that factorial of -1 prints invalid entry
def test_factorial_of_negative(mock_print):
    factorial(-1)
    mock_print.assert_called_with('Invalid entry! Cannot find factorial of a negative number')


# edge case - factorial - Test that factorial of -5 prints invalid entry
def test_factorial_of_negative_5(mock_print):
    factorial(-5)
    mock_print.assert_called_with('Invalid entry! Cannot find factorial of a negative number')


# edge case - factorial - Test that factorial of a large number 10 returns 3628800
def test_factorial_of_large_number():
    result = factorial(10)
    assert result == 3628800


# edge case - factorial - Test that factorial of 2 returns 2
def test_factorial_of_2():
    result = factorial(2)
    assert result == 2


# edge case - factorial - Test that factorial of 6 returns 720
def test_factorial_of_6():
    result = factorial(6)
    assert result == 720


