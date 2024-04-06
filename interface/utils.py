import requests
import json
import pandas as pd


def scrape_realtor_properties(url):
    """
    Function to scrape realtor properties by making a POST request to the specified URL.

    Parameters:
    - url (str): The URL of the Realtor website to scrape properties from.

    Returns:
    - json_data (dict): JSON data containing scraped properties if successful.
    - error_message (str): Error message if the request fails.
    """
    # Define the endpoint URL
    endpoint_url = "http://localhost:8000/realtor/properties"

    # Define headers to receive data in JSON format with a specified user agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Content-Type": "application/json"
    }

    # Define parameters for the POST request
    parameters = {"url": url}

    try:
        # Make the POST request
        response = requests.post(endpoint_url, data=json.dumps(parameters), headers=headers)

        # Check if request was successful
        if response.status_code == 200:
            # Return the response JSON data
            return response.json(), None
        else:
            # Return error message if request failed
            return None, f"Error: {response.status_code} - {response.reason}"
    except Exception as e:
        # Return exception message if an error occurs
        return None, f"Exception occurred: {str(e)}"


def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def transform_response(data: dict):
    if data is not None:
        properties= data.get("properties",'')
        if properties:
            results = [flatten_dict(d) for d in properties]
            df=pd.DataFrame(results)
            return df

            
            

if __name__=='__main__':
    url = "https://www.realtor.com/realestateandhomes-search/Los-Angeles_CA/type-single-family-home/price-na-600000/"
    json_data, error_message = scrape_realtor_properties(url)

    if json_data is not None:
        print("Response JSON data:")
        print(json_data)
    else:
        print("Error occurred:")
        print(error_message)
