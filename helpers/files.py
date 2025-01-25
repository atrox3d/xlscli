import typer
from pathlib import Path

from helpers import config

def choose_file(path:str=config.data_dir(), match:str='', case:bool=False, sort:bool=True) -> str:
    files_paths = list(Path(path).glob('*.xls*'))
    file_list = [
        file.name
        for file in (files_paths if not sort else sorted(files_paths))
        if (match if case else match.lower()) in (file.name if case else file.name.lower())
    ]
    for n, file in enumerate(file_list, 1):
        print(f'({n:2}) - {file!r}')

    try:
        fileno = int(input('choose file number: '))
        print(f'you have chosen {fileno}: {file_list[fileno-1]}')
        return file_list[fileno-1]
    except IndexError:
        print(f'wrong number {fileno}')
        raise typer.Abort()