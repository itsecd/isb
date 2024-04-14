import json


def write_file(pathname: str, string: str) -> None:
    """
    pathname - путь к файлу, в которую идёт запись
    string - записываемая строка
    Данная функция осуществляет запись строки string в файл по пути pathname
    """
    try:
        with open(pathname, 'w', encoding='utf-8') as file_write:
            file_write.write(string)
    except FileNotFoundError:
        print(f"Создан файл с названием: {pathname}")
    except Exception as e:
        print(f"Произошла ошибка при работе с файлом {pathname}: {e}")


def read_file(pathname: str) -> str:
    """
        pathname - путь к файлу, который нужно прочитать
        Данная функция считывает содержимое файла по пути pathname
    """
    s = ''
    try:
        with open(pathname, 'r', encoding='utf-8') as file_read:
            s = file_read.read()
    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")
    return s


def get_dict_from_json(pathname):
    """
    pathname - путь к файлу
    Данная функция преобразовывает содержимое файла JSON в словарь
    """
    try:
        with open(pathname, 'r', encoding='utf-8') as file_read:
            data = json.load(file_read)
    except FileNotFoundError:
        print(f"Файл {pathname} не найден.")
        return {}
    except Exception as e:
        print(f"Произошла ошибка при чтении файла {pathname}: {e}")
        return {}

    return data