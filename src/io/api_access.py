import requests

from src.config_loader import load_config

#use uex
#run with python -m src.api_access

config = load_config()

base_url = "https://api.uexcorp.uk/2.0/"


def sort_token(temp_key):
    headers = {
    "Authorization": f"Bearer {config['api_token']}",
    "Accept": "application/json"
    }

    if temp_key:
        headers = {
            "Authorization": f"Bearer {temp_key}",
            "Accept": "application/json"
            }
    
    return headers



def get_request(resource, temp_key = None):
    """
    Send a GET request to the UEX API and save the JSON response to disk.

    Parameters
    ----------
    resource : str
        The resource that data will be retrieved on.
    """

    headers = sort_token(temp_key)

    url = f"{base_url}{resource}"

    response = requests.get(url, headers=headers)

    if response.ok:
        return response
    else:
        print("Error:", response.status_code, response.text)
        return None


def get_history(id_terminal, id_commodity, temp_key = None):

    headers = sort_token(temp_key)

    url = f"{base_url}commodities_prices_history?id_terminal={id_terminal}&id_commodity={id_commodity}"

    response = requests.get(url, headers=headers)

    if response.ok:
        return response
    else:
        print("Error:", response.status_code, response.text)
        return None