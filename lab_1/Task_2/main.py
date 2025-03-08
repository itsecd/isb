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

    #Свод к единому алфавиту для удобства
    for i in range(len(text)):
        if text[i] == "ю":
            text = text.replace("ю", "Ю")
        elif text[i] == "г":
            text = text.replace("г", "Г")
        elif text[i] == "у":
            text = text.replace("у", "У")

        elif text[i] == "7":
            text = text.replace("7", "А")
        elif text[i] == "1":
            text = text.replace("1", "Б")
        elif text[i] == "9":
            text = text.replace("9", "В")
        elif text[i] == "3":
            text = text.replace("3", "Е")

        elif text[i] == "Q":
            text = text.replace("Q", "З")
        elif text[i] == "U":
            text = text.replace("U", "Л")
        elif text[i] == "N":
            text = text.replace("N", "М")
        elif text[i] == "Z":
            text = text.replace("Z", "Н")
        elif text[i] == "Y":
            text = text.replace("Y", "С")
        elif text[i] == "s":
            text = text.replace("s", "Ф")
        elif text[i] == "R":
            text = text.replace("R", "Ц")
        elif text[i] == "i":
            text = text.replace("i", "Ч")
        elif text[i] == "F":
            text = text.replace("F", "Ш")
        elif text[i] == "G":
            text = text.replace("G", "Щ")

        elif text[i] == "=":
            text = text.replace("=", "Ъ")
        elif text[i] == "<":
            text = text.replace("<", "Ы")
        elif text[i] == "%":
            text = text.replace("%", "Ь")

    print("______________________________________________________________\n\nСвод к единому алфавиту:\n")
    print(text)


    #Процентное соотношения
    percent_dict = calculate_char_percentages(text)

    #Сортировка значений ключей
    print("\n______________________________________________________________\n\nСловарь процентного содержания букв зашифрованного текста:\n")
    sorted_dict = {}
    for key in sorted(percent_dict, key=percent_dict.get, reverse=True):
        sorted_dict[key] = percent_dict[key]
    print(sorted_dict)

    print("\n______________________________________________________________\n\nДешифрованный текст:\n")


    text = replace_chars(text, "З", "е") # (Q)
    text = replace_chars(text, "А", "о") #2 (7)
    text = replace_chars(text, "Х", "м") #
    text = replace_chars(text, "Р", "к") #
    #
    text = replace_chars(text, "Д", "я") #
    text = replace_chars(text, "Ц", "ю")
    text = replace_chars(text, "Й", "б")
    text = replace_chars(text, "Ь", "г")
    #
    text = replace_chars(text, "Ч", "ш")
    text = replace_chars(text, "Ж", "н") #
    text = replace_chars(text, "И", "п")
    text = replace_chars(text, "Б", "в")
    #
    text = replace_chars(text, "Я", "а")
    text = replace_chars(text, "Н", "ф")
    text = replace_chars(text, "Ш", "щ")
    text = replace_chars(text, "Ё", "и")
    text = replace_chars(text, "Т", "л")
    #
    text = replace_chars(text, "К", "ы")
    text = replace_chars(text, "Е", "й")
    text = replace_chars(text, "Ф", "у")
    text = replace_chars(text, "Ъ", "р")
    #
    text = replace_chars(text, "С", "ж")
    text = replace_chars(text, "Л", "т")
    text = replace_chars(text, "М", "ь")
    text = replace_chars(text, "У", "д")
    #
    text = replace_chars(text, "Ю", "х")
    text = replace_chars(text, "Щ", "э")
    text = replace_chars(text, "Г", "ц")
    text = replace_chars(text, "П", "с")
    #
    text = replace_chars(text, "Ы", "ч")
    text = replace_chars(text, "В", "з")
    #
    # #Замена в конце дабы исключить повторения символа " " в алфавите
    text = replace_chars(text, "О", " ") #1


    crypt_key = {
        "=": "р",
        "<": "ч",
        "%": "г",

        "7": "о",
        "1": "в",
        "9": "з",
        "3": "й",

        "Q": "е",
        "U": "т",
        "N": "ь",
        "Z": "ф",
        "Y": "ж",
        "s": "у",
        "R": "ю",
        "i": "ш",
        "F": "щ",
        "G": "э",

        "О": " ",
        "Ё": "и",
        "Ж": "н",
        "П": "с",
        "Я": "а",
        "Д": "я",
        "И": "п",
        "ю": "х",
        "Й": "б",
        "г": "ц",
        "Х": "м",
        "Т": "л",
        "К": "ы",
        "у": "д",
        "Р": "к",
    }

    print(text)
    print("\n")

    #Запись в файлы
    write_to_file("encrypted_text.txt", task_text)
    write_to_file("decrypted_text.txt", text)
    write_to_file("decrypt_key.txt", str(crypt_key))

if __name__ == "__main__":
    main()