import json


def reader(file_name: str) -> str:
    """ reading file """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return ''.join(file.readlines())
    except Exception as e:
        print('error', e)
        raise


def writer(file: str, data: str) -> None:
    """ writing to file """
    try:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(data)
    except Exception as e:
        print('error', e)
        raise


def json_loader(file_name: str) -> dict:
    """ reading json file """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print('error', e)
        raise


def json_dumper(data, file_name: str) -> None:
    """ writing to json file keys using RU-symbols """
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
    except Exception as e:
        print('error', e)
        raise
