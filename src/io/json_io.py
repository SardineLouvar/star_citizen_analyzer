import json
import os

from pathlib import Path

from src.config_loader import load_config
from src.paths import JSON_PATH
from src.io.json_utils import json_exists
from src.io.api_access import get_request, get_history
from src.db.db_manager import cur

config = load_config()

def export_json(response, file_name):
    """
    Make a json file from a response and save to the folder specified

    Parameters
    ----------
    response : Response
        A response obtained from an API.
    file_name : str
        The name of the file that will be created / overwritten.
    """
    data = response.json()
    name = str(file_name + ".json")
    
    with open(os.path.join(JSON_PATH, name), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    
    print(f"{name} created...")


def fetch_and_save_json(resource, temp_key = None, history = False):
    """
    Make a request and save it as a json file if file isn't already made.

    Parameters
    ----------
    resource : str
        The resource that data will be retrieved on.
    """

    if history == True:
        #resource should be an array of arrays containing [commodity_id, terminal_id]
        comm_id = resource[0]
        term_id = resource[1]
        
        res = cur.execute(f"""SELECT commodity_name FROM commodities_prices_all
                    WHERE id_commodity = ? AND id_terminal = ?
                    """,(comm_id,term_id,)).fetchone()
        
        if res:
            name = f"{res[0]}_history_terminal_{term_id}".replace(" ", "_")
        else:
            print(f"No name found for id {comm_id}, terminal {term_id}")
            name = f"id_{comm_id[0]}_terminal_{term_id}"

        if not json_exists(name):
            response = get_history(term_id,comm_id,temp_key)
            export_json(response, name)
        else:
            if config["quiet"] == False:
                print(f"file {name} already exists. No json made")

        return name


    if not json_exists(resource):
        response = get_request(resource, temp_key)
        export_json(response, str(resource))
    else:
        if config["quiet"] == False:
            print(f"file {resource} already exists. No json made")
    return


if __name__ == "__main__":
    fetch_and_save_json("commodities_prices_all")