import logging
import typer

from commands import files
from helpers import logconfig
from helpers import config

logger = logging.getLogger(__name__)

app = typer.Typer(add_completion=False, no_args_is_help=True)
app.command('list')(files.list_files)
app.command('open')(files.open_file)
app.command('browse')(files.browse_file)

# main                          -> help
# main list <path or .>         -> list

# main open <filepath>          -> open
# main open <filepath|filename> --path <path>       -> choose -> open
# main browse <path>            -> choose -> open




@app.callback(invoke_without_command=True)
def default(
    ctx:typer.Context, 
    # path:str='.',
    # match:str='',
    # case:bool=False,
    # sort:bool=True,  # list params
    log_level:logconfig.LogLevels = 'DEBUG'
):
    '''***DEFAULT ACTION WITH NO ARGUMENTS IS THE LIST COMMAND AND no_args_is_help==False***'''
    
    logging.basicConfig(level=log_level.value)
    print(f'{ctx.default_map = }')
    logger.debug('ensuring ctx.obj dict')
    ctx.ensure_object(dict)
    logger.debug(f'main callback STARTED {ctx.invoked_subcommand = }')
    # if ctx.invoked_subcommand is None:
        # files.list_files(path, match, case, sort)
    logger.debug(f'{ctx.args = }')
    # if not ctx.args:
        # ctx.get_help()

if __name__ == "__main__":
    app()