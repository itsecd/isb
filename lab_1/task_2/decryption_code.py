import json


def frequency_analysis(file_path: str) -> dict:
    """
    Perform frequency analysis on the characters in a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        list: A list of tuples containing characters and their relative frequencies, sorted in descending order of frequency.
    """
    frequencies = {}
    total_chars = 0
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for char in file.read():
                if char != "\n":
                    total_chars += 1
                    frequencies[char] = frequencies.get(char, 0) + 1
        relative_frequencies = {char: freq / total_chars for char, freq in frequencies.items()}
        sorted_frequencies = sorted(relative_frequencies.items(), key=lambda x: x[1], reverse=True)
        return dict(sorted_frequencies)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def write_file(path: str, data: dict) -> None:
    """
    Write frequency analysis to a file.

    Args:
        path (str): The path to the file.
        data (list): The data to be written to the file.
    """
    try:
        with open(path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def read_file(file_path: str) -> dict:
    """
    Write data to a file.

    Args:
        path (str): The path to the file.
        data (list): The data to be written to the file.
    """
    frequency_dict = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            frequency_dict = json.load(file)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return frequency_dict


def key_decryption(frequency_text_path: str, standard_frequency_path: str, output_file: str) -> None:
    """
    Generate a decryption key based on frequency analysis.

    Args:
        frequency_text_path (str): The path to the file containing frequency data of encrypted text.
        standard_frequency_path (str): The path to the file containing standard frequency data.
        output_file (str): The path to save the generated decryption key.
    """
    try:
        frequency_text = read_file(frequency_text_path)
        standard_frequency = read_file(standard_frequency_path)
        key = {}
        for char, freq_text in frequency_text.items():
            closest_char = min(standard_frequency, key=lambda x: abs(float(freq_text) - float(standard_frequency[x])))
            key[char] = closest_char

        write_file(output_file, list(key))
    except Exception as e:
        print(f"An error occurred {str(e)}")


def decryption(input_file_path: str, output_file_path: str, key_path: str) -> None:
    """
    Decrypt an encrypted text using a decryption key.

    Args:
        input_file_path (str): The path to the encrypted text file.
        output_file_path (str): The path to save the decrypted text.
        key_path (str): The path to the decryption key file.
    """
    try:
        with open(key_path, "r", encoding="utf-8") as json_file:
            decryption_key = json.load(json_file)
        with open(input_file_path, 'r', encoding='utf-8') as input_file, \
        open(output_file_path, 'w', encoding='utf-8') as output_file:
            for line in input_file:
                decrypted_line = ''.join(decryption_key.get(char, char) for char in line.strip())
                output_file.write(decrypted_line + '\n')
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    with open('settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
    data = frequency_analysis(settings["input_file_path"])
    write_file(settings["frequency_text_path"], data)
    #key_decryption(settings["frequency_text_path"], settings["standard_frequency_path"], settings["decryption_key_path"])
    #decryption(settings["input_file_path"], settings["output_file_path"], settings["decryption_key_path"])
