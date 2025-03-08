from file_work import *
from task1.text_encryption import text_encryption


def main():
    text = read_from_file("task1/text.txt")
    key = read_key("task1/key.json")
    new_text = text_encryption(text, key)
    write_to_file("task1/encrypted_text.txt", new_text)


if __name__ == "__main__":
    main()
