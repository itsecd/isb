import os
import logging

def read_from_text_file(path_to_text_file: str) -> str:
    """Read encrypted text from a file"""
    encrypted_text: str = ""
    try:
        with open(os.path.join(path_to_text_file), "r") as file:
            for i in file:
                encrypted_text += i.replace('\n', '')
    except:
        logging.warning(f"The file {path_to_text_file} is not exist!", NameError)

    return encrypted_text

def read_from_key_file(path_to_key_file: str) -> str:
    key: str = ""
    try:
        with open(os.path.join(path_to_key_file), "r", encoding='utf-8') as file:
            file.__next__()
            while True:
                line: str = file.readline()

                if not line:
                    break

                key += line[0]
    except:
        logging.warning(f"The file {path_to_key_file} is not exist!", NameError)
    return key


def get_stats(encrypted_text: str, key: str) -> str:
    """Calculating the percentage of letters meeting and decoding the text"""
    stats: dict = dict()

    for letter in set(encrypted_text):
        stats[letter] = encrypted_text.count(letter)

    for stat in stats:
        stats[stat] = stats[stat] / len(encrypted_text)

    stats = dict(sorted(stats.items(), key=lambda x: x[1], reverse=True))
    keys = list(stats.keys())
    i = 0

    for stat in key:
        encrypted_text = encrypted_text.replace(keys[i], stat)
        i += 1

    return encrypted_text

def write_to_file(decrypted_text: str, path_to_decrypted_file: str) -> None:
    """Write the decrypted text and the encryption key to the file"""
    with open(os.path.join(path_to_decrypted_file), "w", encoding='utf-8') as file:
        file.write("Decrypted text: \n")
        file.write(decrypted_text)

def start_decrypt(path_to_text_file: str, path_to_key_file: str, path_to_decrypted_file: str) -> None:
    encrypted_text: str = read_from_text_file(path_to_text_file)
    key: str = read_from_key_file(path_to_key_file)
    decrypted_text = get_stats(encrypted_text, key)

    write_to_file(decrypted_text, path_to_decrypted_file)


