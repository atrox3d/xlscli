from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Generator
import pytest


@pytest.fixture
def temp_dir() -> Generator[str, None, None]:
    with TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture
def fake_xls_filenames() -> list[str]:
    return ['1.xls', '2.xlsx', 'a.xls']


@pytest.fixture
def fake_xls_files_ls_output(fake_xls_filenames) -> list[str]:
    return '\n'.join(fake_xls_filenames) + '\n'


@pytest.fixture
def fake_files(temp_dir, fake_xls_filenames) -> Generator[list[str], None, None]:
    for file in fake_xls_filenames:
        Path(temp_dir, file).touch()
    yield fake_xls_filenames
