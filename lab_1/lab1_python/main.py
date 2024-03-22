def encrypt(text: str, permutation: list[str]) -> str:
    """
    text: str - текст, который будет зашифровываться
    permutation: list[str] - перестановка букв
    new_s: str - зашифрованный текст
    Данная функция осуществляет шифроку текста text с помощью перестановки permutation
    """
    new_s = ""
    for i in range(len(text)):
        if text[i] not in letters_arr:
            new_s += s[i]
        else:
            index = letters.index(text[i])
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
        file_write.close()


s = input('Введите текст, который вы хотите зашифровать (заглавные буквы кириллицы и пробел): ')
permutation = input('Введите ключ подстановки (32 заглавных буквы кириллицы и пробел): ')

letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
letters_arr = [a for a in letters]

permutation_arr = [a for a in permutation]

new_s = encrypt(s, permutation_arr)

write_file('begin_text.txt', s)
write_file('code.txt', permutation)
write_file('encrypted_text.txt', new_s)
