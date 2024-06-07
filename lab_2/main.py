from functions import (
    read_json,
    frequency_test,
    runs_test,
    longest_run_test
)

from paths import SEQUENCES_PATH


def main():
    sequences = read_json(SEQUENCES_PATH)

    for key, sequence in sequences.items():
        print(f"Results for {key}:")
        
        frequency_value = frequency_test(sequence)
        print(f"  Frequency test P-value: {frequency_value}")

        runs_value = runs_test(sequence)
        print(f"  Runs test P-value: {runs_value}")

        longest_run_value = longest_run_test(sequence)
        print(f"  Longest run test P-value: {longest_run_value}")



if __name__ == "__main__":
    main()