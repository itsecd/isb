import json
import logging

logging.basicConfig(level=logging.INFO)


class SerializeDeserialize:
    """
    Class for serializing and deserializing data from and to file
    """
    def __init__(self, path: str) -> None:
        self.path = path

    def serialize_key(self, key: bytes) -> None:
        """
        Serialize the key and save it to a file.
        :param key: The key to be serialized.
        """
        try:
            with open(self.path, 'wb') as key_file:
                key_file.write(key)
        except Exception as ex:
            logging.error(f"File is not exist - {ex}")

    def deserialize_key(self) -> bytes:
        """
        Deserialize the key from a file.
        :return: The deserialized key.
        """
        try:
            with open(self.path, 'rb') as key_file:
                return key_file.read()
        except Exception as ex:
            logging.error(f"File is not exist - {ex}")

    def read_text_file(self, mode: str, encoding=None) -> str:
        """
        Read text from a file.
        :param mode: The mode to open the file in.
        :param encoding: (str, optional) The encoding of the text file. Defaults to None .

        :return: The content of the text file.
        """
        try:
            with open(self.path, mode=mode, encoding=encoding) as file:
                return file.read()
        except Exception as ex:
            logging.error(f"File is not exist - {ex}")

    def write_text_file(self, text: str) -> None:
        """
        Write text to a file.

        :param text: The text to write to the file.
        """
        try:
            with open(self.path, 'wb') as file:
                file.write(text)
        except Exception as ex:
            logging.error(f"File is not exist - {ex}")

    def read_json_file(self) -> dict:
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                paths = json.load(f)
            return paths
        except Exception as ex:
            logging.error(f"File is not exist - {ex}")
