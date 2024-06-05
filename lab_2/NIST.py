import json
import math
import os
import logging

from scipy.special import erfc 
from mpmath import gammainc

from constants import PATH, LENGHT, PI_I


def read_json_file(filename: str) -> dict:
    """
    Считывает файл JSON и возвращает данные в виде словаря.

    Parameters: 
    Имя файла JSON для чтения.

    Returns: 
    Директория, содержащая данные, считанные из файла JSON.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Error while reading from file {filename}: {str(e)}")
        return {}


def frequency_bitwise_test(sequence: str) -> float:
    """
    Выполняет побитовую проверку частоты.

    Parameters: 
    Двоичная последовательность для тестирования.

    Returns: 
    P-значение, рассчитанное с помощью статистического теста.
    """
    try:
        N = len(sequence)
        sum = 0
        for bit in sequence:
            sum += bit.count('1') - bit.count('0')
        S_N = (1.0 / math.sqrt(N)) * abs(sum)
        P_value = erfc(S_N / math.sqrt(2))
        if P_value < 0 or P_value > 1:
            raise ValueError('Error: P should be in range [0, 1]')
        return P_value
    except Exception as e:
        print(f"Error: {e}")
        raise


def similar_sequences_test(sequence: str) -> float:
    """
    Выполняет проверку для одних и тех же последовательных битов.
    
    Parameters:
    Двоичная последовательность для тестирования.
    
    Returns:
    P-значение, рассчитанное с помощью статистического теста.
    """
    try:
        N = len(sequence)
        sum = 0
        sum = sequence.count("1")
        proportion_of_ones = sum / N
        if abs(proportion_of_ones - (0.5)) < 2 / math.sqrt(N):
            V_n = 0
            for i in range(0, N - 1):
                if (sequence[i] != sequence[i + 1]):
                    V_n += 1
            P_value = erfc(
                abs(V_n - 2 * N * proportion_of_ones * (1 - proportion_of_ones)) / (
                        2 * math.sqrt(2 * N) * proportion_of_ones * (
                        1 - proportion_of_ones)))
            if P_value < 0 or P_value > 1:
                raise ValueError('Error: P should be in range [0, 1]')
            return P_value
        else:
            return 0
    except Exception as e:
        print(f"Error: {e}")
        raise


def longest_ones_sequence_test(sequence: str):
    """
    Выполняет проверку самой длинной последовательности элементов в блоке.
    
    Parameters:
    Двоичная последовательность для тестирования.
    
    Returns:
    P-значение, рассчитанное с помощью статистического теста.
    """
    try:
        blocks = []
        for i in range(0, int(len(sequence) / LENGHT)):
            blocks.append(sequence[i * LENGHT: (i + 1) * LENGHT])
        V = [0, 0, 0, 0]
        for block in blocks:
            count = 0
            max_length = 0
            for bit in block:
                if bit == "1":
                    count += 1
                    max_length = max(max_length, count)
                else:
                    count = 0
            match max_length:
                case _ if max_length <= 1:
                    V[0] += 1
                case 2:
                    V[1] += 1
                case 3:
                    V[2] += 1
                case _ if max_length >= 4:
                    V[3] += 1
        Xi_in_2 = 0
        for i in range(0, 4):
            Xi_in_2 += pow((V[i] - 16 * PI_I[i]), 2) / (16 * PI_I[i])
        P_value = gammainc(1.5, (Xi_in_2 / 2))
        if P_value < 0 or P_value > 1:
            raise ValueError('Error: P should be in range [0, 1]')
        return P_value
    except Exception as e:
        print(f"Error: {e}")
        raise


def main() -> None:
    """
    Функция для вывода результатов.
    """
    absolute_path = os.path.abspath(os.getcwd())
    json_data = read_json_file(absolute_path + PATH)
    if json_data:
        cpp_sequence = json_data.get("cpp", "")
        java_sequence = json_data.get("java", "")
    if cpp_sequence and java_sequence:
        print("Tests for cpp:")
        print("Frequency bitwise test: P = " + str(frequency_bitwise_test(cpp_sequence)))
        print("Similar sequences test: P = " + str(similar_sequences_test(cpp_sequence)))
        print("Longest ones sequence test: P = " + str(longest_ones_sequence_test(cpp_sequence)))
        print("Tests for java:")
        print("Frequency bitwise test: P = " + str(frequency_bitwise_test(java_sequence)))
        print("Similar sequences test: P = " + str(similar_sequences_test(java_sequence)))
        print("Longest ones sequence test: P = " + str(longest_ones_sequence_test(java_sequence)))


if __name__ == "__main__":
    main()