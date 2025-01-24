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
    [
        print(file.name)
        for file in (files_paths if not sort else sorted(files_paths))
        if (match if case else match.lower()) in (file.name if case else file.name.lower())
    ]