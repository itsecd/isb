import json


def read_json_file(file_path: str) -> dict:
    """
    Функция считывает данные из JSON файла.
    :param file_path:
    :return dict:
    """
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            json_data = json.load(file)
            return json_data
    except FileNotFoundError:
        print("Файл не найден.")
    except json.JSONDecodeError:
        print("Ошибка при считывании JSON-данных.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")