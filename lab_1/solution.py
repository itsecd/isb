import os
import sys

import consts
import json_reader

import src.monoalphabetic_substitution as crypt


def main():
    """Main function of the program."""

    for folder in consts.FOLDERS_RESOURCE:

        try:
            path = os.path.join(folder, consts.NAME_INPUT_FILE)

            data = json_reader.read_json(path)

            path_alphabet = os.path.join(
                folder, data[consts.NAME_HEADER_FILE_ALPHABET])
            path_key = os.path.join(folder, data[consts.NAME_HEADER_FILE_KEY])
            path_text = os.path.join(
                folder, data[consts.NAME_HEADER_FILE_TEXT])

            with open(path_alphabet, 'r') as f:
                alphabet = f.read()

            with open(path_key, 'r') as f:
                key = f.read()

            with open(path_text, 'r') as f:
                text = f.read()

            encrypt = crypt.encrypt(alphabet, key, text)

            path_output = os.path.join(
                folder, data[consts.NAME_HEADER_FILE_OUTPUT])

            output = {
                data[consts.NAME_HEADER_FILE_ALPHABET].rsplit('.', 1)[0]: alphabet,
                data[consts.NAME_HEADER_FILE_KEY].rsplit('.', 1)[0]: key,
                data[consts.NAME_HEADER_FILE_TEXT].rsplit('.', 1)[0]: text,
                data[consts.NAME_HEADER_FILE_OUTPUT].rsplit('.', 1)[0]: encrypt
            }

            json_reader.write_json(output, path_output)

        except Exception as e:
            raise Exception(f"{folder}: {e}")


if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        print(e, file=sys.stderr)
