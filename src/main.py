import os
import shutil

from pathlib import Path

from src.config_loader import load_config
from src.paths import ANALYSIS_DATA_PATH, FIG_PATH
from src.io.json_io import fetch_and_save_json
from src.db.db_manager import json_into_db

config = load_config()

def check_key():
    if not config["api_token"]:
        print("No API token detected in config.yaml. If you would like to run the program once, paste the token below")

        user = str(input("Token : "))

        if user == "":
            raise ValueError("API token is missing in the config. Please add before running.")
        else:
            return user


def generate_analysis_file(name):
    file_path = Path(ANALYSIS_DATA_PATH) / f"{name}.py"

    if not file_path.exists():
        file_path.touch()
        print(f"file {name}.py created")


def generate_history_analysis_file(name):
    file_path = Path(ANALYSIS_DATA_PATH) / "History" / f"{name}.py"

    if not file_path.exists():
        file_path.touch()
        print(f"file {name}.py created")


def generate_fig_folder(name):
    folder_path = Path(FIG_PATH) / name

    if not folder_path.exists():
        folder_path.mkdir(exist_ok=True)
        print(f"folder {name} created for figures")


def generate_history_fig_folder(name):
    folder_path = Path(FIG_PATH) / "History" / name

    if not folder_path.exists():
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"folder {name} created in history folder for figures")


def delete_pycache_dirs():
    """
    Task: Remove all pycache directories for cleaner look after running code.
    """
    for dirpath, dirnames, filenames in os.walk("."):
        for dirname in dirnames:
            if dirname == "__pycache__":
                full_path = os.path.join(dirpath, dirname)
                shutil.rmtree(full_path)


if __name__ == "__main__":
    temp_key = check_key()

    # Resources to get data on
    resources = ["commodities_prices_all", "cities", "space_stations"]

    #general APIs
    for r in resources:
        fetch_and_save_json(r, temp_key)
        json_into_db(r)
        generate_analysis_file(r)
        generate_fig_folder(r)

    # List of [commodity_id, terminal_id] to get history of (get from commodities_prices_all)
    id_searches = [[5,12],[32,16]]

    # commodity histories
    for id in id_searches:
        name = fetch_and_save_json(id, temp_key, history=True)
        json_into_db(name)
        generate_history_analysis_file(name)
        generate_history_fig_folder(name)

    delete_pycache_dirs()
    