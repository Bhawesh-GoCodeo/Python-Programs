import pytest
from unittest import mock
import Programs.P02_VariableScope as module

@pytest.fixture
def mock_setup():
    with mock.patch('Programs.P02_VariableScope.print') as mock_print:
        yield mock_print

    with mock.patch('Programs.P02_VariableScope.x', new_callable=mock.PropertyMock) as mock_global_x:
        mock_global_x.return_value = 'Global x'
        yield mock_global_x

# happy path - test - Test that local variables are used within the function
def test_local_variables(mock_setup):
    module.test()
    mock_setup.assert_called_once_with('Local x, Local y')


# happy path - test - Test that global variable is not modified inside the function
def test_global_variable_unmodified(mock_setup):
    module.test()
    assert module.x == 'Global x'


# happy path - test - Test that function prints local x and local y
def test_function_output(mock_setup):
    module.test()
    mock_setup.assert_called_once_with('Local x, Local y')


# happy path - test - Test that global x is printed after function call
def test_global_x_after_function(mock_setup):
    module.test()
    mock_setup.assert_any_call('Global x')


# happy path - test - Test that local variable y is not accessible outside function
def test_local_y_scope():
    try:
        y
    except NameError as e:
        assert str(e) == "name 'y' is not defined"


# edge case - test - Test that accessing local variable outside function raises error
def test_access_local_variable_outside():
    try:
        y
    except NameError as e:
        assert str(e) == "name 'y' is not defined"


# edge case - test - Test that modifying global variable inside function with global keyword
def test_modify_global_variable(mock_setup):
    with mock.patch('Programs.P02_VariableScope.test') as mock_test:
        mock_test.side_effect = lambda: exec('global x; x = "Modified Global x"')
        mock_test()
    assert module.x == 'Modified Global x'


# edge case - test - Test that using global keyword allows modification of global variable
def test_global_keyword_effect(mock_setup):
    with mock.patch('Programs.P02_VariableScope.test') as mock_test:
        mock_test.side_effect = lambda: exec('global x; x = "Modified Global x"')
        mock_test()
    mock_setup.assert_any_call('Modified Global x')


# edge case - test - Test that local variable x does not affect global x
def test_local_global_x_independence(mock_setup):
    module.test()
    assert module.x == 'Global x'


# edge case - test - Test that declaring a variable with same name in different scopes does not interfere
def test_scope_independence(mock_setup):
    module.test()
    mock_setup.assert_called_once_with('Local x, Local y')
    assert module.x == 'Global x'


