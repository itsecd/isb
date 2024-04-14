import func
import paths
import file_operations

"""
Главная функция программы, которая выполняет шифрование и дешифрование текста.

- Читает и обрабатывает входные данные для шифрования.
- Шифрует текст с помощью перестановки символов.
- Записывает исходный текст, код для шифрования и зашифрованный текст в файлы.
- Читает зашифрованный текст из файла.
- Вычисляет частоту символов в зашифрованном тексте.
- Получает правильный текст, исправляя перестановку символов.
- Вычисляет частоту символов в исправленном тексте.
- Записывает дешифрованный текст в файл.

"""


def main():
    dict_ = file_operations.get_dict_from_json('settings.json')

    # Первая часть программы

    s, permutation = func.get_parse()
    permutation_arr = [a for a in permutation]
    new_s = func.encrypt(s, permutation_arr)
    file_operations.write_file(dict_['begin_text'], s)
    file_operations.write_file(dict_['code'], permutation)
    file_operations.write_file(dict_['encrypted_text'], new_s)

    # Вторая часть программы
    s2 = file_operations.read_file(dict_['encrypted_text2'])
    res = func.get_frequency(s2)
    for a in res:
        print(a)
    print()

    s_cor = func.get_correct_text(s2, dict_['before_perm'], dict_['after_perm'])

    res = func.get_frequency(s_cor)
    for a in res:
        print(a)
    print(s_cor)

    file_operations.write_file(dict_['decrypted_text2'], s_cor)


if __name__ == '__main__':
    main()
