from math import erfc, pow, sqrt
from mpmath import gammainc
SIZE = 128
PI_I = {1: 0.2148, 2: 0.3672, 3: 0.2372, 4: 0.1875}


def max_consecutive_ones(string: str) -> int:
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
    return erfc((binary_sequence.count('1') - binary_sequence.count('0'))/sqrt(SIZE)/sqrt(2))    


def perform_identical_consecutive_bits_test(binary_sequence: str) -> float:
    xie = binary_sequence.count('1')/SIZE
    if not (abs(xie-0.5) < (2 / sqrt(SIZE))):
        return 0.0
    v_n = 0
    for i in range(SIZE-1):
        if (binary_sequence[i] != binary_sequence[i+1]):
            v_n += 1
    return erfc(abs(v_n - 2*SIZE*xie*(1-xie))/(2*sqrt(2*SIZE)*xie*(1-xie)))


def perform_longest_sequence_of_ones(binary_sequence: str, len_of_block = 8) -> list[str]:
    blocks = [binary_sequence[i:i+len_of_block] for i in range(0, SIZE, len_of_block)]
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
    x_2 = 0
    for i in range(1, len(PI_I)):
        x_2 += pow(v_i[i] - 16 * PI_I[i], 2) / (16 * PI_I[i])
    return gammainc(3/2, x_2/2)

print(perform_longest_sequence_of_ones('11000111111010000000111101010011101110011010001010101011111101110001011100101001000000011111101011111011001110101000011000110110'))
