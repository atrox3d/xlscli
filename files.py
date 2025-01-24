import logging
import typer
from pathlib import Path


logger = logging.getLogger(__name__)

app = typer.Typer()


@app.callback(invoke_without_command=True)
def default(ctx:typer.Context, path:str='data', match:str='', case:bool=False, sort:bool=True):
    ctx.ensure_object(dict)
    
    logger.debug(f'files callback STARTED {ctx.invoked_subcommand = }')
    if ctx.invoked_subcommand is None:
        list_files(path, match, case, sort)


@app.command('list')
def list_files(path:str='data', match:str='', case:bool=False, sort:bool=True):
    # print(locals())
    # exit()
    files_paths = list(Path(path).glob('*.xls*'))
    file_list = [
        file.name
        for file in (files_paths if not sort else sorted(files_paths))
        if (match if case else match.lower()) in (file.name if case else file.name.lower())
    ]
    for n, file in enumerate(file_list, 1):
        print(f'({n:2}) - {file!r}')


@app.command('choose')
def choose_file(path:str='data', match:str='', case:bool=False, sort:bool=True):
    # print(locals())
    # exit()
    files_paths = list(Path(path).glob('*.xls*'))
    file_list = [
        file.name
        for file in (files_paths if not sort else sorted(files_paths))
        if (match if case else match.lower()) in (file.name if case else file.name.lower())
    ]
    for n, file in enumerate(file_list, 1):
        print(f'({n:2}) - {file!r}')
    
    try:
        fileno = int(input('choose file number: '))
        print(f'you have chosen {fileno}: {file_list[fileno-1]}')
    except IndexError:
        print(f'wrong number {fileno}')
        raise typer.Abort()
