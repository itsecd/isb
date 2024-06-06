import json
import logging

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

class Support:
    def save_to_file(filename, content):
        """
        Saves content to a file.

        Parameters:
        filename (str): The name of the file to save to.
        content (str): The content to write to the file.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
        except Exception as e:
            logging.error(f"Error while saving to file {filename}: {str(e)}")


    def read_from_file(filename):
        """
        Reads content from a file.
        
        Parameters:
        filename (str): The name of the file to read from.
        
        Returns:
        str: The content read from the file.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            logging.error(f"Error while reading from file {filename}: {str(e)}")
            return ""


    def read_from_json_file(filename):
        """
        Reads JSON data from a file.

        Parameters:
        filename (str): The name of the file to read from.

        Returns:
        dict: The JSON data read from the file.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except Exception as e:
            logging.error(f"Error while reading from file {filename}: {str(e)}")
            return {}


    def save_to_json_file(filename: str, data):
        """
        Saves data to a JSON file.

        Parameters:
        file_path (str): The path to the JSON file to save the data to.
        data (dict): The data to be saved to the JSON file.

        Raises:
            Exception: If an error occurs while writing data to the file.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False)
            print(f"Data has been successfully written to the file {filename}\n")
        except Exception as e:
            print(
                f"Error occurred while writing data to the file {filename}: {str(e)}")


    def write_bytes_to_txt(data: str, path: str) -> None:
        """
        Writes bytes data to a text file.

        Parameters:
        data (str): The bytes data to write to the file.
        path (str): The path to the text file to write the data to.
        """
        try:
            with open(path, 'wb') as file:
                file.write(data)
        except Exception as e:
            logging.error(f'[write_bytes_to_txt]: {e}')

    def read_bytes(path: str) -> bytes:
        """
        Reads bytes data from a text file.

        Parameters:
        path (str): The path to the text file to read the data from.

        Returns:
        bytes: The bytes data read from the file.
        """
        try:
            with open(path, 'rb') as file:
               return file.read()
        except Exception as e:
            logging.error(f'[read_bytes]: {e}')

    def serialize_sym_key(self, path: str) -> None:
        """
        Serializes the symmetric key to a file.

        Parameters:
        path (str): The path to save the key.

        Returns:
        None
        """
        Support.write_bytes_to_txt(self.key, path)

    def deserialize_sym_key(self, path: str) -> bytes:
        """
        Deserializes the symmetric key from a file.

        Parameters:
        path (str): The path to the key file.

        Returns:
        bytes: The deserialized symmetric key.
        """
        self.key = Support.read_bytes(path)
        return self.key
    
    def serialize_asym_key(self, path: str, key_type: str):
        """
        Serializes a key from a file.

        Parameters:
        path (str): The path to the key file.
        key_type (str): The type of key ('public' or 'private').

        Returns:
        The serialized key object.
        """
        with open(path, 'wb') as f:
            if key_type == 'private':
                f.write(self.private_key.private_bytes(encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()))
            elif key_type == 'public':
                f.write(self.public_key.public_bytes(encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo))
            else:
                raise ValueError("Invalid key type specified")

    def deserialize_asym_key(self, path: str, key_type: str):
        """
        Deserializes a key from a file.

        Parameters:
        path (str): The path to the key file.
        key_type (str): The type of key ('public' or 'private').

        Returns:
        The deserialized key object.
        """
        with open(path, 'rb') as f:
            key_bytes = f.read()
            if key_type == 'public':
                self.public_key = load_pem_public_key(key_bytes)
                return self.public_key
            elif key_type == 'private':
                self.private_key = load_pem_private_key(key_bytes, password=None)
                return self.private_key
            else:
                raise ValueError("Invalid key type specified")
