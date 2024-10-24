import pytest
from unittest import mock
from Programs.P07_PrimeNumber import checkPrime

@pytest.fixture
def mock_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2')

@pytest.fixture
def mock_print(mocker):
    return mocker.patch('builtins.print')

@pytest.fixture
def setup_check_prime(mock_input, mock_print):
    return mock_input, mock_print

# happy path - checkPrime - Test that 2 is correctly identified as a prime number
def test_check_prime_with_2(mock_print):
    checkPrime(2)
    mock_print.assert_called_once_with('2 is a Prime Number')


# happy path - checkPrime - Test that 3 is correctly identified as a prime number
def test_check_prime_with_3(mock_print):
    checkPrime(3)
    mock_print.assert_called_once_with('3 is a Prime Number')


# happy path - checkPrime - Test that 5 is correctly identified as a prime number
def test_check_prime_with_5(mock_print):
    checkPrime(5)
    mock_print.assert_called_once_with('5 is a Prime Number')


# happy path - checkPrime - Test that 7 is correctly identified as a prime number
def test_check_prime_with_7(mock_print):
    checkPrime(7)
    mock_print.assert_called_once_with('7 is a Prime Number')


# happy path - checkPrime - Test that 11 is correctly identified as a prime number
def test_check_prime_with_11(mock_print):
    checkPrime(11)
    mock_print.assert_called_once_with('11 is a Prime Number')


# edge case - checkPrime - Test that 1 is correctly identified as not a prime number
def test_check_prime_with_1(mock_print):
    checkPrime(1)
    mock_print.assert_called_once_with('1 is not a Prime Number')


# edge case - checkPrime - Test that 0 is correctly identified as not a prime number
def test_check_prime_with_0(mock_print):
    checkPrime(0)
    mock_print.assert_called_once_with('0 is not a Prime Number')


# edge case - checkPrime - Test that negative number -3 is correctly identified as not a prime number
def test_check_prime_with_negative_3(mock_print):
    checkPrime(-3)
    mock_print.assert_called_once_with('-3 is not a Prime Number')


# edge case - checkPrime - Test that 4 is correctly identified as not a prime number
def test_check_prime_with_4(mock_print):
    checkPrime(4)
    mock_print.assert_called_once_with('4 is not a Prime Number')


# edge case - checkPrime - Test that 9 is correctly identified as not a prime number
def test_check_prime_with_9(mock_print):
    checkPrime(9)
    mock_print.assert_called_once_with('9 is not a Prime Number')


