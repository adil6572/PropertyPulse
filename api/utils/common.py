import random
import string
import json

def generate_random_filename():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.json'

def read_json_file(file_path):
    """
    Reads a JSON file and returns its contents as a dictionary.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The JSON contents as a dictionary.
    """
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data
