import json


def read_json_file(file_name: str) -> dict:
    """
    Функция считывает данные из JSON файла с именем file_name.
    Возвращает словарь(dict).
    :param file_name:
    :return dict:
    """
    try:
        with open(file_name, "r", encoding="UTF-8") as file:
            json_data = json.load(file)
            return json_data
    except FileNotFoundError:
        print("Файл не найден.")
    except json.JSONDecodeError:
        print("Ошибка при считывании JSON-данных.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")