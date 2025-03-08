import math
import re


def frequency_test(sequence):
    """
    Проверяет, что количество нулей и единиц в последовательности примерно одинаково
    :param sequence: Передаваемая последовательность (бит)
    :return: P-значение (если P->0 значит seq предсказуема, P->1 - seq случайна)
    """
    n = len(sequence)
    ones = sequence.count('1')
    zeros = sequence.count('0')
    sum = ones - zeros;
    S_n = abs(sum) / (n ** 0.5)
    p_value = math.erfc(S_n / (2 ** 0.5))
    return p_value


def runs_test(sequence):
    """
    Проверяет, что количество последовательностей одинаковых битов соответствует ожидаемому
    :param sequence: Передаваемая последовательность (бит)
    :return: P-значение
    """
    n = len(sequence)
    ones = sequence.count('1')
    zeros = sequence.count('0')

    prop = ones / n #Доля единиц в seq
    tau = 2 / (n ** 0.5)
    if abs(prop - 0.5) >= tau:
        return 0.0

    runs = 1 #Знакоперемены
    for i in range(1, n):
        if sequence[i] != sequence[i - 1]:
            runs += 1

    p_value = math.erfc(abs(runs - 2 * n * prop * (1 - prop)) /
                        (2 * (2 * n)** 0.5 * prop * (1 - prop)) )
    return p_value


def longest_run_of_ones_test_needCalculatorToCount(sequence, block_size=128):
    """
    Тест на самую длинную последовательность единиц в блоке
    :param sequence: Передаваемая последовательность (бит)
    :param block_size: Длина последовательности - 128, (блоков - 8)
    :return: Хи-квадрат/2 для калькулятора p_value
    """
    n = len(sequence)
    num_blocks = n // block_size
    if num_blocks == 0:
        return 0.0

    # Разделение последовательности на блоки
    blocks = []
    for i in range(num_blocks):
        start = i * block_size
        end = (i + 1) * block_size
        block = sequence[start:end]
        blocks.append(block)

    # Поиск максимальной длины последовательности единиц в каждом блоке
    max_runs = []
    for block in blocks:
        runs = re.findall('1+', block) #регулярное выражение: одна и более единица
        if runs:
            max_run = max(len(run) for run in runs)
        else:
            max_run = 0
        max_runs.append(max_run)


    # Ожидаемые значения для block_size = 128
    expected_pi = [0.2148, 0.3672, 0.2305, 0.1875]
    if block_size == 128:
        V = [0, 0, 0, 0, 0]
        for run in max_runs:
            if run <= 4:
                V[0] += 1
            elif run == 5:
                V[1] += 1
            elif run == 6:
                V[2] += 1
            elif run == 7:
                V[3] += 1
            else:
                V[4] += 1

        chi_square = sum((V[i] - num_blocks * expected_pi[i]) ** 2 / (num_blocks * expected_pi[i]) for i in range(4))
        #p_value = math.igamc(1.5, chi_square/2)
        #return p_value

        return chi_square/2
    else:
        return 0.0



# Загрузка сгенерированной последовательности
with open("C:\OIB_lab2\lab_2\Task_1\Random_seq_cpp.txt", "r") as file:
    sequence_cpp = file.read().strip()

with open("C:\OIB_lab2\lab_2\Task_1\Random_seq_java.txt", "r") as file:
    sequence_java = file.read().strip()

# Применение тестов
p_value_freq_cpp = frequency_test(sequence_cpp)
p_value_runs_cpp = runs_test(sequence_cpp)
NEED_TO_CALCULATE_cpp = longest_run_of_ones_test_needCalculatorToCount(sequence_cpp)

p_value_freq_java = frequency_test(sequence_java)
p_value_runs_java = runs_test(sequence_java)
NEED_TO_CALCULATE_java = longest_run_of_ones_test_needCalculatorToCount(sequence_java)

# Вывод результатов
print("C++ Sequence:")
print(f"Frequency Test p-value: {p_value_freq_cpp}")
print(f"Runs Test p-value: {p_value_runs_cpp}")
print(f"Longest Run of Ones Test p-value: {NEED_TO_CALCULATE_cpp}")
#Проверил на калькуляторе:
#Regularized upper incomplete gamma function: 0.63205382


print("\nJava Sequence:")
print(f"Frequency Test p-value: {p_value_freq_java}")
print(f"Runs Test p-value: {p_value_runs_java}")
print(f"Longest Run of Ones Test p-value: {NEED_TO_CALCULATE_java}")
#Проверил на калькуляторе:
#Regularized upper incomplete gamma function: 0.63205382