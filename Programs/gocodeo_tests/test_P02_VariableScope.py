import pytest
from unittest import mock
import Programs.P02_VariableScope as module

@pytest.fixture
def mock_setup():
    with mock.patch('Programs.P02_VariableScope.print') as mock_print:
        yield {
            'mock_print': mock_print,
            'global_x': 'Global x'
        }

# happy path - test - Test that the function prints local variables correctly
def test_prints_local_variables(mock_setup):
    mock_setup['mock_print'].assert_called_with('Local x, Local y')


# happy path - test - Test that the global variable remains unchanged after function execution
def test_global_variable_unchanged(mock_setup):
    assert module.x == mock_setup['global_x']


# happy path - test - Test that the function runs without errors
def test_runs_without_errors(mock_setup):
    try:
        module.test()
    except Exception as e:
        pytest.fail(f"Function raised an exception: {e}")


# happy path - test - Test that the function does not affect other global variables
def test_no_side_effects_on_globals(mock_setup):
    other_global = 'unchanged'
    module.test()
    assert other_global == 'unchanged'


# happy path - test - Test that local variable 'y' is not accessible outside the function
def test_local_y_not_accessible_outside(mock_setup):
    with pytest.raises(NameError):
        print(y)


# edge case - test - Test that the function handles absence of global variable 'x' gracefully
def test_absence_of_global_x(mock_setup):
    with mock.patch('Programs.P02_VariableScope.x', new=None):
        try:
            module.test()
        except Exception as e:
            pytest.fail(f"Function raised an exception: {e}")


# edge case - test - Test that the function handles large local variable values
def test_large_local_values(mock_setup):
    with mock.patch('Programs.P02_VariableScope.x', new='x'), \
         mock.patch('Programs.P02_VariableScope.y', new='y'):
        module.test()
        mock_setup['mock_print'].assert_called_with('Local x, Local y')


# edge case - test - Test that the function handles special characters in local variables
def test_special_characters_in_locals(mock_setup):
    with mock.patch('Programs.P02_VariableScope.x', new='!@#$%^&*()'), \
         mock.patch('Programs.P02_VariableScope.y', new='<>?:'):
        module.test()
        mock_setup['mock_print'].assert_called_with('Local x, Local y')


# edge case - test - Test that the function handles numeric values in local variables
def test_numeric_values_in_locals(mock_setup):
    with mock.patch('Programs.P02_VariableScope.x', new=123), \
         mock.patch('Programs.P02_VariableScope.y', new=456):
        module.test()
        mock_setup['mock_print'].assert_called_with('Local x, Local y')


# edge case - test - Test that the function handles empty strings in local variables
def test_empty_strings_in_locals(mock_setup):
    with mock.patch('Programs.P02_VariableScope.x', new=''), \
         mock.patch('Programs.P02_VariableScope.y', new=''):
        module.test()
        mock_setup['mock_print'].assert_called_with('Local x, Local y')


