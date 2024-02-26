import json

def read_json(path: str) -> dict:
    """The function of reading data from a json file
    Args:
      path: the path to the file
    Returns:
      Dictionary with json file structure
    """
    with open(path, 'r', encoding='UTF-8') as file:
        return json.load(file)