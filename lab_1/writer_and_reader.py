import logging


logging.basicConfig(level=logging.INFO)


def write_to_file(filename: str, content: str) -> None:
    """Write content to choosen file"""
    try:
        with open(filename, 'w', encoding="utf8") as file:
            file.write(content)
            logging.info(f"Successfully written to file '{filename}'")
    except IOError:
        logging.error(f"Error while writing to file'{filename}'.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


def read_from_file(filename: str) -> str:
    """Read and return content of the file"""
    try:
        with open(filename, 'r+', encoding="utf8") as file:
            content = file.read()
        logging.info(f"Successfully read from file '{filename}'")
        return content
    except IOError:
        logging.error(f"Error while reading from file '{filename}'")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")