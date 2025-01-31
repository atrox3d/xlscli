import pandas
import logging
from pathlib import Path
import typer


logger = logging.getLogger(__name__)


def print_sheet(sheet:str, df:pandas.DataFrame):
        print()
        print(sheet)
        print()
        print(df.to_string(index=False))
        print()


def ask_sheet(workbook:dict) -> str|None:
    if len(workbook) > 1:
        for n, sheet in enumerate(workbook):
            print(f'({n:2}) - {sheet!r}')
        choice = input('choose sheet number (enter=all): ')
        print(f'{choice!r}')
        
        return list(workbook.keys())[int(choice)] if choice else None
    else:
        return None


def open_xls(path:Path) -> pandas.DataFrame:
    workbook = pandas.read_excel(path, sheet_name=None)
    
    if (sheet :=ask_sheet(workbook)) is None:
        for sheet, df in workbook.items():
            print_sheet(sheet, df)
    else:
        print_sheet(sheet, workbook[sheet])

    print(f'total sheets: {len(workbook)}')
    print(f'sheets: {list(workbook.keys())}')

