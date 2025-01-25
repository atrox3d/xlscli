import logging
import pandas
import numpy
import typer

import commands.files as files
import logconfig

logger = logging.getLogger(__name__)

app = typer.Typer(add_completion=False)
app.add_typer(files.app, name='files')


@app.callback(invoke_without_command=True)
def default(
    ctx:typer.Context, 
    path:str='data', match:str='', case:bool=False, sort:bool=True,
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