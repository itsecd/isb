import json
import logging

def read_json(path_to_file: str) -> str:
    """
    This function reads and loads JSON data from a file specified by the path.

        Parameters:
            path_to_file (str): The path to the JSON file to read.

        Returns:
            str: The JSON data loaded from the file.
    """
    with open(path_to_file, 'r', encoding="utf-8") as file:        
        try:   
            json_data = json.load(file)         
            return json_data
        except Exception as e:
            logging.error(e)  
                    
        
def write_to_file(str: str, path: str) -> None:
    """
    Write a string to a file.

        Args:
            str (str): The string to write to the file.
            path (str): The file path where the string will be written.

        Returns:
            None
    """
    try:
        with open(path, 'a', encoding='utf-8') as file:
            file.write(str)
    except Exception as e:
        logging.error(e)