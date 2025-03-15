from file_work import read_from_file, read_data, write_to_file, save_data
from task1.text_encryption import text_encryption, make_dict_upper
from task2.frequency_analysis import frequency_count, sort_dict


def main():
    try:
        # task1
        text = read_from_file("task1/text.txt")
        key = read_data("task1/key.json")
        encrypted_text = text_encryption(text, key)
        write_to_file("task1/encrypted_text.txt", encrypted_text)

        # task2
        cod25 = read_from_file("task2/cod25.txt")
        save_data("task2/frequency.json", sort_dict(frequency_count(cod25)))
        key_cod25 = read_data("task2/key.json")
        decrypted_text = text_encryption(cod25, key_cod25)
        write_to_file("task2/decrypted_text.txt", decrypted_text)
    except Exception as e:
        print(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()
