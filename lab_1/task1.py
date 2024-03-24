from works_files import *

alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя :.,?/!()- \n "


def cipher(mode: Mode, path_key: str, input_path: str, output_path: str) -> None:
    """
        implements a cipher with a key and writes the data to a file

        Parameters
            mode: A Mode enumeration indicating the mode of operation (encryption or decryption).
            path_key: the path to the key file
            input_path: path to the file where the message is located
            output_path: the path where the cipher will be written
    """
    key = read_json(path_key)
    result = ''
    text = read_files(input_path)

    for char in text:
        match mode:
            case Mode.ENCRYPT:
                if char in key:
                    result += key[char]
                else:
                    result += char
            case Mode.DECRYPT:
                found_key = None
                for k, v in key.items():
                    if v == char:
                        found_key = k
                        break
                result += found_key

    write_files(output_path, result)


def key_json(key: str, path: str) -> None:
    """
    Create a key to the text using the transpose method for a given key
    value and write it to a json file as a dictionary

    Parameters
        key: the values of the key that will be used to create a new one
        path: the path where the key will be written
    """
    sz = len(key)
    key = dict()
    num_rows = -(-len(alphabet) // sz)
    matrix = [['' for _ in range(sz)] for _ in range(num_rows)]

    index = 0
    for row in range(num_rows):
        for col in range(sz):
            if index < len(alphabet):
                matrix[row][col] = alphabet[index]
                index += 1

    ciphertext = ''
    for col in range(sz):
        for row in range(num_rows):
            ciphertext += matrix[row][col]

    for i, char in enumerate(alphabet):
        key[char] = ciphertext[i]
    write_json(key, path)


if __name__ == "__main__":

    try:
        config = read_json("config.json")
        text_path = config["text_path_task1"]
        key_path = config["key_path_task1"]
        encryption_path = config["encryption_path_task1"]
        decryption_path = config["decryption_path_task1"]
        keys = config["keys_task1"]

        key_json(keys, key_path)
        cipher(Mode.ENCRYPT, key_path, text_path, encryption_path)
        cipher(Mode.DECRYPT, key_path, encryption_path, decryption_path)
    except Exception as e:
        print(f"An error occurred during the main execution: {e}")
