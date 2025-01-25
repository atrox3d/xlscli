import logging
import typer
from pathlib import Path

from helpers import files
from helpers import xls
from helpers import config


logger = logging.getLogger(__name__)

app = typer.Typer()


@app.callback(invoke_without_command=True)
def default(
        ctx:typer.Context,
        path:str=config.input_dir(),
        match:str='',
        case:bool=False,
        sort:bool=True
):
    ctx.ensure_object(dict)
    
    logger.debug(f'files callback STARTED {ctx.invoked_subcommand = }')
    if ctx.invoked_subcommand is None:
        list_files(path, match, case, sort)


@app.command('list')
def list_files(
        path:str='.',
        match:str='',
        case:bool=False,
        sort:bool=True
):
    files_paths = list(Path(path).glob('*.xls*'))
    file_list = [
        file.name
        for file in (files_paths if not sort else sorted(files_paths))
        if (match if case else match.lower()) in (file.name if case else file.name.lower())
    ]
    # for n, file in enumerate(file_list, 1):
        # print(f'({n:2}) - {file!r}')
    for file in file_list:
        print(file)

@app.command('open')
def open_file(
        filename:str = typer.Argument(default=None),
        path:str=config.input_dir(),
        match:str='', 
        case:bool=False,
        sort:bool=True
):
    if filename is None:
        # filename = files.choose_file(path, match, case, sort)
        raise typer.Exit(1)
    filepath = Path(path, filename)
    try:
        xls.open_xls(filepath)
    except FileNotFoundError as e:
        logger.fatal(f'{filepath} does not exist')
        raise typer.Abort()


