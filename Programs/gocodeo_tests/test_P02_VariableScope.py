import pytest
from unittest import mock
import Programs.P02_VariableScope as variable_scope

@pytest.fixture
def mock_print(mocker):
    mocker.patch('builtins.print', side_effect=lambda *args, **kwargs: None)

@pytest.fixture
def mock_global_x(mocker):
    mocker.patch.object(variable_scope, 'x', 'Global x')

@pytest.fixture
def mock_test_function(mocker):
    mocker.patch('Programs.P02_VariableScope.test', side_effect=variable_scope.test)

@pytest.fixture(autouse=True)
def setup_mocks(mock_print, mock_global_x, mock_test_function):
    pass

# happy path - test - Test that local variables are used inside the function
def test_local_variables(mock_global_x, mock_test_function):
    with mock.patch('builtins.print') as mocked_print:
        variable_scope.test()
        mocked_print.assert_called_once_with('Local x, Local y')


# happy path - test - Test that global variable is not affected by local variable assignment
def test_global_variable_unchanged(mock_global_x, mock_test_function):
    variable_scope.test()
    assert variable_scope.x == 'Global x'


# happy path - test - Test that function prints local x and local y
def test_function_output(mock_global_x, mock_test_function):
    with mock.patch('builtins.print') as mocked_print:
        variable_scope.test()
        mocked_print.assert_called_once_with('Local x, Local y')


# happy path - test - Test that global x is printed after function call
def test_global_x_after_function(mock_global_x, mock_test_function):
    variable_scope.test()
    with mock.patch('builtins.print') as mocked_print:
        print(variable_scope.x)
        mocked_print.assert_called_with('Global x')


# happy path - test - Test that local x does not affect global x
def test_local_does_not_affect_global(mock_global_x, mock_test_function):
    variable_scope.test()
    assert variable_scope.x == 'Global x'


# edge case - test - Test that global keyword changes x to global scope
def test_global_keyword_effect(mock_global_x, mock_test_function):
    with mock.patch('Programs.P02_VariableScope.test', side_effect=variable_scope.test):
        variable_scope.test()
        assert variable_scope.x == 'Local x'


# edge case - test - Test that local variables are not accessible outside the function
def test_local_variables_scope(mock_global_x, mock_test_function):
    variable_scope.test()
    with pytest.raises(NameError):
        print(y)


# edge case - test - Test that reassigning global x inside function without global keyword does not change global x
def test_reassign_global_without_keyword(mock_global_x, mock_test_function):
    variable_scope.test()
    assert variable_scope.x == 'Global x'


# edge case - test - Test that function runs without modifying global variables
def test_function_no_global_modification(mock_global_x, mock_test_function):
    variable_scope.test()
    assert variable_scope.x == 'Global x'


# edge case - test - Test that LEGB rule is followed for variable resolution
def test_legb_rule_followed(mock_global_x, mock_test_function):
    with mock.patch('builtins.print') as mocked_print:
        variable_scope.test()
        mocked_print.assert_called_once_with('Local x, Local y')


