import json

def read_txt_file(file_path: str) -> str:
    """
    Read the content of a text file.

    :param file_path: The path to the text file.
    :return: The content of the text file.
    """
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading file: {str(e)}"

def write_txt_file(file_path: str, content: str) -> str:
    """
    Write content to a text file.

    :param file_path: The path to the text file.
    :param content: The content to be written to the file.
    :return: A message indicating the status of the file writing process.
    """
    try:
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(content, ensure_ascii=False)
        return "File recorded"
    except Exception as e:
        return f"Error writing file: {str(e)}"

def load_json_file(file_path: str) -> dict:
    """
    Load JSON data from a JSON file.

    :param file_path: The path to the JSON file.
    :return: The JSON data loaded from the file.
    """
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data
    except Exception as e:
        return f"Error loading JSON file: {str(e)}"

def save_json_file(file_path: str, data: dict) -> str:
    """
    Save JSON data to a JSON file.

    :param file_path: The path to the JSON file.
    :param data: The JSON data to be saved to the file.
    :return: A message indicating the status of the file saving process.
    """
    try:
        with open(file_path, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return "JSON file saved"
    except Exception as e:
        return f"Error saving JSON file: {str(e)}"