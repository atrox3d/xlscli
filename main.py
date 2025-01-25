import logging
import pandas
import numpy
import typer

from commands import files
from helpers import logconfig
from helpers import config

logger = logging.getLogger(__name__)

app = typer.Typer(add_completion=False)
app.add_typer(files.app, name='files')


@app.callback(invoke_without_command=True)
def default(
    ctx:typer.Context, 
    path:str=config.data_dir(), match:str='', case:bool=False, sort:bool=True,
    log_level:logconfig.LogLevels = 'INFO'
):
    logging.basicConfig(
        level=log_level.value
    )
    
    ctx.ensure_object(dict)
    
    logger.debug(f'main callback STARTED {ctx.invoked_subcommand = }')
    if ctx.invoked_subcommand is None:
        files.list_files(path, match, case, sort)


if __name__ == "__main__":
    app()