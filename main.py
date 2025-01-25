import logging
import typer

from commands import files
from helpers import logconfig
from helpers import config

logger = logging.getLogger(__name__)

app = typer.Typer(add_completion=False, no_args_is_help=True)
app.command('list')(files.list_files)
app.command('open')(files.open_file)

# main                          -> help
# main list <path or .>         -> list

# main open <filepath>          -> open
# main open <filepath|filename> --path <path>       -> choose -> open
# main browse <path>            -> choose -> open




@app.callback(invoke_without_command=True)
def default(
    ctx:typer.Context, 
    path:str=config.input_dir(),
    match:str='',
    case:bool=False,
    sort:bool=True,  # list params
    log_level:logconfig.LogLevels = 'INFO'
):
    '''***DEFAULT ACTION WITH NO ARGUMENTS IS THE LIST COMMAND***'''
    
    logging.basicConfig(level=log_level.value)
    print(f'{ctx.default_map = }')
    ctx.ensure_object(dict)
    logger.info(f'main callback STARTED {ctx.invoked_subcommand = }')
    # if ctx.invoked_subcommand is None:
        # files.list_files(path, match, case, sort)


if __name__ == "__main__":
    app()