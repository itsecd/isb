import json
import logging

from collections import Counter

from encryption import read_from_file, write_to_file, load_json_file


logging.basicConfig(level=logging.INFO)


def frequency_analysis(input_file: str, output_file: str) -> None:
    """
    Perform frequency analysis on the characters in the input file and write the results to the output file.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.

    Returns:
        None
    """
    try:
        original_text = read_from_file(input_file)
        character_count = Counter(original_text)
        total_characters = sum(character_count.values())
        character_frequency_percentage = {
            char: count / total_characters * 100 for char, count in character_count.items()}
        sorted_character_frequency = dict(sorted(
            character_frequency_percentage.items(), key=lambda item: item[1], reverse=True))
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(sorted_character_frequency, f,
                      ensure_ascii=False, indent=4)
        logging.info(
            "Frequency analysis results (sorted by frequency and represented as percentages) written to JSON file successfully.")
    except FileNotFoundError as e:
        logging.error(f"The input file '{input_file}' was not found.")
    except PermissionError as e:
        logging.error(f"Permission denied to access the file: {e}")
    except Exception as e:
        logging.error(f"An error occurred during frequency analysis: {e}")


def replace_keys_with_values(json_file: str, input_file: str, output_file: str) -> None:
    """
    Replace keys in the input text file with their corresponding values from the JSON file
    and write the modified text to the output file.

    Args:
        json_file (str): Path to the JSON file containing key-value pairs.
        input_file (str): Path to the input text file.
        output_file (str): Path to the output text file.

    Returns:
        None
    """
    try:
        json_data = load_json_file(json_file)
        original_text = read_from_file(input_file)
        for key, value in json_data.items():
            original_text = original_text.replace(key, value)
        write_to_file(output_file, original_text)
        logging.info(
            "Replacement completed successfully. Results written to the output file.")
    except FileNotFoundError as e:
        logging.error(f"The file '{e.filename}' was not found.")
    except PermissionError as e:
        logging.error(f"Permission denied to access the file: {e}")
    except Exception as e:
        logging.error(
            f"An error occurred during replacement: {e}")


if __name__ == "__main__":
    try:
        with open("lab_1/options.json", "r") as options_file:
            options = json.load(options_file)
        frequency_analysis(options['input_file'], 
                           options['output_file'])
        replace_keys_with_values(options['json_file'], 
                                 options['input_file'], 
                                 options['output_file2'])
    except FileNotFoundError as e:
        logging.error(f"The options file '{e.filename}' was not found.")
    except PermissionError as e:
        logging.error(f"Permission denied to access the file: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")