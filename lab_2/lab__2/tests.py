import math
import mpmath
import os

from working_with_a_file import *

PI = {0: 0.2148, 1: 0.3672, 2: 0.2305, 3: 0.1875}


def frequency_test(path: str, path_write: str, key: str) -> None:
    """
    Performs a frequency test on a binary sequence and writes the result to a file.

    Parameters
        path: the path to the JSON file containing the binary sequence.
        path_write: the path to write the result of the test.
        key: the key in the dictionary to the binary sequence.
    """
    b_sequence = read_json(path)
    try:
        sequence = [-1 if bit == "0" else 1 for bit in b_sequence.get(key)]
        s_n = sum(sequence) / math.sqrt(len(sequence))
        p_value = math.erfc(math.fabs(s_n) / math.sqrt(2))
        write_file(path_write, f'{key} : {p_value}\n')
    except Exception as e:
        print("Error when performing a frequency bitwise test: ", e)


def same_bits_test(path: str, path_write: str, key: str) -> None:
    """
    Performs a test for the same consecutive bits and writes the result to a file.

    Parameters
        path: the path to the JSON file containing the binary sequence.
        path_write: the path to write the result of the test.
        key: the key in the dictionary to the binary sequence.
    """
    sequence = read_json(path)
    try:
        n = len(sequence.get(key))
        ones_count = sequence.get(key).count("1")
        zita = ones_count / n
        if abs(zita - 0.5) < (2 / math.sqrt(len(sequence.get(key)))):
            v = 0
            for bit in range(len(sequence.get(key)) - 1):
                if sequence.get(key)[bit] != sequence.get(key)[bit + 1]:
                    v += 1
            numerator = abs(v - 2 * n * zita * (1 - zita))
            denominator = 2 * math.sqrt(2 * n) * zita * (1 - zita)
            p_value = math.erfc(numerator / denominator)
        else:
            p_value = 0
        write_file(path_write, f'{key} : {p_value}\n')
    except Exception as e:
        print("An error occurred when performing a test for the same consecutive bits: ", e)


def longest_run_ones_test(path: str, path_write: str, key: str) -> None:
    """
    Performs a test for the longest sequence of ones in the block and writes the result to a file.

    Parameters
        path: the path to the JSON file containing the binary sequence.
        path_write: the path to write the result of the test.
        key: the key in the dictionary to the binary sequence.
    """
    sequence = read_json(path)
    try:
        len_sequence = len(sequence.get(key))
        block_max_size = 8
        blocks = [sequence.get(key)[i:i + block_max_size] for i in range(0, len_sequence, block_max_size)]
        v = {1: 0, 2: 0, 3: 0, 4: 0}
        for block in blocks:
            max_count = 0
            count = 0
            for bit in block:
                count = count + 1 if bit == "1" else 0
                max_count = max(max_count, count)
            match max_count:
                case 0 | 1:
                    v[1] += 1
                case 2:
                    v[2] += 1
                case 3:
                    v[3] += 1
                case _:
                    v[4] += 1
        xi_square = 0
        for i in range(4):
            xi_square += pow(v[i + 1] - 16 * PI[i], 2) / (16 * PI[i])
        value = mpmath.gammainc(3 / 2, xi_square / 2)
        write_file(path_write, f'{key} : {value}\n')
    except Exception as e:
        print("An error occurred while performing the test for the longest sequence of ones in the block: ", e)


if __name__ == "__main__":
    setting = read_json("setting.json")
    p = setting["from"]
    pw = setting["to"]

    frequency_test(p, pw, "java")
    frequency_test(p, pw, "c++")

    same_bits_test(p, pw, "java")
    same_bits_test(p, pw, "c++")

    longest_run_ones_test(p, pw, "java")
    longest_run_ones_test(p, pw, 'c++')
