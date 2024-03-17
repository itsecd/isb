import argparse
import logging
import os
from enum import Enum

from writer_and_reader import read_from_file, write_to_file


logging.basicConfig(level=logging.INFO)


class CaesarMode(Enum):
    ENCRYPT = 1
    DECRYPT = 2



rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'



def caesar_cipher(text: str, shift: int, mode: CaesarMode) -> str:
    """
    This function performs Caesar encryption or decryption based on the mode.
    """
    try:
        result_text = ''
        for char in text:
            if char in rus_alphabet:
                position = rus_alphabet.index(char)
                match mode:
                    case CaesarMode.ENCRYPT:
                        new_position = (position + shift) % len(rus_alphabet)
                    case CaesarMode.DECRYPT:
                        new_position = (position - shift) % len(rus_alphabet)
                result_text += rus_alphabet[new_position]
            else:
                result_text += char
        return result_text
    except Exception as ex:
        logging.error(f"Error: {ex}\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Caesar encryption.')
    parser.add_argument('--input_file',
                        type=str,
                        default=os.path.join('isb','lab_1','task1', 'input.txt'),
                        help='Input file path.')
    parser.add_argument('--shift',
                        type=int,
                        default=5,
                        help='Shift value.')
    parser.add_argument('--output_crypted',
                        type=str,
                        default=os.path.join('isb','lab_1','task1', 'encrypted_text.txt'),
                        help='Output crypted file path.')
    parser.add_argument('--output_decrypted',
                        type=str,
                        default=os.path.join('isb','lab_1','task1', 'decrypted_text.txt'),
                        help='Output decrypted file path.')

    args = parser.parse_args()

    try:
        text = read_from_file(args.input_file)
        encrypted_text = read_from_file(args.output_crypted)
        write_to_file(args.output_crypted, caesar_cipher(text, args.shift,  CaesarMode.ENCRYPT))
        write_to_file(args.output_decrypted, caesar_cipher(encrypted_text, args.shift, CaesarMode.DECRYPT))
    except Exception as ex:
        logging.error(f"Can't encrypt or decrypt text: {ex}")
