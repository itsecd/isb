import json
import logging
import math
import os


from mpmath import gammainc

logging.basicConfig(filename="lab_2/report.log", filemode="a", level=logging.INFO)

PI = {"v1": 0.2148, "v2": 0.3672, "v3": 0.2305, "v4": 0.1875}


def freq_bit_test(sequence: str) -> float:
    """
    The function allows you to perform a bit frequency test for a sequence

    Args:
        sequence (str): binary sequence
    
    Returns:
        float: calculated p-value

    Raises:
        Any error that occurs while the function is running
    """
    bits = {"0": -1, "1": 1}
    try:
        sum_value = sum(bits.get(bit, 0) for bit in sequence)
        p_value = math.erfc(abs(sum_value) / (math.sqrt(2 * len(sequence))))
    except Exception as e:
        logging.error(f"Problems in the frequency bit test: {e}")
    logging.info("Frequency bit test passed successfully")
    return p_value


def search_identical_bits(sequence: str) -> float:
    """
    The function allows you to test for identical consecutive bits

    Args:
        sequence (str): binary sequence
    
    Returns:
        float: calculated p-value

    Raises:
        Any error that occurs while the function is running
    """
    try:
        share = sum(int(bit) for bit in sequence) / len(sequence)
        if abs(share - 0.5) < (2 / math.sqrt(len(sequence))):
            v = 0
            for bit in range(len(sequence) - 1):
                if sequence[bit] != sequence[bit + 1]:
                    v += 1
            p_value = math.erfc(
                (abs(v - 2 * len(sequence) * share * (1 - share)))
                / (2 * math.sqrt(2 * len(sequence)) * share * (1 - share)))
        else:
            p_value = 0
        logging.info("Test 2 work")
    except Exception as e:
        logging.error("Problem is in the test for identical bits")
    return p_value


def longest_sequence_test(sequence: str) -> float:
    """
    The function allows you to test for the longest sequence of ones in a block

    Args:
        sequence (str): binary sequence
    
    Returns:
        float: calculated p-value

    Raises:
        Any error that occurs while the function is running
        LookupError: catches an error when creating statistics
    """
    try:
        blokcs = [sequence[i : i + 8] for i in range(0, len(sequence), 8)]
        statistics = {"v1": 0, "v2": 0, "v3": 0, "v4": 0}
        for block in blokcs:
            max_counter = 0
            counter = 0
            for bit in block:
                if bit == "1":
                    counter += 1
                else:
                    max_counter = max(max_counter, counter)
                    counter = 0
            max_counter = max(max_counter, counter)    
            match max_counter:
                case 0:
                    statistics["v1"] += 1
                case 1:
                    statistics["v1"] += 1
                case 2:
                    statistics["v2"] += 1
                case 3:
                    statistics["v3"] += 1
                case _:
                    statistics["v4"] += 1
        logging.info("Statistics collected")
        chi_squared_distribution = 0
        for v in statistics:
            chi_squared_distribution += (pow(statistics[v] - 16 * PI[v], 2)) / (
                16 * PI[v]
            )
        p_value = gammainc(3 / 2, chi_squared_distribution / 2)
    except (Exception, LookupError) as e:
        logging.error(f"Problem calculating chi-square and gamma function: {e}")
    return p_value


def save_results(result: float, path: str) -> None:
    """
    Saves the results to the specified path

    Args:
        results (float): Saved result
        path (str): path where you want to save the result

    Returns:
        None

    Raises:
        Any exceptions that occur during the file saving process.
    """
    try:
        with open(path, "a+", encoding="utf-8") as f:
            f.write(str(result))
        logging.info("Results uploaded successfully")
    except Exception as e:
        logging.error(f"Error in saving results: {e}")


if __name__ == "__main__":
    try:
        with open(os.path.join("lab_2", "settings.json"), "r", encoding="utf-8") as json_f:
            settings = json.load(json_f)
    except Exception as e:
        logging.error("Error loading json file")
    save_results(
        freq_bit_test(settings["genc"]),
        os.path.join(settings["folder"], settings["file"]),
    )
    save_results(
        freq_bit_test(settings["genj"]),
        os.path.join(settings["folder"], settings["file"]),
    )
    logging.info('Frequency bit test in C++: %f\n', freq_bit_test(settings["genc"]))
    logging.info('Frequency bit test in Java: %f\n', freq_bit_test(settings["genj"]))
    save_results(
        search_identical_bits(settings["genc"]),
        os.path.join(settings["folder"], settings["file"]),
    )
    save_results(
        search_identical_bits(settings["genj"]),
        os.path.join(settings["folder"], settings["file"]),
    )
    logging.info('Test for identical consecutive bits in C++: %f\n', search_identical_bits(settings["genc"]))
    logging.info('Test for identical consecutive bits in Java: %f\n', search_identical_bits(settings["genj"]))
    save_results(
        longest_sequence_test(settings["genc"]),
        os.path.join(settings["folder"], settings["file"]),
    )
    save_results(
        longest_sequence_test(settings["genj"]),
        os.path.join(settings["folder"], settings["file"]),
    )
    logging.info('Test for the longest sequence of ones in a block in C++: %f\n', longest_sequence_test(settings["genc"]))
    logging.info('Test for the longest sequence of ones in a block in Java: %f\n', longest_sequence_test(settings["genj"]))
    
