task_text = ("И7уОПЁХХQU=Ё<Ж7ПUNRО9уQПNОИ7ЖЁХЯQUПДОИ=ЁХQЖQЖЁQО"
            "уТДО=ЯПiЁZ=71РЁОU7%7ОYQОПЯХ7%7ОРТR<ЯОР7U7=КХОЙКТ7О9ЯiЁZ"
            "=71ЯЖ7ОИ7ПТЯЖЁQ"
            "7ПЖ71ЖКQОU=QЙ71ЯЖЁДОРОПЁХХQU=Ё<ЖКХОЯТ%7=ЁUХЯХОUЯР"
            "ЁQОПUЯUЁПUЁ<QПРЁюО9ЯР7Ж7ХQ=Ж7ПUQ3О1ОiЁZ=sQХ7ХОП77ЙF"
            "QЖЁЁО7ПUЯ1ЯUNПДОЖQОу7ТYЖ7ОТЁЖQ3Ж7ПUЁОU7YQ"
            "ПЁХХQU=Ё<ЖКQОПЁПUQХКО1ОП17RО7<Q=QуNОуQТДUОЖЯОЙТ7<ЖКQ"
            "ОЁОИ7U7<ЖКQ"
            "О1ОЙТ7<ЖКюОПЁПUQХЯюОiЁZ=71ЯЖЁQО1КИ7ТЖДQUПДОUЯРОЁПю"
            "7уЖ7QОП77ЙFQЖЁQОуQТЁUПДОЖЯОЙТ7РЁОЯО9ЯUQХОРЯYуК3ОЁ9"
            "ОЖЁюОР7уЁ=sQUПДОПОЁПИ7ТN971ЯЖЁQХО7И=QуQТQЖЖ7%7ОРТR<Я"
            "1ОИ7U7<ЖКюОЯТ%7=ЁUХЯюОZ7=ХЁ=sQUПДОUЯРОЖЯ9К1ЯQХЯДО1"
            "Кю7уЖЯДО%ЯХХЯООЁО1ОИ=7гQППQОQQО%QЖQ=Ё=71ЯЖЁДО7ПsF"
            "QПU1ТДQUПДОiЁZ=71ЯЖЁQОИ7ПТЯЖЁД"
            "U7ОQПUNО7ЖЯОИ7U7Р7ХОЖЯРТЯуК1ЯQUПДОЖЯОЁПю7уЖЁР"
            "1Ою7уQОПЁХХQU=Ё<Ж7%7ОiЁZ=71ЯЖЁДОуТДОИ7уПUЯЖ71РЁОЁОИ"
            "Q=QПUЯЖ71РЁОЁПю7уЖКюОуЯЖЖКюО9ЯуQ3ПU1sRUПДОПТ7YЖКQ"
            "ОХЖ7%7s=71ЖQ1КQОЯТ%7=ЁUХК"
            "GUЁюОs=71ЖQ3ООХ7YQUОЙКUNО7<QЖNОХЖ7%7ОЁОРЯYуК3ОП7О"
            "П17ЁХОРТR<7Х")


rus_freq = {
    'о': 0.0965, 'и': 0.0753, 'е': 0.0723, 'а': 0.0648, 'н': 0.0618,
    'т': 0.0616, 'с': 0.0520, 'р': 0.0407, 'в': 0.0393, 'м': 0.0298,

    'л': 0.0294, 'д': 0.0270, 'я': 0.0264, 'к': 0.0260, 'п': 0.0248,
    'з': 0.0160, 'ы': 0.0157, 'ь': 0.0151, 'у': 0.0133, 'ч': 0.0117,

    'ж': 0.0107, 'г': 0.0099, 'х': 0.0087, 'ф': 0.0073, 'й': 0.0069,
    'ю': 0.0067, 'б': 0.0067, 'ц': 0.0050, 'ш': 0.0042, 'щ': 0.0036,
    'э': 0.0024, 'ъ': 0.0004, 'ё': 0.0004, ' ': 0.1287
}


