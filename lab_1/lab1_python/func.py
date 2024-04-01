import argparse

letters_arr = [a for a in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ']


def get_parse():
    """
    Функция парсит два аргумента:
    -t -- текст для зашифровки
    -p -- перестановка букв
    Функция возвращает кортеж: (текст, перестановка)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', dest='text', help='Текст для зашифровки', type=str)
    parser.add_argument('-p', dest='permutation', help='Перестановка букв', type=str)
    args = parser.parse_args()
    return args.text, args.permutation


def encrypt(text: str, permutation_arr: list[str]) -> str:
    """
    text: str - текст, который будет зашифровываться
    permutation: list[str] - перестановка букв
    new_s: str - зашифрованный текст
    Данная функция осуществляет шифроку текста text с помощью перестановки permutation
    """
    new_s = ""
    for i in range(len(text)):
        if text[i] not in letters_arr:
            new_s += text[i]
        else:
            index = letters_arr.index(text[i])
            new_symbol = permutation_arr[index]
            new_s += new_symbol
    return new_s


def write_file(pathname: str, string: str) -> None:
    """
    pathname - путь к файлу, в которую идёт запись
    string - записываемая строка
    Данная функция осуществляет запись строки string в файл по пути pathname
    """
    with open(pathname, 'w', encoding='utf-8') as file_write:
        file_write.write(string)


def read_file(pathname: str) -> str:
    s = ''
    with open(pathname, 'r', encoding='utf-8') as file_read:
        s = file_read.read()
    return s


def get_frequency(string: str) -> list[str, float]:
    """
        str - строка с шифром
        list - список частотности
        Данная функция создает список с частотой каждого символа
    """
    len_s = len(string)
    res = dict()
    for symbol in string:
        if symbol not in res:
            res[symbol] = 1
        else:
            res[symbol] += 1
    for item in res:
        res[item] /= len_s
    res = [[item, res[item]] for item in res]
    res.sort(key=lambda x: x[1])
    return reversed(res)


def replace_symbols(s, f_symbol, s_symbol):
    """
        s - рабочая строка
        f_symbol - первый символ замены
        s_symbol - второй символ замены
        Данная функция меняет два символа местами
        """
    new_s = ''
    for symbol in s:
        if symbol == f_symbol:
            new_s += s_symbol
        elif symbol == s_symbol:
            new_s += f_symbol
        else:
            new_s += symbol
    return new_s


def get_correct_text(s):
    first_sym = 'ЙФШЫ М2ОЕ>ДРИУЧКХЩЬ5Л1ЪА4Пrt7<8'
    second_sym = 'ТЙФШЫ МВОЕНДСИУЮКХЩБЯЛЦЬАГПРЖЧЗ'
    for i in range(len(first_sym)):
        s = replace_symbols(s, first_sym[i], second_sym[i])
    return s
