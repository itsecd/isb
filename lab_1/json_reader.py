import json

from typing import Dict

import consts

def read_json(path_input: str) -> Dict[str, str]:
    
    """Reads a JSON file and checks for required headers.

    Raises a `ValueError` if any of the required headers are missing.

    Args:
        - path_input (str): Path to the JSON file to be read.

    Returns:
        - dict: A dictionary containing the data from the JSON file.
    """

    data: Dict[str, str]

    with open(path_input, 'r') as f:
        data = json.load(f)

    for header in consts.MUST_CONTAINED_IN_FILE_INPUT:
        if not header in data.keys():
            raise ValueError(f"Header:  {header} not contains in {consts.MUST_CONTAINED_IN_FILE_INPUT}")

    return data

def write_json(dict_output: dict , path_output: str) -> None:
    
    """Writes a dictionary to a JSON file with proper encoding for non-ASCII characters.

    Args:
        - dict_output (dict): The dictionary to be written to the JSON file.
        - path_output (str): The path to the output JSON file.
    """
    
    with open(path_output, 'w') as f:
        json.dump(dict_output, f, indent=4, ensure_ascii=False)
