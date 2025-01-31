from tempfile import TemporaryDirectory
from pathlib import Path
import json

from helpers import config


def test_config_load_defaults():
    assert config._config == config.load('wrong')


def test_fake_config():
    with TemporaryDirectory() as tempdir:
        fakedata = {
            'input_dir': 'inputdir',
            'output_dir': 'outputdir'
        }
        fakeconfig_path = str(Path(tempdir, 'config.json'))
        with open(fakeconfig_path, 'w') as fp:
            json.dump(fakedata, fp)
        
        data = config.load(fakeconfig_path)
        assert data == fakedata


def test_check_after():
    assert config._defaults != config._config


def test_reset_to_defaults():
    config.reset_to_defaults()
    assert config._defaults == config._config