import argparse

def parsing() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки
    """
    parser = argparse.ArgumentParser(description="Шифрование текста с использованием шифра Виженера")
    parser.add_argument("_text", type=str, help="Текст для шифрования")
    parser.add_argument("_key", type=str, help="Ключ для шифрования")
    args = parser.parse_args()
    return args


text_1 = (
    "Посол Франции в Риме Блез де Виженер, познакомившись с трудами Тритемия, Белазо, Кардано, Порта, Альберти,"
    "также увлёкся криптографией. В 1585 году он написал «Трактат о шифрах», в котором излагаются основы криптографии. "
    "В этом труде он замечает: «Все вещи в мире представляют собой шифр. Вся природа является просто шифром и "
    "секретным письмом». Эта мысль была позднее повторена Блезом Паскалем — одним из основоположников теории "
    "вероятностей, а в XX веке и Норбертом Винером — «отцом кибернетики». По сути дела Виженер объединил подходы "
    "Тритемия, Беллазо, Порта к шифрованию открытых текстов, по существу не внеся в них ничего оригинального."
)
key_1 = "ибас"


def shifr(text, key):
    """
    Функция кодирования текста при помощи метода Вижинера
    :param text: шифруемый текст
    :param key: ключ шифрования
    :return: зашифрованный текст
    """
    key = key.lower()
    shifr_text = []
    key_len = len(key)

    #ASCII-код
    #ord("А") = 1040
    #ord("Я") = 1071
    #ord("а") = 1072
    #ord("я") = 1103

    int_key = [ord(i) for i in key]
    int_text = [ord(i) for i in text]

    #растянуть ключ на длину текста (не нужно)
    #key_repeat = (key*(---))

    for i in range (len(int_text)):
        if text[i].isalpha():
            #для ключей больше 32 символов необходимо %32 дабы зациклить
            if text[i].isupper():
                shift = (int_key[i % key_len] - 1040) % 32
                shifr_text.append(chr((int_text[i] + shift - 1040) % 32 + 1040))
            else:
                shift = (int_key[i % key_len] - 1072) % 32
                shifr_text.append(chr((int_text[i] + shift - 1072) % 32 + 1072))
        else:
            shifr_text.append(text[i])

    return ''.join(shifr_text)

def save_to_file(filename, data):
    """
    Сохраняет данные в файл
    :param filename: имя файла
    :param data: данные для сохранения
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(data)

def main():
    args = parsing()
    text = args._text
    key = args._key

    # Шифруем текст
    shifr_text = shifr(text, key)
    print("Зашифрованный текст: ")
    print(shifr_text)

    # Сохраняем исходный текст, зашифрованный текст и ключ в файлы
    save_to_file("original_text.txt", text)
    save_to_file("shifr_text.txt", shifr_text)
    save_to_file("key.txt", key)

    print("Данные сохранены в файлы: original_text.txt, encrypted_text.txt, key.txt")
if __name__ == "__main__":
    main()

