from argparse import Namespace
from idlelib.iomenu import encoding
import argparse

from  vigenere import *


def parser_create() -> Namespace:
    """
    parser

    :return: parsed arguments
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('input_text', type=str, help='Name of input text file')
    parser.add_argument('output_text', type=str, help='Name of output text file')
    parser.add_argument('key_filename', type=str, help='Filename containing the key')

    return parser.parse_args()


def read_text(filename: str) -> str:
    """
    Text reading function.

    :return: The input text.
    """
    with open(filename, 'r', encoding='utf-8') as text:
        return text.read()


def write_encrypted_text(filename: str, text: str) -> None:
    """
    Function to write text to file.

    """

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)


def main():

    args = parser_create()

    key = read_text(args.key)
    input_text = read_text(args.input_text)
    encrypted_text = vigenere_cipher_encrypt(input_text, key)
    output_text = args.output_text

    write_encrypted_text(output_text, encrypted_text)


if __name__ == "__main__":
     main()