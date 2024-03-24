import math
SIZE = 128


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
    return math.erfc((binary_sequence.count('1') - binary_sequence.count('0'))/math.sqrt(SIZE)/math.sqrt(2))    


def perform_identical_consecutive_bits_test(binary_sequence: str) -> float:
    xie = binary_sequence.count('1')/SIZE
    if not (abs(xie-0.5) < (2 / math.sqrt(SIZE))):
        return 0.0
    v_n = 0
    for i in range(SIZE-1):
        if (binary_sequence[i] != binary_sequence[i+1]):
            v_n += 1
    return math.erfc(abs(v_n - 2*SIZE*xie*(1-xie))/(2*math.sqrt(2*SIZE)*xie*(1-xie)))


print(perform_identical_consecutive_bits_test('11000111111010000000111101010011101110011010001010101011111101110001011100101001000000011111101011111011001110101000011000110110'))
print(perform_frequency_bit_test('11000111111010000000111101010011101110011010001010101011111101110001011100101001000000011111101011111011001110101000011000110110'))
print(max_consecutive_ones('1101111101'))
