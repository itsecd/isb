import os
import logging
from working_with_a_file import open_file, write_text, saving_text

logging.basicConfig(level=logging.INFO)

RUS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def encryption(path: str, new_path: str, step: int) -> None:
    data = open_file(path)
    cipher_str = ""
    for i in data:
        if i == " ":
            cipher_str += i
            continue
        index = RUS.find(i)
        new_index = (index + step) % len(RUS)
        cipher_str += RUS[new_index]
    write_text(new_path, cipher_str)


def cipher_key(path: str, header: str, step: int) -> None:
    key = dict()
    for i in RUS:
        index = RUS.find(i)
        key[i] = RUS[(index + step) % len(RUS)]
    saving_text(key, path, header)


if __name__ == "__main__":

    encryption(
        os.path.join("lab_1", "purpose_1", "source_text.txt"),
        os.path.join("lab_1", "purpose_1", "encrypted_text.txt"),
        1,
    )

    cipher_key(
        os.path.join("lab_1", "purpose_1", "encryption_key.txt"),
        "Ключ к шифру императора Августа\n", 1
    )

