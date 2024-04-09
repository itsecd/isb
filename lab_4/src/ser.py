import json
import logging

from typing import Set

logger = logging.getLogger(__name__)


def read_file_lines(path_to_file: str) -> Set[str]:
    """
    Read lines from a file and return them as a set.

    Args:
        - path_to_file (str): The path to the input file.

    Returns:
        - set: A set containing the lines read from the file.

    Raises:
        - TypeError: If there's an error reading the file.
    """

    try:
        with open(path_to_file, "r") as file:

            lines_set = set()

            for line in file:

                cleaned_line = line.strip()
                lines_set.add(cleaned_line)

        logger.info(f"Read[{path_to_file}] file lines successfull.")
        return lines_set

    except Exception as e:

        raise TypeError(f"Read[{path_to_file}] read file lines error, {e}")


def write_file_lines(path_to_file: str, data: Set[str]) -> None:
    """
    Write lines to a file.

    Args:
        - path_to_file (str): The path to the output file.
        - data (set): The set of lines to write to the file.

    Raises:
        - TypeError: If there's an error writing to the file.
    """

    try:
        with open(path_to_file, "w") as file:
            for item in data:
                file.write(item + "\n")

        logger.info(f"Write[{path_to_file}] file lines successfull.")

    except Exception as e:

        raise TypeError(f"Write[{path_to_file}] read file lines error, {e}")


def write_json(path_to_output_json: str, result: dict) -> None:
    """Write a dictionary to a JSON file.

    Args:
        - path_to_output_json (str): The path to the output JSON file.
        - result (dict): The dictionary to write to the JSON file.

    Raises:
        - TypeError: If there's an error writing to the JSON file.
    """

    try:

        with open(path_to_output_json, "w") as f:
            json.dump(result, f, indent=4)

        logger.info(f"Write[{path_to_output_json}] file json successfull")

    except Exception as e:

        raise TypeError(f"Write[{path_to_output_json}] file json error, {e}")
