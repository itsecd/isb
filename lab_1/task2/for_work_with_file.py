import json
import logging

def save_to_file(filename, content):
    """
    Saves the given content to a file with the specified filename.
    
    Parameters:
        filename (str): The name of the file to save to.
        content (str): The content to be written to the file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        logging.error(f"An error occurred while saving to file {filename}: {str(e)}")



def read_from_file(filename):
    """
    Reads the content from a file with the specified filename.
    
    Parameters:
        filename (str): The name of the file to read from.
    
    Returns:
        str: The content read from the file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        logging.error(f"An error occurred while reading from file {filename}: {str(e)}")
        return ""
       
def save_to_json_file(file_path: str, data):
    """
    Saves the given data to a JSON file.
    
    Writes the provided data dictionary to a JSON file located at the specified file path.
    
    Parameters:
        file_path (str): The path to the JSON file to save the data to.
        data (dict): The data to be saved to the JSON file.
    
    Raises:
        Exception: If an error occurs while writing data to the file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Data has been successfully written to the file {file_path}\n")
    except Exception as e:
        print(f"Error occurred while writing data to the file {file_path}: {str(e)}")
