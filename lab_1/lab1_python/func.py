import argparse

letters_arr = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '


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
    try:
        with open(pathname, 'w', encoding='utf-8') as file_write:
            file_write.write(string)
    except FileNotFoundError:
        print('Создан файл с названием: ', pathname)


def read_file(pathname: str) -> str:
    """
        pathname - путь к файлу, который нужно прочитать
        Данная функция считывает содержимое файла по пути pathname
    """
    s = ''
    try:
        with open(pathname, 'r', encoding='utf-8') as file_read:
            s = file_read.read()
    except FileNotFoundError:
        print("Файл не найден.")
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
        match symbol:
            case str(f_symbol):
                new_s += s_symbol
            case str(s_symbol):
                new_s += f_symbol
            case _:
                new_s += symbol
    return new_s


def get_correct_text(s, first_sym, second_sym):
    """
        s - входная строка
        f_symbol - первый символ замены
        s_symbol - второй символ замены
        Данная функция заменяет символы в строке на основе сопоставлений
    """
    for i in range(len(first_sym)):
        s = replace_symbols(s, first_sym[i], second_sym[i])
    return s


def get_dict_from_md(pathname):
    """
        pathname - путь к файлу
        Данная функция преобразовывает содержимое файла Markdown в словарь
    """
    temp_arr = []
    with open(pathname, 'r', encoding='utf-8') as file_read:
        temp_arr = file_read.readlines()
    for i in range(len(temp_arr)):
        temp_arr[i] = temp_arr[i].rstrip('\n')
        temp_arr[i] = temp_arr[i].split(': ')
    res = {a[0]: a[1] for a in temp_arr}
    return res


if __name__ == '__main__':
    get_dict_from_md('paths2.md')
