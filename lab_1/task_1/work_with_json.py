import json


def read_json_file(file_path: str) -> dict:
    """
    a method for reading paths from a json file
    parametrs: file_path as str
    return: dict

    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Файл не найден.")
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON-данных.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
