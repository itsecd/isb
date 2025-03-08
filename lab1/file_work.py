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
