class CryptoUtility:
    @staticmethod
    def serialize_key(key: bytes, key_path: str) -> None:
        """
        Serialize the key and save it to a file.

        :param key: The key to be serialized.
        :param key_path: The path where the serialized key will be saved.
        """
        with open(key_path, 'wb') as key_file:
            key_file.write(key)

    @staticmethod
    def deserialize_key(key_path: str) -> bytes:
        """
        Deserialize the key from a file.

        :param key_path: The path from where to deserialize the key.

        :return: The deserialized key.
        """
        with open(key_path, 'rb') as key_file:
            return key_file.read()

    @staticmethod
    def read_text_file(text_path: str, mode: str, encoding=None) -> str:
        """
        Read text from a file.

        :param text_path: The path to the text file.
        :param mode: The mode to open the file in.
        :param encoding (str, optional): The encoding of the text file. Defaults to None.

        :return: The content of the text file.
        """
        with open(text_path, mode=mode, encoding=encoding) as file:
            return file.read()

    @staticmethod
    def write_text_file(text: str, path: str) -> None:
        """
        Write text to a file.

        :param text: The text to write to the file.
        :param path: The path to the file.
        """
        with open(path, 'wb') as file:
            file.write(text)