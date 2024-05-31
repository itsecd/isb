import argparse

from functions import read_the_file, frequency_bitwise_test, same_consecutive_bits_test, longest_sequence_of_units_in_a_block_test


def main() -> None:
    parser = argparse.ArgumentParser(description="Pseudorandom sequences")
    parser.add_argument('cxx', type=str, help='Sequence on CXX')
    parser.add_argument('java', type=str, help='Sequence on Java')

    args = parser.parse_args()

    sequence_cxx = read_the_file(args.cxx)
    print(f"C++ sequence: {sequence_cxx}")
    print(f"1st test: {frequency_bitwise_test(sequence_cxx)}")
    print(f"2nd test: {same_consecutive_bits_test(sequence_cxx)}")
    print(
        f"3rd test: {longest_sequence_of_units_in_a_block_test(sequence_cxx)}")

    sequence_java = read_the_file(args.java)
    print(f"Java sequence: {sequence_java}")
    print(f"1st test: {frequency_bitwise_test(sequence_java)}")
    print(f"2nd test: {same_consecutive_bits_test(sequence_java)}")
    print(
        f"3rd test: {longest_sequence_of_units_in_a_block_test(sequence_java)}")


if __name__ == "__main__":
    main()

# python lab_2\\NIST_tests.py lab_2\\sequences\\cxx.txt lab_2\\sequences\\java.txt
