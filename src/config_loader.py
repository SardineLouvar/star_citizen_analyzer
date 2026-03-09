import yaml

from pathlib import Path

from src.paths import CONFIG_PATH
from src.paths import DEV_CONFIG_PATH

path = CONFIG_PATH if not Path(DEV_CONFIG_PATH).is_file() else DEV_CONFIG_PATH

def load_config():
    with open(path, 'r') as f:
        return yaml.safe_load(f)