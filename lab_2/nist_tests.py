def perform_frequency_bit_test(binary_sequence: str) -> float:
    return (1 / (len(binary_sequence)**(0.5))) * \
        (binary_sequence.count('1') - binary_sequence.count('0'))


if __name__ == '__main__':
    print(perform_frequency_bit_test('101'))
