import argparse

from work_w_files import read_file, write_file


def encrypt_w_caesar_cipher(text: list[str], shift=5) -> list[str]:
    """
    Each character shifts by 'shift' value
    """
    new_letters = []
    for char in text.replace('ё', 'е').replace('Ё', 'Е'):
        match char: 
            case char.islower():
                new_letters.append(
                    chr((ord(char) + shift - ord('а')) % 32 + ord('а')))
            case char.isupper():
                new_letters.append(
                    chr((ord(char) + shift - ord('А')) % 32 + ord('А')))
            case _:
                new_letters.append(char)
    return new_letters


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Input file path,output file path, shift")
    parser.add_argument("-i", "--input", help="Input file path", type=str)
    parser.add_argument("-o", "--output", help="output file path", type=str)
    parser.add_argument("-s", "--shift", help="shift", type=int)
    args = parser.parse_args()
    write_file(
        args.output,
        encrypt_w_caesar_cipher(
            read_file(
                args.input),
            args.shift))
