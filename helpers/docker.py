import subprocess
from time import sleep
import logging
from pathlib import Path
logger = logging.getLogger(__name__)

try:
    from helpers import commands
except ModuleNotFoundError:
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from helpers import commands
    


def db_up():
    completed = commands.run(
        'docker compose uap -d',
        raise_for_errors=True
    )
    return True


def db_down():
    completed = commands.run(
        'docker compose down',
        raise_for_errors=True
    )
    return True


if __name__ == "__main__":
    print('main')
    try:
        print('spinning up db...')
        db_up()
        print('Ok')
        sleep(5)
        print('shutting down...')
        db_down()
        print('done')
    except subprocess.CalledProcessError as cpe:
        logger.critical(f'cannot spin up db, details:')
        logger.critical(f'{cpe.args = }')
        logger.critical(f'{cpe.returncode = }')
        logger.critical(f'{cpe.cmd = }')
        logger.critical(f'\n')
        logger.critical(f'{cpe.stdout = }')
        logger.critical(f'{cpe.stderr = }')
        print(f'{cpe.stdout = }')
