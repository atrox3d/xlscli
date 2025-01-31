import pandas
import logging
from pathlib import Path
import typer


logger = logging.getLogger(__name__)


def open_xls(path:Path) -> pandas.DataFrame:
    workbook = pandas.read_excel(path, sheet_name=None)
    for sheet, df in workbook.items():
        print()
        print(sheet)
        print()
        print(df.to_string(index=False))
        print()
    print(f'total sheets: {len(workbook)}')
    print(f'sheets: {list(workbook.keys())}')

