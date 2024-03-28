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
    
    
    
def save_to_json_file(file_path: str, key: str):
    """
    Saves the key to a JSON file.
    
    Parameters:
        file_path (str): The path of the JSON file to save the key to.
        key (str): The key to be saved in the JSON file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as key_file:
            json.dump({'key': key}, key_file, ensure_ascii=False, indent=4)
        print(f"Ключ успешно сохранен в файл {file_path}")
    except Exception as e:
        print(f"Ошибка при сохранении ключа в файл {file_path}: {str(e)}")