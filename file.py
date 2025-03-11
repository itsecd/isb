
import json

def open_file(path):
    """
    Function to open file
    :param path: path to your file
    :return: content
    """
    try:
        if path.endswith('.json'):
            with open(path, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            with open(path, 'r', encoding='utf-8') as file:
                return file.read()
    except FileNotFoundError:
        print(f"Файл '{path}' не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле '{path}'.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return None


def save(file, content):
    """
   Saving files

    :param file: name of file to save
    :param content: content of the file
    """
    if file.endswith('.json'):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=4)
    else:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f"Данные сохранены в файл: {file}")