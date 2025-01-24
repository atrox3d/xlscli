import logging
from pathlib import Path
import pandas
import numpy
import typer


app = typer.Typer()


@app.callback(invoke_without_command=True)
def default(ctx:typer.Context, path:str='data', match:str='', case:bool=False, sort:bool=True):
    ctx.ensure_object(dict)
    
    print('STARTED')
    
    list_files(path, match, case, sort)


@app.command('list')
def list_files(path:str='data', match:str='', case:bool=False, sort:bool=True):
    files_paths = list(Path(path).glob('*.xls*'))
    [print(file.name) for file in (files_paths if not sort else sorted(files_paths)) if (match if case else match.lower()) in (file.name if case else file.name.lower())]



if __name__ == "__main__":
    app()