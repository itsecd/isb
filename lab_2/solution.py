import os
import sys

import json_reader
import src.tests as nist

from consts import HEADERS_GENERATE, NAME_INPUT_FILE, HEADER_FOLDER_RESOURCE, HEADER_OUTPUT_FILE


def main():
    """Main function of the program.

    This function reads a JSON file containing the paths to the input files and the output file.
    It then iterates over the input files, reads the contents of each file, and performs three statistical tests on the contents of the file.
    The results of the tests are stored in a dictionary, which is then written to the output file.

    Args:
        None

    Returns:
        None"""

    output = {}

    try:
        for type_generate in HEADERS_GENERATE:

            path = os.path.join(NAME_INPUT_FILE)
            data = json_reader.read_json(path)

            path_generate = os.path.join(
                data[HEADER_FOLDER_RESOURCE], data[type_generate])
            with open(path_generate, 'r') as f:
                generate = f.read()

            output[data[type_generate].rsplit('.', 1)[0]] = {
                "frequency_bit_test": nist.frequency_bitwise_test(generate),
                "identical_consecutive_bits_test": nist.consecutive_bits_test(generate),
                "longest_sequence_ones_block_eight_test": nist.longest_sequence_block_test(generate)
            }

        path_output = os.path.join(data[HEADER_OUTPUT_FILE])
        json_reader.write_json(output, path_output)

    except Exception as e:
        raise Exception(f"{type_generate}: {e}")


if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        print(e, file=sys.stderr)
