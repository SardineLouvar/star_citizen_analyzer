import json

from pathlib import Path

from src.paths import JSON_PATH


def json_exists(name):
    path = Path(JSON_PATH) / f"{name}.json"
    return path.is_file()


def get_json(name):
    json_file = JSON_PATH / f"{name}.json"

    if json_exists(name):
        with open(json_file, "r", encoding="utf+8") as f:
            data = json.load(f)
        return data
    
    else:
        print(f"no existing json found for {name}")
        return None