from math import erfc, pow, sqrt
from mpmath import gammainc
from work_w_files import json_to_dict

SETTINGS_JSON_FILE = 'settings.json'
PI_I = {1: 0.2148, 2: 0.3672, 3: 0.2305, 4: 0.1875}


def max_consecutive_ones(string: str) -> int:
    """
    finds the maximal sequence of '1'

    Args:
        string (str): binary sequence part

    Returns:
        int: max count of consecutive ones
    """
    max_c = 0
    cur_c = 0
    for char in string:
        if char == '1':
            cur_c += 1
            max_c = max(max_c, cur_c)
        else:
            cur_c = 0
    return max_c


def perform_frequency_bit_test(binary_sequence: str) -> float:
    """
    frequency bitwise test.

    Returns:
        float: p-value
    """
    return erfc((binary_sequence.count('1') - binary_sequence.count('0')
                 ) / sqrt(len(binary_sequence)) / sqrt(2))


def perform_identical_consecutive_bits_test(binary_sequence: str) -> float:
    """
    test for identical consecutive bits

    Returns:
        float: p-value
    """
    size_seq = len(binary_sequence)
    xie = binary_sequence.count('1') / size_seq
    if not (abs(xie - 0.5) < (2 / sqrt(size_seq))):
        return 0.0
    v_n = len([i for i in range(size_seq - 1)
              if binary_sequence[i] != binary_sequence[i + 1]])
    return erfc(abs(v_n - 2 * size_seq * xie * (1 - xie)) /
                (2 * sqrt(2 * size_seq) * xie * (1 - xie)))


def perform_longest_sequence_of_ones(
        binary_sequence: str, len_of_block: int) -> list[str]:
    """
    test for the longest sequence of units in a block.

    Returns:
        float: p-value
    """
    blocks = [binary_sequence[i:i + len_of_block]
              for i in range(0, len(binary_sequence), len_of_block)]
    v_i = {1: 0, 2: 0, 3: 0, 4: 0}
    for block in blocks:
        count_ones = max_consecutive_ones(block)
        match count_ones:
            case 0 | 1:
                v_i[1] += 1
            case 2:
                v_i[2] += 1
            case 3:
                v_i[3] += 1
            case 4 | 5 | 6 | 7 | 8:
                v_i[4] += 1
    x_2 = sum([pow((v_i[i] - 16 * PI_I[i]), 2) / (16 * PI_I[i])
              for i in range(1, len(PI_I)+1)])
    return gammainc(3 / 2, x_2 / 2)


if __name__ == '__main__':
    args = json_to_dict(SETTINGS_JSON_FILE)
    cpp_bs = json_to_dict(args['json'])['cpp']
    java_bs = json_to_dict(args['json'])['java']
    len_of_block = args['block']
    print('\n'.join([
        f'cpp binary sequence: {cpp_bs}',
        f'1st test: {perform_frequency_bit_test(cpp_bs)}',
        f'2nd test: {perform_identical_consecutive_bits_test(cpp_bs)}',
        f'3rd test: {perform_longest_sequence_of_ones(cpp_bs,len_of_block)}'
    ]))
    print('\n'.join([
        f'java binary sequence: {java_bs}',
        f'1st test: {perform_frequency_bit_test(java_bs)}',
        f'2nd test: {perform_identical_consecutive_bits_test(java_bs)}',
        f'3rd test: {perform_longest_sequence_of_ones(java_bs,len_of_block)}'
    ]))
