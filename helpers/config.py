import json
import logging


logger = logging.getLogger(__name__)

_defaults = {
    'input_dir': '.data_in',
    'output_dir': '.data_out',
}
_config = _defaults.copy()


def reset_to_defaults():
    global _config
    _config = _defaults.copy()


def load(
    jsonpath  :str, 
    _config   :dict = _config, 
    _defaults :dict = _defaults
) -> dict:
    _config.update(_defaults)
    try:
        with open(jsonpath, 'r') as fp:
            data = json.load(fp)
        _config.update(data)
    except:
        logger.warning(f'could not load {jsonpath}')
    return _config


def input_dir() -> str:
    return _config['input_dir']