def write_to_file(filename, content):
    """
    Записывает содержимое в файл.
    :param filename: имя файла
    :param content: содержимое для записи
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def replace_chars(text, target_char, replacement_char):
    """
    Заменяет все вхождения target_char на replacement_char в тексте.
    :param text: исходный текст
    :param target_char: символ, который нужно заменить
    :param replacement_char: символ, на который нужно заменить
    :return: текст с выполненными заменами
    """
    return text.replace(target_char, replacement_char)


def calculate_char_percentages(text):
    """
    Вычисляет процент встречаемости каждого символа в тексте.
    :param text: исходный текст
    :return: словарь, где ключ — символ, значение — процент его встречаемости
    """
    char_count = {}  # Словарь
    text_len = len(text)

    # Подсчет кол-ва символов в текстк
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Вычисление процентного соотношения
    char_percentages = {}
    for char, count in char_count.items():
        char_percentages[char] = (count / text_len) * 100

    return char_percentages


def main():
    text = task_text

    #Зашифрованный текст
    print("\nЗашифрованный текст:\n")
    print(text)

    # #Свод к единому алфавиту для удобства
    # for i in range(len(text)):
    #     if text[i] == "8":
    #         text = text.replace("8", "В")
    #     elif text[i] == "5":
    #         text = text.replace("5", "Г")
    #     elif text[i] == "4":
    #         text = text.replace("4", "Ю")
    #     elif text[i] == "7":
    #         text = text.replace("7", "Ж")
    #     elif text[i] == "2":
    #         text = text.replace("2", "З")
    #     elif text[i] == "1":
    #         text = text.replace("1", "Н")
    #     elif text[i] == "w":
    #         text = text.replace("w", "С")
    #     elif text[i] == "r":
    #         text = text.replace("r", "Т")
    #     elif text[i] == "t":
    #         text = text.replace("t", "Ц")
    #     elif text[i] == ">":
    #         text = text.replace(">", "Э")
    # print("______________________________________________________________\n\nСвод к единому алфавиту:\n")
    # print(text)


    #Процентное соотношения

    percent_dict = calculate_char_percentages(text)

    #Сортировка значений ключей
    print("\n______________________________________________________________\n\nСловарь процентного содержания букв зашифрованного текста:\n")
    sorted_dict = {}
    for key in sorted(percent_dict, key=percent_dict.get, reverse=True):
        sorted_dict[key] = percent_dict[key]
    print(sorted_dict)

    print("\n______________________________________________________________\n\nДешифрованный текст:\n")


    # text = replace_chars(text, " ", "и") #
    # text = replace_chars(text, "Е", "о") #
    # text = replace_chars(text, "Д", "н") #
    # text = replace_chars(text, "Ч", "а") #
    #
    # text = replace_chars(text, "Ы", "е") #
    # text = replace_chars(text, "Ц", "р")
    # text = replace_chars(text, "Й", "т")
    # text = replace_chars(text, "Н", "л")
    #
    # text = replace_chars(text, "З", "м")
    # text = replace_chars(text, "Ж", "ь")
    # text = replace_chars(text, "И", "с")
    # text = replace_chars(text, "Б", "к") #
    #
    # text = replace_chars(text, "Я", "з")
    # text = replace_chars(text, "Щ", "в")
    # text = replace_chars(text, "Э", "ы")
    # text = replace_chars(text, "Т", "п")
    #
    # text = replace_chars(text, "К", "у")
    # text = replace_chars(text, "С", "д")
    # text = replace_chars(text, "Ф", "я")
    # text = replace_chars(text, "Ъ", "г")
    #
    # text = replace_chars(text, "Ь", "ж")
    # text = replace_chars(text, "Л", "ф")
    # text = replace_chars(text, "М", "х")
    # text = replace_chars(text, "У", "ю")
    #
    # text = replace_chars(text, "Ю", "ц")
    # text = replace_chars(text, "О", "ш")
    # text = replace_chars(text, "Г", "ч")
    # text = replace_chars(text, "П", "щ")
    #
    # text = replace_chars(text, "А", "й")
    # text = replace_chars(text, "В", "э")
    #
    # #Замена в конце дабы исключить повторения символа " " в алфавите
    text = replace_chars(text, "О", " ")


    # crypt_key = {
    #     "r": "п",
    #     "w": "с",
    #     "t": "р",
    #
    #     "1": "л",
    #     "2": "м",
    #     "4": "ц",
    #     "5": "ч",
    #     "7": "ь",
    #     "8": "э",
    #
    #     "А": "й",
    #     "Б": "к",
    #     "Д": "н",
    #     "Е": "о",
    #     "И": "с",
    #     "Й": "т",
    #     "К": "у",
    #     "Л": "ф",
    #     "М": "х",
    #     "О": "ш",
    #     "П": "щ",
    #     "У": "ю",
    #     "Ф": "я",
    #     "Х": " ",
    #     "Ч": "а",
    #     "Щ": "в",
    #     "Ъ": "г",
    #     "Ы": "е",
    #     "Ь": "ж",
    #     "Я": "з",
    # }

    print(text)
    print("\n")

    #Запись в файлы
    write_to_file("encrypted_text.txt", task_text)
    write_to_file("decrypted_text.txt", text)
    #write_to_file("decrypt_key.txt", str(crypt_key))

if __name__ == "__main__":
    main()