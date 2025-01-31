from enum import StrEnum
import logging

# get logging levels mapping
_loglevels = logging.getLevelNamesMapping()

# create list of level, level tuples
_choices = list(zip(_loglevels, _loglevels))

# create enum type for main callback option
LogLevelsEnum = StrEnum('LogLevels', _choices)


def print_info():
    print(f'{_loglevels = }')
    print(f'{_choices = }')
    print(f'{LogLevelsEnum = }')