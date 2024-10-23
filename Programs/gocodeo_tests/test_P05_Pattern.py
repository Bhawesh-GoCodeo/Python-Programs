import pytest
from unittest.mock import patch, MagicMock
from Programs.P05_Pattern import pattern1, pattern2, pattern3, pattern4, pattern5, pattern6

@pytest.fixture
def mock_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '3')

@pytest.fixture
def mock_print(monkeypatch):
    mock_print = MagicMock()
    monkeypatch.setattr('builtins.print', mock_print)
    return mock_print

@pytest.fixture
def mock_pattern1():
    with patch('Programs.P05_Pattern.pattern1') as mock:
        yield mock

@pytest.fixture
def mock_pattern2():
    with patch('Programs.P05_Pattern.pattern2') as mock:
        yield mock

@pytest.fixture
def mock_pattern3():
    with patch('Programs.P05_Pattern.pattern3') as mock:
        yield mock

@pytest.fixture
def mock_pattern4():
    with patch('Programs.P05_Pattern.pattern4') as mock:
        yield mock

@pytest.fixture
def mock_pattern5():
    with patch('Programs.P05_Pattern.pattern5') as mock:
        yield mock

@pytest.fixture
def mock_pattern6():
    with patch('Programs.P05_Pattern.pattern6') as mock:
        yield mock

# happy path - pattern1 - Test that pattern1 generates correct increasing pattern for level 3
def test_pattern1_level_3(mock_input, mock_print, mock_pattern1):
    pattern1(3)
    expected_calls = [
        ("",),
        ("*",),
        ("",),
        ("**",),
        ("",),
        ("***",)
    ]
    mock_print.assert_has_calls(expected_calls, any_order=False)


# happy path - pattern2 - Test that pattern2 generates correct decreasing pattern for level 4
def test_pattern2_level_4(mock_input, mock_print, mock_pattern2):
    pattern2(4)
    expected_calls = [
        ("",),
        ("****",),
        ("",),
        ("***",),
        ("",),
        ("**",),
        ("",),
        ("*",)
    ]
    mock_print.assert_has_calls(expected_calls, any_order=False)


# happy path - pattern3 - Test that pattern3 generates correct right-aligned increasing pattern for level 4
def test_pattern3_level_4(mock_input, mock_print, mock_pattern3):
    pattern3(4)
    expected_calls = [
        ("   *",),
        ("  **",),
        (" ***",),
        ("****",)
    ]
    mock_print.assert_has_calls(expected_calls, any_order=False)


# happy path - pattern4 - Test that pattern4 generates correct right-aligned decreasing pattern for level 4
def test_pattern4_level_4(mock_input, mock_print, mock_pattern4):
    pattern4(4)
    expected_calls = [
        ("****",),
        (" ***",),
        ("  **",),
        ("   *",)
    ]
    mock_print.assert_has_calls(expected_calls, any_order=False)


# happy path - pattern5 - Test that pattern5 generates correct centered pyramid pattern for level 3
def test_pattern5_level_3(mock_input, mock_print, mock_pattern5):
    pattern5(3)
    expected_calls = [
        ("  *",),
        (" ***",),
        ("*****",)
    ]
    mock_print.assert_has_calls(expected_calls, any_order=False)


# happy path - pattern6 - Test that pattern6 generates correct increasing pattern for input 5
def test_pattern6_input_5(mock_input, mock_print, mock_pattern6):
    with patch('builtins.input', return_value='5'):
        pattern6(5)
    expected_calls = [
        ("*",),
        ("**",),
        ("***",),
        ("****",),
        ("*****",)
    ]
    mock_print.assert_has_calls(expected_calls, any_order=False)


# edge case - pattern1 - Test that pattern1 handles level 0 without error
def test_pattern1_level_0(mock_input, mock_print, mock_pattern1):
    pattern1(0)
    mock_print.assert_called_once_with("")


# edge case - pattern2 - Test that pattern2 handles level 0 without error
def test_pattern2_level_0(mock_input, mock_print, mock_pattern2):
    pattern2(0)
    mock_print.assert_called_once_with("")


# edge case - pattern3 - Test that pattern3 handles level 0 without error
def test_pattern3_level_0(mock_input, mock_print, mock_pattern3):
    pattern3(0)
    mock_print.assert_called_once_with("*")


# edge case - pattern4 - Test that pattern4 handles level 0 without error
def test_pattern4_level_0(mock_input, mock_print, mock_pattern4):
    pattern4(0)
    mock_print.assert_called_once_with("")


# edge case - pattern5 - Test that pattern5 handles level 0 without error
def test_pattern5_level_0(mock_input, mock_print, mock_pattern5):
    pattern5(0)
    mock_print.assert_called_once_with("")


# edge case - pattern6 - Test that pattern6 handles input 0 without error
def test_pattern6_input_0(mock_input, mock_print, mock_pattern6):
    with patch('builtins.input', return_value='0'):
        pattern6(0)
    mock_print.assert_called_once_with("")


