from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Generator
import pytest


@pytest.fixture
def temp_dir() -> Generator[str, None, None]:
    with TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture
def fake_files(temp_dir) -> Generator[list[str], None, None]:
    fake_xls_files = ['1.xls', '2.xlsx', 'a.xls']
    for file in fake_xls_files:
        Path(temp_dir, file).touch()
    yield fake_xls_files
