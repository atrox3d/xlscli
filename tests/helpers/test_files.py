from tempfile import TemporaryDirectory
from pathlib import Path
from typing import Generator
import pytest


from helpers import files


@pytest.fixture
def temp_dir() -> Generator[str, None, None]:
    with TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture
def fake_files(temp_dir) -> Generator[list, None, None]:
    fake_xls_files = ['1.xls', '2.xlsx', 'a.xls']
    for file in fake_xls_files:
        Path(temp_dir, file).touch()
    yield fake_xls_files


def test_get_files(temp_dir, fake_files):
    assert files.get_files(temp_dir) == fake_files


def test_get_files_match(temp_dir, fake_files):
    assert files.get_files(temp_dir, match='1') == ['1.xls']


def test_get_files_match_case_sensitive(temp_dir, fake_files):
    assert files.get_files(temp_dir, match='a', case=True) == ['a.xls']
    assert files.get_files(temp_dir, match='A', case=True) == []


def test_get_files_reverse(temp_dir, fake_files):
    assert files.get_files(temp_dir, reverse=True) == sorted(fake_files, reverse=True)


def test_get_files_empty(temp_dir):
    assert files.get_files(temp_dir) == []


