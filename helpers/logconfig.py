from enum import Enum
import logging


_loglevels = logging.getLevelNamesMapping()
choices = list(zip(_loglevels, _loglevels))
LogLevels = Enum('LogLevels', choices)
