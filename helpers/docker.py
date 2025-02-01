import subprocess
from time import sleep
import logging
from pathlib import Path


logger = logging.getLogger(__name__)

# workaround for testing
# delete after implementation
try:
    from helpers import commands
except ModuleNotFoundError:
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from helpers import commands


def check_yml(path:str=None, filename:str='docker-compose.yml') -> None:
    if path:
        yml = Path(path, 'docker-compose.yml')
    else:
        yml = Path('docker-compose.yml')
    if not yml.exists():
        raise FileNotFoundError(yml)


def db_up(path:str=None) -> subprocess.CompletedProcess:
    check_yml(path)
    return commands.run(
        'docker compose up -d',
        raise_for_errors=True
    )


def docker_compose_ps() -> list[str]|None:
    completed = commands.run(
        'docker compose ps -q',
        raise_for_errors=True
    )
    # print(f'{completed.stdout!r}')
    if completed.stdout and completed.stdout.splitlines():
        return completed.stdout.splitlines()
    return None


def db_down(path:str=None) -> subprocess.CompletedProcess:
    check_yml(path)
    return commands.run(
        'docker compose down',
        raise_for_errors=True
    )


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    logger.info(f'main {Path.cwd()}')
    try:
        print('spinning up db...')
        db_up()
        
        containers = docker_compose_ps()
        if not containers:
            logging.error('no containers')
        else:
            print('Ok')
            for container in containers:
                logger.info(f'{container = }')
        
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
        logger.info(f'''{cpe.stderr = !s}''')
        logger.info(f"""{cpe.stdout = !s}""")
