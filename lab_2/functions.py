import math
import mpmath

from constants import PI


def read_the_file(file_name: str) -> str:
    """
    This function converts text from a file to a string

    Args:
        file_name (str): path to the file

    Raises:
        Exception: an exception appears if the file can not be opened

    Returns:
        str: text from the file
    """
    try:
        text = ""
        with open(file_name, "r", encoding="UTF-8") as file:
            text = file.read()
        return text
    except Exception as e:
        raise Exception(f'Error here: {e}')


def frequency_bitwise_test(sequence: str) -> float:
    """
    This function implements a Frequency bitwise test.
    This test evaluates this proximity of the P-value to one

    Args:
        sequence (str): a string containing a sequence of 0 and 1

    Returns:
        float: the P-value for the frequency bitwise test
    """
    sum_seq = sum(list(map(lambda x: 1 if x == '1' else -1, sequence)))
    s = abs(sum_seq) / math.sqrt(len(sequence))
    p_value = math.erfc(s / math.sqrt(2))

    return p_value


def same_consecutive_bits_test(sequence: str) -> float:
    """
    This function sets how often the "1" is changed to "0" and back.

    Args:
        sequence (str): sequence of 0 and 1

    Returns:
        float: the P value for the test of the same consecutive bits
    """
    seq_len = len(sequence)

    proportion_of_units = sum(
        list(map(lambda x: 1 if x == '1' else 0, sequence))) / seq_len

    if abs(proportion_of_units - 1 / 2) < 2 / math.sqrt(seq_len):
        v = 0
        for i in range(seq_len - 1):
            v += 0 if sequence[i] == sequence[i + 1] else 1
        p_value = math.erfc((abs(v - 2 * seq_len * proportion_of_units * (1 - proportion_of_units))) /
                            (2 * math.sqrt(2 * seq_len) * proportion_of_units * (1 - proportion_of_units)))

        return p_value
    else:
        return 0


def longest_sequence_of_units_in_a_block_test(sequence: str) -> float:
    """
    This function calculates the P value for an incomplete gamma function
    by counting the number of blocks of length from 1 to 4
    and calculating the Xi-square

    Args:
        sequence (str): sequence of 0 and 1

    Returns:
        float: the P value for the test of the longest sequence of units in a block
    """
    blocks = [sequence[i:i + 8] for i in range(0, len(sequence), 8)]
    v = [0, 0, 0, 0]
    for block in blocks:
        max_count = 0
        count = 0
        for bit in block:
            count = count + 1 if bit == "1" else 0
            max_count = max(max_count, count)
        match max_count:
            case 0 | 1:
                v[0] += 1
            case 2:
                v[1] += 1
            case 3:
                v[2] += 1
            case _:
                v[3] += 1
    xi = 0
    for i in range(4):
        xi += pow(v[i] - 16 * PI[i], 2) / (16 * PI[i])
    p_value = mpmath.gammainc(3 / 2, xi / 2)

    return p_value
