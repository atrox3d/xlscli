import pandas
import logging
from pathlib import Path
import typer


def open_xls(path:Path) -> pandas.DataFrame:
    df = pandas.read_excel(path, sheet_name=None)
    print(df)
    print(f'total sheets: {len(df)}')
    print(f'sheets: {list(df.keys())}')

