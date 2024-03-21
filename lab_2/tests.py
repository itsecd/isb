import json
import logging
import math
import mpmath
import os 


logging.basicConfig(level=logging.INFO)


def frequency_bitwise_test(data: str) -> float:
    sum_n = 0
    try:
        one = data.count("1")
        zero = data.count("0")
        sum_n = abs(one - zero)/math.sqrt(len(data))
        p_value = math.erfc(sum_n/math.sqrt(2))
        return p_value
    except Exception as ex:
        logging.error(f"Division by zero: {ex.message}\n{ex.args}\n")


def same_consecutive_bits(data: str) -> float:
    sum_n = 0
    v_n = 0
    try:
        sum_n = data.count("1")/len(data)
        comparison = abs(sum_n-0.5)
        module = 2/math.sqrt(len(data))
        if comparison >= module:
            return 0
        for j in range(len(data)-1):
            if data[j] != data[j+1]:
                v_n += 1
        p_value = math.erfc((abs(v_n-2*len(data)*sum_n*(1-sum_n))) /
                            (2*sum_n*(1-sum_n)*math.sqrt(2*len(data))))
        return p_value
    except Exception as ex:
        logging.error(f"Division by zero: {ex.message}\n{ex.args}\n")


def longest_sequence_of_units(data: str) -> float:
    block_length = 8
    n_i = [0.2148, 0.3672, 0.2305, 0.1875]
    value = [0]*4
    xi = 0
    try:
        for i in range(0, len(data), block_length):
            count = 0
            prev = 0
            for num in data[i:i+block_length]:
                if num != "0":
                    count += 1
                else:
                    if count > prev:
                        prev = count
                    count = 0
                max_num = max(count, prev)
            match max_num:
                case max_num if max_num <= 1:
                    value[0] += 1
                case 2:
                    value[1] += 1
                case 3:
                    value[2] += 1
                case max_num if max_num >= 4:
                    value[3] += 1
        for j in range(len(n_i)):
            xi += pow(value[j]-16*n_i[j], 2)/(16*n_i[j])
            p_value = mpmath.gammainc(3/2, xi/2)
        return p_value
    except Exception as ex:
        logging.error(f"Division by zero: {ex.message}\n{ex.args}\n")


if __name__ == "__main__":
    with open(os.path.join("lab_2", "settings.json"), "r") as file:
        settings = json.load(file)
    c = settings["c++"]
    java = settings["java"]
    with open(os.path.join("lab_2", "nist_result.txt"), "w", encoding="utf-8") as main:
        main.write(f"test_frequency_bitwise:\n\tc++: {frequency_bitwise_test(c)}\n\t")
        main.write(f"java: {frequency_bitwise_test(java)}\n")
        main.write(f"test_same_consecutive_bits:\n\tc++: {same_consecutive_bits(c)}\n\t")
        main.write(f"java: {same_consecutive_bits(java)}\n")
        main.write(f"test_longest_sequence_of_units:\n\tc++: {longest_sequence_of_units(c)}\n\t")
        main.write(f"java: {longest_sequence_of_units(java)}\n")
