import logging

logging.basicConfig(level=logging.INFO)


def write_data(path: str, data: bytes) -> None:
    """Function for writing data in file

    parametrs:
    path: path where the file is located
    data: data to be recorded
    """
    try:
        with open(path, "wb") as f:
            f.write(data)
    except Exception as ex:
        logging.error(f"File writing error: {ex.message}\n{ex.args}\n")


def read_file(path: str) -> bytes:
    """Function for reading files

    parametrs:
    path: path where the file is located

    return bytes:data
    """
    try:
        with open(path, "rb") as f:
            data = f.read()
        return data
    except Exception as ex:
        logging.error(f"File reading error: {ex.message}\n{ex.args}\n")
