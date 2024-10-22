import pytest
from unittest import mock
import random
from Programs.P21_GuessTheNumber import guess

@pytest.fixture
def mock_input(monkeypatch):
    inputs = iter([10])  # Replace with desired inputs for each test case
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

@pytest.fixture
def mock_random_number():
    with mock.patch('random.randint', return_value=10):  # Replace with desired random number
        yield

# happy path - guess - Test that the function correctly identifies the guessed number when input matches the random number on the first try
def test_guess_correct_first_try(monkeypatch):
    inputs = iter([10])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch('random.randint', return_value=10):
        with mock.patch('builtins.print') as mocked_print:
            guess()
            mocked_print.assert_any_call('You have got it in', 1, 'tries')


# happy path - guess - Test that the function correctly identifies the guessed number when input matches the random number on the second try
def test_guess_correct_second_try(monkeypatch):
    inputs = iter([5, 10])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch('random.randint', return_value=10):
        with mock.patch('builtins.print') as mocked_print:
            guess()
            mocked_print.assert_any_call('You have got it in', 2, 'tries')


# happy path - guess - Test that the function correctly identifies the guessed number after multiple tries
def test_guess_correct_after_multiple_tries(monkeypatch):
    inputs = iter([1, 2, 3, 4, 5])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch('random.randint', return_value=5):
        with mock.patch('builtins.print') as mocked_print:
            guess()
            mocked_print.assert_any_call('You have got it in', 5, 'tries')


# happy path - guess - Test that the function outputs 'Too small' for a guess lower than the random number
def test_guess_too_small(monkeypatch):
    inputs = iter([5])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch('random.randint', return_value=10):
        with mock.patch('builtins.print') as mocked_print:
            guess()
            mocked_print.assert_any_call('Too small')


# happy path - guess - Test that the function outputs 'Too large' for a guess higher than the random number
def test_guess_too_large(monkeypatch):
    inputs = iter([15])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch('random.randint', return_value=10):
        with mock.patch('builtins.print') as mocked_print:
            guess()
            mocked_print.assert_any_call('Too large')


# edge case - guess - Test that the function handles the minimum boundary input of 0 correctly
def test_guess_min_boundary(monkeypatch):
    inputs = iter([0])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch('random.randint', return_value=0):
        with mock.patch('builtins.print') as mocked_print:
            guess()
            mocked_print.assert_any_call('You have got it in', 1, 'tries')


# edge case - guess - Test that the function handles the maximum boundary input of 20 correctly
def test_guess_max_boundary(monkeypatch):
    inputs = iter([20])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch('random.randint', return_value=20):
        with mock.patch('builtins.print') as mocked_print:
            guess()
            mocked_print.assert_any_call('You have got it in', 1, 'tries')


# edge case - guess - Test that the function handles consecutive incorrect guesses before a correct guess
def test_guess_consecutive_incorrect_then_correct(monkeypatch):
    inputs = iter([1, 2, 3, 10])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch('random.randint', return_value=10):
        with mock.patch('builtins.print') as mocked_print:
            guess()
            mocked_print.assert_any_call('You have got it in', 4, 'tries')


# edge case - guess - Test that the function handles repeated incorrect guesses of the same number
def test_guess_repeated_incorrect_guesses(monkeypatch):
    inputs = iter([5, 5, 5, 10])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch('random.randint', return_value=10):
        with mock.patch('builtins.print') as mocked_print:
            guess()
            mocked_print.assert_any_call('You have got it in', 4, 'tries')


# edge case - guess - Test that the function handles alternating too small and too large guesses before a correct guess
def test_guess_alternating_small_large_then_correct(monkeypatch):
    inputs = iter([5, 15, 10])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch('random.randint', return_value=10):
        with mock.patch('builtins.print') as mocked_print:
            guess()
            mocked_print.assert_any_call('You have got it in', 3, 'tries')


