import requests

from src.config_loader import load_config

def test_api(url, temp_key = None):
    """
    Test a url to check that it is working correctly (expected <Response [200]>)
    
    :param url: The full url on the API to be tested
    :param temp_key: the token if submitted temporarily
    """
    headers = {
    "Authorization": f"Bearer {config['api_token']}",
    "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.ok:
        return response
    else:
        print("Error:", response.status_code, response.text)
        return None
    

if __name__ == "__main__":
    config = load_config()

    url = str(input("URL to test: "))

    print(test_api(url))