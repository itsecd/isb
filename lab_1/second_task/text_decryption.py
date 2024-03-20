import argparse
import sys
sys.path.insert(1, '../first_task')
from work_w_files import read_file, write_file, json_to_dict


def get_statistics(text: str) -> list[str]:
    """
    counts the number of letters in the text
    returns a list of letters sorted by descending frequency in the text
    """
    freq = {}
    for char in text:
        if char != '\n':
            freq[char] = freq[char] + 1 if char in freq else 1
    res = [
        elem[-1] for elem in sorted(
            freq.items(),
            key=lambda item: item[0],
            reverse=True)]

    return res


def get_new_text(text: str, key: dict) -> list[str]:
    """
    replaces letters in the source text according to the key
    """
    new_text=[] 
    for char in text.lower():
        if char.isalpha(): 
            new_text.append(char.replace(key[char], char).upper())
        else:
            new_text.append(char)
    for i in range(len(text)):
        if text[i].islower():
            new_text[i] = new_text[i].lower()
    return new_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Input file path,output file path, path to key")
    parser.add_argument("-i", "--input", help="Input file path", type=str)
    parser.add_argument("-o", "--output", help="output file path", type=str)
    parser.add_argument("-k", "--key", help="path to json key", type=str)
    args = parser.parse_args()
    write_file(
        args.output, get_new_text(
            read_file(
                args.input), json_to_dict(
                args.key)))
