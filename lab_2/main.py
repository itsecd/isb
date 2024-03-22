from NIST_tests import *
from work_with_file import *


if __name__ == "__main__":
    path_to_file_with_sequences = r'sequences.json'
    key1 = "C++"
    key2 = "Java"
    sequence = read_json(path_to_file_with_sequences)
    path_to_output_file = 'result.md'

    data = (f"Частотный побитовый тест (C++): {frequency_bitwise_test(sequence[key1])}\n"
        f"Тест на одинаковые подряд идущие биты (C++): {same_consecutive_bits_test(sequence[key1])}\n"
        f"Тест на самую длинную последовательность единиц в блоке (C++): {longest_sequence_test(sequence[key1])}\n"
        f"Частотный побитовый тест (Java): {frequency_bitwise_test(sequence[key2])}\n"
        f"Тест на одинаковые подряд идущие биты (Java): {same_consecutive_bits_test(sequence[key2])}\n"
        f"Тест на самую длинную последовательность единиц в блоке (Java): {longest_sequence_test(sequence[key2])}\n")

    write_to_file(data, path_to_output_file)