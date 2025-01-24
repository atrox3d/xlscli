import logging
from pathlib import Path
import pandas
import numpy
import typer


app = typer.Typer()


@app.callback(invoke_without_command=True)
def default(ctx:typer.Context):
    ctx.ensure_object(dict)
    print('STARTED')
    list_files()


@app.command('list')
def list_files(path:str='data'):
    files_paths = list(Path(path).glob('*.xls*'))
    print([file.name for file in files_paths])



if __name__ == "__main__":
    app()