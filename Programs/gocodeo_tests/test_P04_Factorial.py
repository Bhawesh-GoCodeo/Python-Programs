import pytest
from unittest import mock
from Programs.P04_Factorial import factorial

@pytest.fixture
def mock_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')  # Mock input to return '5'

@pytest.fixture
def mock_print(monkeypatch):
    mock_print = mock.Mock()
    monkeypatch.setattr('builtins.print', mock_print)
    return mock_print

@pytest.fixture
def mock_factorial():
    with mock.patch('Programs.P04_Factorial.factorial', wraps=factorial) as mock_factorial:
        yield mock_factorial

# happy path - factorial - Test that factorial of 5 returns 120
def test_factorial_of_5(mock_factorial):
    result = factorial(5)
    assert result == 120
    mock_factorial.assert_called_once_with(5)


# happy path - factorial - Test that factorial of 3 returns 6
def test_factorial_of_3(mock_factorial):
    result = factorial(3)
    assert result == 6
    mock_factorial.assert_called_once_with(3)


# happy path - factorial - Test that factorial of 1 returns 1
def test_factorial_of_1(mock_factorial):
    result = factorial(1)
    assert result == 1
    mock_factorial.assert_called_once_with(1)


# happy path - factorial - Test that factorial of 0 returns 1
def test_factorial_of_0(mock_factorial):
    result = factorial(0)
    assert result == 1
    mock_factorial.assert_called_once_with(0)


# happy path - factorial - Test that factorial of 4 returns 24
def test_factorial_of_4(mock_factorial):
    result = factorial(4)
    assert result == 24
    mock_factorial.assert_called_once_with(4)


# edge case - factorial - Test that factorial of -1 prints invalid entry
def test_factorial_of_negative_1(mock_factorial, mock_print):
    factorial(-1)
    mock_print.assert_called_once_with('Invalid entry! Cannot find factorial of a negative number')
    mock_factorial.assert_called_once_with(-1)


# edge case - factorial - Test that factorial of -5 prints invalid entry
def test_factorial_of_negative_5(mock_factorial, mock_print):
    factorial(-5)
    mock_print.assert_called_once_with('Invalid entry! Cannot find factorial of a negative number')
    mock_factorial.assert_called_once_with(-5)


# edge case - factorial - Test that factorial of a large number 10 returns 3628800
def test_factorial_of_10(mock_factorial):
    result = factorial(10)
    assert result == 3628800
    mock_factorial.assert_called_once_with(10)


# edge case - factorial - Test that factorial of -10 prints invalid entry
def test_factorial_of_negative_10(mock_factorial, mock_print):
    factorial(-10)
    mock_print.assert_called_once_with('Invalid entry! Cannot find factorial of a negative number')
    mock_factorial.assert_called_once_with(-10)


# edge case - factorial - Test that factorial of 2 returns 2
def test_factorial_of_2(mock_factorial):
    result = factorial(2)
    assert result == 2
    mock_factorial.assert_called_once_with(2)


