import pytest
from unittest.mock import patch


@patch('builtins.print')
def test_greet_patch_decorator(mock_print):
    def greet(name):
        print('Hello ', name)
    
    # The actual test
    greet('John')
    mock_print.assert_called_with('Hello ', 'John')
    greet('Eric')
    mock_print.assert_called_with('Hello ', 'Eric')


def test_greet_patch_context_manager():
    def greet(name):
        print('Hello ', name)
    
    with patch('builtins.print') as mock_print:
        # The actual test
        greet('John')
        mock_print.assert_called_with('Hello ', 'John')
        greet('Eric')
        mock_print.assert_called_with('Hello ', 'Eric')