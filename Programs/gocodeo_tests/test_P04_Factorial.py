import pytest
from unittest import mock
from Programs.P04_Factorial import factorial

@pytest.fixture
def mock_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')

@pytest.fixture
def mock_print(monkeypatch):
    mock_print = mock.Mock()
    monkeypatch.setattr('builtins.print', mock_print)
    return mock_print

@pytest.fixture
def mock_factorial():
    with mock.patch('Programs.P04_Factorial.factorial') as mock_factorial:
        yield mock_factorial

# happy path - factorial - Test that factorial of 5 returns 120



# happy path - factorial - Test that factorial of 0 returns 1



# happy path - factorial - Test that factorial of 1 returns 1



# happy path - factorial - Test that factorial of 3 returns 6



# happy path - factorial - Test that factorial of 4 returns 24



# edge case - factorial - Test that factorial of -1 prints an error message



# edge case - factorial - Test that factorial of -10 prints an error message



# edge case - factorial - Test that factorial of a large number like 20 returns correct result



# edge case - factorial - Test that factorial of 2 returns 2



