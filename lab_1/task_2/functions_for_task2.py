import csv
import logging
import math
import os


def set_right_directory(folder_name: str) -> bool:
    """Устанавливает рабочую директорию на folder_name"""
    path = os.getcwd()[-len(folder_name):]
    if path == folder_name:
        return True
    
    # Поиск папки в текущей директории и её поддиректориях
    try:
        for root, dirs, files in os.walk('.'):
            if folder_name in dirs:
                # Папка найдена
                folder_path = os.path.join(root, folder_name)
                print("Папка найдена:", folder_path)

                # Установка найденной папки как рабочей директории
                os.chdir(folder_path)
                print('\033[92m' + "Рабочая директория изменена на:",\
                      os.getcwd() + '\033[0m')
                return
        print("Не удалось установить рабочую директорию")
    except:
        print('\033[91m' + "Ошибка установки рабочей директории"\
              + '\033[0m')

def main():
    """С этой функции необходимо начинать код для добавления логирования
    и установки верной рабочей директории"""
    set_right_directory("task_2")

    logging.basicConfig(filename='message.log', level=logging.DEBUG,\
                        format='%(asctime)s - %(levelname)s - %(message)s', encoding="utf-8")

main()
# Импортирую consts после вызова main(), чтобы была установлена правильная рабочая
# директория, ведь в consts используется относительный путь
import consts


def read_csv_frequency(file_name: str) -> dict:
    """Читает файл file_name формата csv с разделителем '=', возвращает словарь с ключом в виде символа и знач. в виде частоты"""
    try:
        frequency = {}
        with open(file_name, "r", encoding="utf-8") as readFile:
            file_reader = csv.reader(readFile, delimiter="=")
            for row in file_reader:
                if row[0].find("(пробел)") == -1:
                    frequency[row[0].replace(" ", "")] = float(row[1])
                else:
                    row[0] = row[0].replace(" ", "")
                    frequency[row[0].replace("(пробел)", " ")] = float(row[1])
                    
        logging.info(f"Чтение файла '{file_name}' прошло успешно")
        return frequency
    
    except FileNotFoundError:
        logging.error(f"Неудача при открытии файла '{file_name}', в функции read_csv_frequency")
    except:
        logging.error(f"Ошибка в функции read_csv_frequency")


def read_file_with_text(file_name: str, mode: str, _encoding: str) -> str:
    """Читает текст из файла."""
    try:
        text = ''
        with open(file_name, mode, encoding=_encoding) as readFile:
            text = readFile.read()

        logging.info(f"Чтение файла '{file_name}' прошло успешно")
        return text

    except FileNotFoundError:
        logging.error(f"Неудача при открытии файла '{file_name}', в функции read_file_with_text")
    except:
        logging.error(f"Ошибка в функции read_file_with_text")


def write_frequency_for_encrypt_text(file_name: str, freq: dict) -> None:
    """Записывает новую частотность в файл file_name из словаря freq"""
    try:
        with open(file_name, "w+", encoding="utf-8") as CSV_file:
            csw_writer = csv.writer(CSV_file, delimiter='=', lineterminator='\n')

            for key in freq:
                if key == " ":
                    csw_writer.writerow(["(пробел) ", " " + str(freq[key])])
                    continue
                csw_writer.writerow([str(key) + " ", " " + str(freq[key])])

        logging.info(f"Запись в файл '{file_name}' прошла успешно")

    except FileNotFoundError:
        logging.error(f"Неудача при открытии файла '{file_name}', "\
                      f"в функции write_frequency_for_encrypt_text")
    except:
        logging.error(f"Ошибка в функции write_frequency_for_encrypt_text")

def write_text_file(file_name: str, text: str) -> None:
    """Записывает текст text в файл file_name"""
    try:
        print(consts.COLOR_RED + text + consts.COLOR_RESET)
        with open(file_name, "w+", encoding="utf-8") as text_file:
            text_file.write(text)
        
        logging.info(f"Запись в файл '{file_name}' прошла успешно")

    except FileNotFoundError:
        logging.error(f"Неудача при открытии файла '{file_name}', "\
                      f"в функции write_text_file")
    except:
        logging.error(f"Ошибка в функции write_text_file")

