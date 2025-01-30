import logging
import typer
from pathlib import Path

from helpers.files import get_files
from helpers import xls


logger = logging.getLogger(__name__)

# @app.command('list')
def list_files(
        ctx:typer.Context, 
        path:str=typer.Argument(default='.'),
        match:str='',
        case:bool=False,
        sort:bool=True,
        reverse:bool=False
):
    logger.info(f'listing xls* files in {Path(path).resolve()}')
    file_list = get_files(path, match, case, sort, reverse)
    for file in file_list:
        print(file)


def browse_file(
        path:str=typer.Argument(default='.'),
        match:str='',
        case:bool=False,
        sort:bool=True,
        reverse:bool=False
) -> str:
    file_list = get_files(path, match, case, sort, reverse)
    logger.info(f'listing xls* files in {Path(path).resolve()}')
    if file_list:
        for n, file in enumerate(file_list, 1):
            print(f'({n:2}) - {file!r}')
        try:
            fileno = input('choose file number: ')
            fileno = int(fileno)
            print(f'you have chosen {fileno}: {file_list[fileno-1]}')
            filename = file_list[fileno-1]
            open_file(filename, path)
        except IndexError:
            print(f'wrong number: {fileno}')
            raise typer.Abort()
        except ValueError:
            print(f'invalid number: {fileno!r}')
            raise typer.Abort()
    else:
        logger.warning(f'no xls* files found in {Path(path).resolve()}')

# @app.command('open')
def open_file(
        filename:str,
        path:str=None,
):
    if path is not None:
        filepath = Path(path, filename)
    else:
        filepath = Path(filename)
    try:
        xls.open_xls(filepath)
    except FileNotFoundError as e:
        logger.fatal(f'{filepath} does not exist')
        raise typer.Abort()
