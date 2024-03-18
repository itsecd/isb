import math
import os

from working_with_a_file import *


def frequency_test(path: str, path_write: str, key: str) -> None:
    b_sequence = read_json(path)
    try:
        sequence = [-1 if bit == "0" else 1 for bit in b_sequence.get(key)]
        s_n = sum(sequence)/math.sqrt(len(sequence))
        p_value = math.erfc(math.fabs(s_n) / math.sqrt(2))
        write_file(path_write,f'{key} : {p_value}\n')
    except Exception as e:
        print("Error when performing a frequency bitwise test: ", e)


def same_bits_test(path: str, path_write: str, key: str) -> None:
    sequence = read_json(path)
    try:
        n = len(sequence.get(key))
        ones_count = sequence.get(key).count("1")
        p = ones_count / n
        if abs(p - 0.5) < (2 / math.sqrt(len(sequence.get(key)))):
            v = 0
            for bit in range(len(sequence.get(key)) - 1):
                if sequence.get(key)[bit] != sequence.get(key)[bit + 1]:
                    v += 1
            p_value = math.erfc(
                (abs(v - 2 * len(sequence.get(key)) * p * (1 - p)))
                / (2 * math.sqrt(2 * len(sequence.get(key))) * p * (1 - p)))
        else:
            p_value = 0
        write_file(path_write, f'{key} : {p_value}\n')
    except Exception as e:
        print("An error occurred when performing a test for the same consecutive bits: ", e)


if __name__ == "__main__":
    frequency_test(os.path.join('sequence.json'), os.path.join('result.txt'), 'java')
    frequency_test(os.path.join('sequence.json'), os.path.join('result.txt'), 'c++')

    same_bits_test(os.path.join('sequence.json'), os.path.join('result.txt'), 'java')
    same_bits_test(os.path.join('sequence.json'), os.path.join('result.txt'), 'c++')