def replacer(text: str, old_char: str, new_char: str) -> str:
    """Заменяет символ old_char на new_char в переданном тексте и возвращает его копию.
    Если в тексте уже есть new_char, то они заменяются на символ, который не используется в тексте"""
    if old_char == new_char:
        return text, new_char
    
    try:
        # Получаю список символов из юникода, для возможности замены, если
        # в старом тексте уже будут иметься те символы, на которые я собираюсь заменять
        unicode_list = [chr(i) for i in range(50, 0xC8)]
        new_txt = text
        replace_char = new_char
        if replace_char in text:
            for char in unicode_list:
                if not (char in text):
                    replace_char = char
                    break

            # Если в исходн. тексте есть символ, на который мы хотим заменить,
            # то заменяем в исходн. тексте на символ, которого ещё нет в нём
            new_txt = text.replace(new_char, replace_char)

        new_txt = new_txt.replace(old_char, new_char)
        return new_txt, replace_char
    
    except:
        logging.error(f"Ошибка в функции replacer")


def sorted_dict_with_frequency(frequency: dict, count: int = 0) -> dict:
    """Cортирует по значениям словарь с частотностью символов
    возвращает первые count самых популярных знач"""
    try:
        arr_frequency = []

        for key in frequency:
            arr_frequency.append(frequency[key])

        arr_frequency.sort(reverse=True)
        new_dict = {}

        if count == 0:
            ind = 0
            while True:
                if len(arr_frequency) == ind:
                    break
                for key in frequency:
                    if frequency[key] == arr_frequency[ind]:
                        if key in list(new_dict.keys()):
                            continue
                        else:
                            new_dict[key] = frequency[key]
                            break
                ind += 1
        else:
            ind = 0
            while True:
                if (len(arr_frequency) == ind) or (ind == count):
                    break
                for key in frequency:
                    if math.isclose(frequency[key], arr_frequency[ind]):
                        if key in new_dict.keys():
                            continue
                        else:
                            new_dict[key] = frequency[key]
                            break
                ind += 1
            print(len(new_dict))

        logging.info(f"Сортировка словаря в sorted_dict_with_frequency прошла успешно")
        return new_dict
    
    except IndexError:
        logging.error(f"Выход за границы элемента в sorted_dict_with_frequency")
    except KeyError:
        logging.error(f"Неверный ключ для словаря в sorted_dict_with_frequency")
    except:
        logging.error(f"Ошибка в функции sorted_dict_with_frequency")


def statistic(text: str) -> dict:
    """Возвращает статистику текста. Частотность символов в переданном тексте"""
    try:
        counter = {}
        all_symbols = len(text)

        for char in text:
            if char in counter.keys():
                counter[char] += 1
            else:
                counter[char] = 1
        our_frequency = counter

        for key in our_frequency:
            our_frequency[key] = our_frequency[key] / all_symbols

        return our_frequency
    
    except KeyError:
        logging.error(f"неверный ключ для словаря в statistic")
    except:
        logging.error(f"Ошибка в функции statistic")


def auto_replace_symbols(text: str, statistic_text: list, common_frequency: list, count: int = -1) -> str:
    """Рассчитывает получить зашифр. текст text и отсортированные списки в порядке убывания частоты
    statistic_text - список символов зашифрованного текста,
    common_frequency - список символов независимых текстов.
    Заменяет символы statistic_text на символы из common_frequency. 
    Возвращает новый текст и новый список statistic_text"""
    try:
        new_text = text
        ind = 0
        copy_statistic_text = statistic_text
        for char in common_frequency:
            if (len(common_frequency) == ind) or (len(copy_statistic_text) == ind) or ind == count:
                break
            # print(char, f"ind = {ind}", len(copy_statistic_text))
            new_text, new_char = replacer(new_text, copy_statistic_text[ind], char)
            if new_char != char:
                copy_statistic_text[copy_statistic_text.index(char)] = new_char
            copy_statistic_text[ind] = char
            # print(new_text)
            # print(copy_statistic_text)
            write_frequency_for_encrypt_text(
                consts.FILES["frequency_for_encrypt_text"], sorted_dict_with_frequency(statistic(new_text)))

            ind += 1

        return new_text
    
    except IndexError:
        logging.error(f"Выход за границы элемента в auto_replace_symbols")
    except:
        logging.error(f"Ошибка в функции auto_replace_symbols")
