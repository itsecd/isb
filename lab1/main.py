from file_work import read_from_file, read_key, write_to_file
from task1.text_encryption import text_encryption


def main():
    try:
        text = read_from_file("task1/text.txt")
        key = read_key("task1/key.json")
        encrypted_text = text_encryption(text, key)
        write_to_file("task1/encrypted_text.txt", encrypted_text)
    except Exception as e:
        print(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()
