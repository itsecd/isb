import json
import os

from config.messages import ERRORS


def write_to_file(path: str, text: str) -> None:
    """Writes text to a file.

    Args:
        path (str): File path.
        text (str): Text for writing.

    Raises:
        FileNotFoundError: Incorrect path to the file.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(ERRORS["invalid_file_path"].format(path=path))

    with open(path, "w", encoding="utf-8-sig") as file:
        file.write(text)


def read_file(path: str) -> str:
    """Reads a file at the path.

    Args:
        path (str): File path.

    Raises:
        FileNotFoundError: Incorrect path to the file.

    Returns:
        str: Text from file.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(ERRORS["invalid_file_path"].format(path=path))

    with open(path, "r", encoding="utf-8-sig") as file:
        return file.read()


def json_to_dict(path: str) -> dict:
    """Converts a json file to a dict object.

    Args:
        path (str): File path.

    Raises:
        FileNotFoundError: Incorrect path to the file.
        ValueError: The file does not have a json extension.
        ValueError: Incorrect contents of the json file.

    Returns:
        dict: Dictionary from json.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(ERRORS["invalid_file_path"].format(path=path))

    if not path.endswith(".json"):
        raise ValueError(ERRORS["file_not_json"].format(path=path))

    try:
        with open(path, "r", encoding="utf-8-sig") as file:
            settings = json.load(file)
            return settings
    except json.decoder.JSONDecodeError as e:
        raise ValueError(ERRORS["invalid_json"].format(path=path, e=e))


def read_settings() -> dict:
    """Reads the settings.json file.

    Returns:
        dict: Dictionary with settings.
    """
    settings_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "config",
        "settings.json"
    )
    return json_to_dict(settings_path)


def get_frequency(lang: str) -> dict:
    """Gets letter frequencies from files.

    Args:
        lang (str): Language key. For example: ru, en.

    Raises:
        ValueError: Incorrect lang key.

    Returns:
        dict: Dictionary with frequency.
    """
    settings = read_settings().get("letter_frequency", {})
    path = settings.get(lang)

    if path is None:
        raise ValueError(ERRORS["invalid_lang_key"].format(key=lang))

    return json_to_dict(path)
