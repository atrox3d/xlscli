import logging
import typer

from commands import files
from helpers import logging_enum
from helpers import config

logger = logging.getLogger(__name__)

app = typer.Typer(
    add_completion  = False,   # disable completion hint
    no_args_is_help = False   # need to always execute main callback
)

# link commands directly to functions, not to sub app
app.command('list'  )(files.list_files)
app.command('browse')(files.browse_file)
app.command('open'  )(files.open_file)

'''
schema of commands:

main                          -> help
main list <path or .>         -> list

main open <filepath>          -> open
main open <filepath|filename> --path <path>       -> choose -> open
main browse <path>            -> choose -> open
'''

@app.callback(invoke_without_command=True)
def default_callback(
    ctx       :typer.Context, 
    log_level :logging_enum.LogLevelsEnum='DEBUG'
):
    '''default_callback: configure logging, ctx and calls this help'''
    
    logging_enum.print_info()
    # configure logging
    logging.basicConfig(level=log_level.value)
    
    logger.debug(f'{ctx.default_map = }')
    
    logger.debug('ensuring ctx.obj dict')
    ctx.ensure_object(dict)
    
    logger.debug(f'main callback STARTED {ctx.invoked_subcommand = }')
    
    # call help if no args, no_args_is_help must be False
    logger.debug(f'{ctx.args = }')
    if not ctx.args:
        ctx.get_help()


if __name__ == "__main__":
    app()