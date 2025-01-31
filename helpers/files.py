from pathlib import Path


def get_files(
        path   :str,
        match  :str  = '',
        case   :bool = False,
        sort   :bool = True,
        reverse:bool = False
) -> list[str]:
    files_paths = list(Path(path).glob('*.xls*'))
    file_list = [
        file.name
        for file in (files_paths if not sort else sorted(files_paths, reverse=reverse))
        if (match if case else match.lower()) in (file.name if case else file.name.lower())
    ]
    return file_list