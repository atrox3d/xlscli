import logging
from pathlib import Path
import pandas
import numpy
import typer


app = typer.Typer()

@app.callback(invoke_without_command=True)
def callback(ctx:typer.Context):
    ctx.ensure_object(dict)
    print('STARTED')


if __name__ == "__main__":
    app()