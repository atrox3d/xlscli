import pytest
from unittest.mock import patch, call

from commands import files


def test_list_files(
    # mockprint, 
    temp_dir, 
    fake_files, 
    fake_xls_filenames
):
    with patch('builtins.print') as mockprint:
        files.list_files(temp_dir)
        calls = mockprint.mock_calls
        assert calls == [call(f) for f in fake_xls_filenames]
    print(calls)


