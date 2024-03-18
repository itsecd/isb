import math
import os

from working_with_a_file import *


def frequency_test(path: str, path_write: str, key) -> None:
    b_sequence = read_json(path)
    try:
        sequence = [-1 if bit == "0" else 1 for bit in b_sequence.get(key)]
        s_n = sum(sequence)/math.sqrt(len(sequence))
        p_value = math.erfc(math.fabs(s_n) / math.sqrt(2))
        write_file(path_write,f'{p_value}\n')
    except Exception as e:
        print("Error when performing a frequency bitwise test:", e)


if __name__ == "__main__":
    # seq = "100101001010"
    # print(frequency_test(seq))

    frequency_test(os.path.join('sequence.json'), os.path.join('result.txt'), 'java')
    frequency_test(os.path.join('sequence.json'), os.path.join('result.txt'), 'c++')
