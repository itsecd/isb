import argparse
import functions

def create_parser()->tuple:
    """
    Gets a path to key, decrypted and encrypted texts for task1 and key, encrypted and decrypted texts for task2
    :return: tuple of 6 strings
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key",type=str,help="key")
    parser.add_argument("input_text",type=str,help="path to the original text")
    parser.add_argument("encrypted_text", type=str, help="path where result for task1 will be saved")
    parser.add_argument("task2_key", type=str, help="path to the key for task2")
    parser.add_argument("task2_encrypted", type=str, help="path to encrypted text for task2")
    parser.add_argument("task2_result", type=str, help="path where result for task2 will be saved")
    args=parser.parse_args()
    return args.key, args.input_text, args.encrypted_text, args.task2_key, args.task2_encrypted, args.task2_result


def main():
    try:
        key = functions.read_file(create_parser()[0])
        text = functions.read_file(create_parser()[1])
        result = create_parser()[2]

        encrypted_text = functions.tritemius_cipher(text, key)
        functions.write_file(result, encrypted_text)

        task2_key = create_parser()[3]
        original_text_task2 = functions.read_file(create_parser()[4])
        functions.get_frequency(original_text_task2)

        task2_decrypted = create_parser()[5]

        task2_res = functions.get_decryption(original_text_task2, functions.get_key(task2_key))
        functions.write_file(task2_decrypted, task2_res)
    except Exception as e:
        print(f"An error occurred while accessing the directory: {e} ")


if __name__ == "__main__":
    main()