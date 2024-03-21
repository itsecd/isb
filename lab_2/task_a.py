from math import sqrt
from scipy.special import erfc


def main():
    """
    Проверить сгенерированные последовательность с помощью частотного побитового теста
    Returns:
        Если P<0.01: Вывод "Failed test"
        Если P>=0.01: Вывод "Passed test"
    """
    bits = '11001000001111111010100100100110101011101101101110100111111001000000000101000110110000001001011000111110001010110001111000101110'
    count_one = bits.count('1')
    count_zero = bits.count('0')
    total = count_one+count_zero*(-1)
    S = total/sqrt(128)
    P = erfc(S/sqrt(2))
    print(P)
    if (P < 0.01):
        print("Failed test")
    else:
        print( "Passed test")

if __name__ == "__main__":
    main()
