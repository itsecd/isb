import json


def read_from_file(directory: str) -> str:
    """
    The function opens a text file and reads the data into a string
    :param directory: file directory
    :return: string with text
    """
    with open(directory, mode="r", encoding="utf-8") as file:
        return file.read()


def write_to_file(directory: str, data: str) -> None:
    """
    The function opens/creates a text file and writes data to it
    :param directory: file directory
    :param data: data that will be written to the file
    :return: None
    """
    with open(directory, mode="w", encoding="utf-8") as file:
        file.write(data)


def read_data(directory: str) -> dict[str, int]:
    """
    The function opens a json file and reads the key as a dictionary
    :param directory: json file directory
    :return: key as a dictionary
    """
    with open(directory, mode="r", encoding="utf-8") as file:
        return json.load(file)


def save_data(directory: str, data: dict[str, float]) -> None:
    """
    The function saves the data to a json file
    :param directory: json file directory
    :param data: data that will be written to the file
    :return:
    """
    with open(directory, mode="w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)
