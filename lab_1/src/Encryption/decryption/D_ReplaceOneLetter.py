import os
import json

from typing import List, Dict


class D_ReplaceOneLetter:
    """
    Класс для взлома шифра замены одной буквы и его производных.
    ...
    Атрибуты
    --------
    _text : str
        Содержит текст для работы. Нужен для удобства
    Методы
    ------
    changeText(text: str):
        Изменить текст для работы.
    
    @staticmethod 
    analysis_text_s(text: str) -> dict:
        Возвращает словарь частот для данного текста. Будет отсортирован по символам

    analysis_text(self) -> dict:
        Возвращает словарь частот для данного текста. Будет отсортирован по символам. Работает с атрибутом _text

    @staticmethod
    sort_dict_values_s(dictionary: dict) -> dict:
        Сортировка словаря по значениям частот, где первая буква - максимальная частота в тексте
    
    @staticmethod
    analysis_text_and_sort_frequency_s(text: str) -> dict:
        Вернёт уже отсортированный словарь букв - частот, где первая буква - максимальная частота в тексте.

    analysis_text_and_sort_frequency(self) -> dict:
        Вернёт уже отсортированный словарь букв - частот, где первая буква - максимальная частота в тексте. Работает с атрибутом _text.

    @staticmethod
    size_alphabet_s(text: str) -> int:
        Вернёт размер алфавита по тексту.

    size_alphabet(self) -> int:
        Вернёт размер алфавита по тексту. Работает с атрибутом _text.

    @staticmethod
    get_translate_dict_sort_frequency_s(text: str, testAlphabet: str) -> dict:
        Объединяет словарь частот и вводимый алфавит. Самая частая буква должа быть первой в testAlphabet.
    
    get_translate_dict_frequency(self, testAlphabet: str) -> dict:
        Объединяет словарь частот и вводимый алфавит. Самая частая буква должа быть первой в testAlphabet. Работает с атрибутом _test.

    @staticmethod
    get_translate_dict_sort_alphabet_s(text: str, testAlphabet: str) -> dict:
        Объединяет алфавит text, полученный функцией sorted и вводимый алфавит. Самая первая буква алфавита должа быть первой в testAlphabet. 

    get_translate_dict_sort_alphabet(text: str, testAlphabet: str) -> dict:
        Объединяет алфавит text, полученный функцией sorted и вводимый алфавит. Самая первая буква алфавита должа быть первой в testAlphabet. Работает с атрибутом _text  

    @staticmethod
    __translate(text: str, dictionary: dict) -> str:
        Переводит текст по словарю.

    @staticmethod
    decryption_sort_alphabet_s(text: str, key: str) -> str:
        Функция для расшифровки текста по тестовому словарю - key. Все буквы поставятся в соответствии алфавиту текста(сам создаст алфавит на основании sorted()). Для примера словаря смотри функцию get_translate_dict_alphabet(...)

    decryption_sort_alphabet(self, key: str) -> str:
        Функция для расшифровки текста по тестовому словарю - key. Все буквы поставятся в соответствии алфавиту текста(сам создаст алфавит на основании sorted()). Для примера словаря смотри функцию get_translate_dict_alphabet(...). Работает с атрибутом _text  
    
    @staticmethod
    decryption_sort_frequency_s(text: str, key: str) -> str:
        Функция для расшифровки текста по тестовому словарю - key. Все буквы поставятся в соответствии частоте буквам текста(сам создаст алфавит на основании частот). Для примера словаря смотри функцию get_translate_dict_frequency(...). 
    
    decryptionFrequency(text: str, key: str) -> str:
        Функция для расшифровки текста по тестовому словарю - key. Все буквы поставятся в соответствии частоте буквам текста(сам создаст алфавит на основании частот). Для примера словаря смотри функцию get_translate_dict_frequency(...). Работает с атрибутом _text  
        
    @staticmethod
    split_text(text: str, delimiters: list) -> list:
        Разделяет текст на слова, где разделители удаляются.

    @staticmethod
    split_text_by_size_s(text: str, delimiters: list, size: int) -> list:
        Разделяет текст на слова, где разделители удаляются. Остаются только слова размером size

    split_text_by_size(self, delimiters: list, size: int) -> list:
        Разделяет текст на слова, где разделители удаляются. Остаются только слова размером size. Работает с атрибутом _text.

    @staticmethod
    swap_letters_in_test_alphabet(testAlphabet: str, letter_1: str, letter_2: set) -> str:
        Меняет местами символы алфавита. Нужно чтобы алфавит соотвествовал некоторым критериям.
    
    @staticmethod
    count_word_size_in_text_s(text: str, delimiters: list, size: int) -> int:
        Находит количество слов размером size.
    
    count_word_size_in_text(self, delimiters: list, size: int) -> int:
        Находит количество слов размером size. Работает с атрибутом _text

    @staticmethod
    word_size_in_text_frequency_s(text: str, delimiters: list, size: int) -> float:
        Возвращает частотность слов размером size. 

    word_size_in_text_frequency_s(self, delimiters: list, size: int) -> float:
        Возвращает частотность слов размером size. Работает с атрибутом _text.

    @staticmethod
    swap_set_characters(testAlphabet: str, set_1: str, set_2: str) -> str:
        Меняет местами определнное количество символов в алфавите. По сути расширение для swap_letters_in_test_alphabet(...).
    """
    
    def __init__(self, text: str):
        """
        Устанавливает все необходимые атрибуты для объекта D_ReplaceOneLetter.
        Параметры
        ---------
        _text : str
                Текст для расшифровки

        Исключения
        ----------
        None

        Возвращаемое значение
        ---------------------
        None
        """
        self._text = text
        pass
    
    def changeText(self, text: str):
        """
        Меняет текст класса на другой. Уже новый текст будет использоваться для расшифровки.
        Параметры
        ---------
        text : str
            Текст на замену для атрибута _text.

        Исключения
        ----------
        None

        Возвращаемое значение
        ---------------------
        None

        """
        self._text = text
        pass
    

    @staticmethod
    def analysis_text_s(text: str) -> dict:
        """
        Анализирует текст и возвращает словарь частот текста. Поиск словаря происходит по символу.
        
        Параметры
        ---------
        text : str
            Текст для анализа. Так как функция статическая
        
        Исключения
        ----------
        None

        Возвращаемое значение
        ---------------------
        Неотсортированный словарь частот символов текста

        """
        size = len(text)
        alphabet = sorted(set(text))
        frequency = dict()

        for letter in alphabet:

            frequency[letter] = text.count(letter) / size
        return frequency
    
    def analysis_text(self) -> dict:
        """
        Анализирует текст и возвращает словарь частот текста. Работает с атрибутом _text
        
        Параметры
        ---------
        None

        Исключения
        ----------
        None
        
        Возвращаемое значение
        ---------------------
        Неотсортированный словарь частот символов текста _text
        """
        return D_ReplaceOneLetter.analysis_text_s(self._text)
    

    @staticmethod
    def sort_dict_values_s(dictionary: dict) -> dict:
        """
        Сортирует словарь по частотам из функций analysis_text_s и analisysText. Нужно для остальных функций.
        
        Параметры
        ---------
        dictionary: dict
            Неотсортированный словарь частот
    
        Исключения
        ----------
        None

        Возвращаемое значение
        ---------------------
        Отсортированный словарь частот символов.
        """
        newDict = dict(reversed(sorted(dictionary.items(), key=lambda x: x[1])))

        return newDict
    
    
    @staticmethod
    def analysis_text_and_sort_frequency_s(text: str) -> dict:
        """
        Анализирует текст и возвращает отсортированный словарь частот текста
        
        Параметры
        ---------
        text : str
            Текст для анализа

        Исключения
        ----------
        None

        Возвращаемое значение
        ---------------------
        Отсортированный словарь частот символов текста text
        """
        return D_ReplaceOneLetter.sort_dict_values_s(D_ReplaceOneLetter.analysis_text_s(text))
    

    def analysis_text_and_sort_frequency(self) -> dict:
        """
        Анализирует текст и возвращает отсортированный словарь частот текста
        
        Параметры
        ---------
        None

        Исключения
        ----------
        None

        Возвращаемое значение
        ---------------------
        Отсортированный словарь частот символов текста text. Работает с атрибутом _text
        """
        return D_ReplaceOneLetter.sort_dict_values_s(D_ReplaceOneLetter.analysis_text_s(self._text))
    

    # def analysis_text(self) -> dict:
        
    #     return D_ReplaceOneLetter.analysis_text_s(self._text)

    @staticmethod
    def size_alphabet_s(text: str) -> int:
        """
        Возвращает размер алфавита текста
        
        Параметры
        ---------
        text : str
            Текст для анализа

        Исключения
        ----------
        None

        Возвращаемое значение
        ---------------------
        Размер алфавита
        """
        return len(set(text))
    
    def size_alphabet_text(self) -> int:
        """
        Возвращает размер алфавита текста. Работает с атрибутом _text
        
        Параметры
        ---------
        None
        
        Исключения
        ----------
        None

        Возвращаемое значение
        ---------------------
        Размер алфавита
        """
        return len(set(self._text))

    
    @staticmethod
    def get_translate_dict_sort_frequency_s(text: str, testAlphabet: str) -> dict:
        """
        Функция создаёт алфавит текста и объединяет его с тестовым алфавитом. 
        Символы сопоставляются по частотности в текста. На первой букве
        тестового алфавита должны быть символы встречающиеся чаще всего
        
        Параметры
        ---------
        text : str
            Текст для обработки
        testAlphabet: str
            Алфавит для построения словаря
        
        Исключения
        ----------
        1. Размеры алфавитов текста и тестового алфавита должны совпадать 
        2. В тестовом алфавите должны быть уникальные значения, так как это моноалфавитная замена.
        
        Возвращаемое значение
        ---------------------
        Новый словарь отсортированный по частотам. **Используется для замены символов текста
        """
        size_alphabet = D_ReplaceOneLetter.size_alphabet_s(text)
        sizeTestAlphabet = len(set(testAlphabet))
        
        if size_alphabet != sizeTestAlphabet:
            raise Exception(f"Your testAlphabet is very bad size Alphabet: {size_alphabet}, size test Alphabet: {sizeTestAlphabet}")
        
        alphabet = list(D_ReplaceOneLetter.sort_dict_values_s(D_ReplaceOneLetter.analysis_text_s(text)).keys())

        translater = dict()

        for index in range(sizeTestAlphabet):

            translater[alphabet[index]] = testAlphabet[index]
        
        return  translater
    
    def get_translate_dict_frequency(self, testAlphabet: str) -> dict:
        """
        Функция создаёт алфавит атрибута _text и объединяет его с тестовым алфавитом. 
        Символы сопоставляются по частотности в текста. На первой букве
        тестового алфавита должны быть символы встречающиеся чаще всего
        
        Параметры
        ---------
        testAlphabet: str
            Алфавит для построения словаря
        
        Исключения
        ----------
        1. Размеры алфавитов текста и тестового алфавита должны совпадать 
        2. В тестовом алфавите должны быть уникальные значения, так как это моноалфавитная замена.
        
        Возвращаемое значение
        ---------------------
        Новый словарь отсортированный по частотам. **Используется для замены символов текста
        """
        return D_ReplaceOneLetter.get_translate_dict_sort_frequency_s(self._text, testAlphabet)


    @staticmethod
    def get_translate_dict_sort_alphabet_s(text: str, testAlphabet: str) -> dict:
        """
        Функция создаёт алфавит текста и объединяет его с тестовым алфавитом. 
        Символы сопоставляются по алфавиту в текста(с помощью функции sorted()). На первой букве
        тестового алфавита должны быть символы которые сопоставятся с первой буквой текстового 
        алфавита
        
        Параметры
        ---------
        text : str
            Текст для обработки
        testAlphabet: str
            Алфавит для построения словаря
        
        Исключения
        ----------
        1. Размеры алфавитов текста и тестового алфавита должны совпадать 
        2. В тестовом алфавите должны быть уникальные значения, так как это моноалфавитная замена.
        
        Возвращаемое значение
        ---------------------
        Новый словарь отсортированный по алфавиту. **Используется для получения ключа.
        """
        size_alphabet = D_ReplaceOneLetter.size_alphabet_s(text)
        sizeTestAlphabet = len(set(testAlphabet))
        
        if size_alphabet != sizeTestAlphabet:
            raise Exception(f"Your testAlphabet is very bad size Alphabet: {size_alphabet}, size test Alphabet: {sizeTestAlphabet}")
        
        alphabet = sorted(set(text))

        translater = dict()

        for index in range(sizeTestAlphabet):

            translater[alphabet[index]] = testAlphabet[index]
        
        return  translater

    def get_translate_dict_alphabet(self, testAlphabet: str) -> dict:
        """
        Функция создаёт алфавит атрибута _text и объединяет его с тестовым алфавитом. 
        Символы сопоставляются по алфавиту в текста(с помощью функции sorted()). На первой букве
        тестового алфавита должны быть символы которые сопоставятся с первой буквой текстового 
        алфавита
        
        Параметры
        ---------
        testAlphabet: str
            Алфавит для построения словаря
        
        Исключения
        ----------
        1. Размеры алфавитов текста и тестового алфавита должны совпадать 
        2. В тестовом алфавите должны быть уникальные значения, так как это 
        моноалфавитная замена.
        
        Возвращаемое значение
        ---------------------
        Новый словарь отсортированный по алфавиту. **Используется для получения ключа.
        """
        return D_ReplaceOneLetter.get_translate_dict_sort_alphabet_s(self._text, testAlphabet)


    @staticmethod
    def __translate(text: str, dictionary: dict) -> str:
        """
        Переводит весь текст по введённому словарю.

        Параметры
        ---------
        text : str
            Текст для обработки
        dictionary : dict
            Словарь для перевода
        
        Исключения
        ----------
        None

        **Проверок на правильность 
        словаря и тд нету, так как функция скрыта от пользователя. Проверки
        производятся в основных функциях
        
        Возвращаемое значение
        ---------------------
        Переведённый с помощью словаря текст
        """
        translate = ""
        for i in text:
            translate += dictionary[i]
        return translate


    @staticmethod
    def decryption_sort_alphabet_s(text: str, key: str) -> str:
        """
        Расшифровывает весь текст по введённому ключу. Ключом служит уже
        обработанный словарь. Символы в ключе должны быть в алфавитном для
        текста порядке. Сначала сортируется словарь текста, потом строиться
        расшифровка

        Параметры
        ---------
        text : str
            Текст для расшифровки
        key : str
            Ключ, состоящий из символов.
        
        Исключения
        ----------
        1. get_translate_dict_sort_alphabet_s(...).

        Возвращаемое значение
        ---------------------
        Расшифрованный текст.
        """
        dictionary = D_ReplaceOneLetter.get_translate_dict_sort_alphabet_s(text, key)
        return D_ReplaceOneLetter.__translate(text, dictionary)

    def decryption_sort_alphabet(self, key: str) -> str:
        """
        Расшифровывает весь текст атрибута _text по введённому ключу. Ключом служит уже
        обработанный словарь. Символы в ключе должны быть в алфавитном для
        текста порядке. Сначала сортируется словарь текста, потом строиться
        расшифровка

        Параметры
        ---------
        key : str
            Ключ, состоящий из символов.
        
        Исключения
        ----------
        1. get_translate_dict_sort_alphabet_s(...).

        Возвращаемое значение
        ---------------------
        Расшифрованный текст атрибута _text.
        """
        return D_ReplaceOneLetter.decryption_sort_alphabet_s(self._text, key)


    @staticmethod
    def decryption_sort_frequency_s(text: str, key: str) -> str:
        """
        Расшифровывает весь текст по введённому ключу. Ключом служит уже
        обработанный вами словарь, чтобы потом поставить их в соотвествии с 
        частотами. Символы в ключе должны быть в частотном порядке появления
        в тексте. Сначала сортируется словарь текста, потом строиться
        расшифровка

        Параметры
        ---------
        text : str
            Текст для расшифровки
        key : str
            Ключ, состоящий из символов.
        
        Исключения
        ----------
        1. get_translate_dict_sort_frequency_s(...).

        Возвращаемое значение
        ---------------------
        Расшифрованный текст.
        """
        dictionary = D_ReplaceOneLetter.get_translate_dict_sort_frequency_s(text, key)
        return D_ReplaceOneLetter.__translate(text, dictionary)
        
    def decryption_sort_frequency(self, key: str) -> str:
        """
        Расшифровывает весь текст атрибута _text по введённому ключу. 
        Ключом служит уже обработанный вами словарь, чтобы потом поставить 
        их в соотвествии с частотами. Символы в ключе должны быть в частотном 
        порядке появления в тексте. Сначала сортируется словарь текста, потом 
        строиться расшифровка

        Параметры
        ---------
        text : str
            Текст для расшифровки
        key : str
            Ключ, состоящий из символов.
        
        Исключения
        ----------
        1. get_translate_dict_sort_frequency_s(...).

        Возвращаемое значение
        ---------------------
        Расшифрованный текст атрибута _text
        """
        return D_ReplaceOneLetter.decryption_sort_frequency_s(self._text, key)

    @staticmethod
    def split_text(text: str, delimiters: list) -> list:
        """
        Делит текст на слова. Разделителями служит список значений

        Параметры
        ---------
        text : str
            Текст для обаботки
        delimetrs : list
            Список разделителей.
        
        Исключения
        ----------
        1. Список delimetrs пуст

        Возвращаемое значение
        ---------------------
        Список слов.
        """
        if len(delimiters) < 1:
            Exception("Doesn't have delimetrs")

        for delimiter in delimiters:
            text = text.replace(delimiter, delimiters[0])
        words = text.split(delimiters[0])
        
        return words
    
    @staticmethod
    def split_text_by_size_s(text: str, delimiters: list, size: int) -> list:
        """
        Делит текст на слова и оставляет только слова размером size. Разделителями служит список значений. 

        Параметры
        ---------
        text : str
            Текст для расшифровки
        delimetrs : list
            Список разделителей.
        size : int
            Размеры слов.        
        Исключения
        ----------
        1. split_text(...)

        Возвращаемое значение
        ---------------------
        Список слов размером size
        """
        words = D_ReplaceOneLetter.split_text(text, delimiters)
        filtered_words = [word for word in words if len(word) == size]

        return filtered_words
    
    def split_text_by_size(self, delimiters: list, size: int) -> list:
        """
        Делит текст на слова и оставляет только слова размером size. Разделителями служит список значений. Работает с атрибутом size.

        Параметры
        ---------
        delimetrs : list
            Список разделителей.
        size : int
            Размеры слов.        
        Исключения
        ----------
        1. split_text(...)

        Возвращаемое значение
        ---------------------
        Список слов размером size
        """
        return D_ReplaceOneLetter.split_text_by_size_s(self._text, delimiters, size) 
        
    @staticmethod
    def swap_letters_in_test_alphabet(testAlphabet: str, letter_1: str, letter_2: set) -> str:
        """
        Меняет местами буквы в тестовом алфавите. 
        
        Параметры
        ---------
        testAlphabet : str
            Алфавит в котором меняют буквы
        letter_1 : str
            Первая буква.
        letter_2 : str
            Вторая буква.
                
        Исключения
        ----------
        1. Алфавит не является алфавитом, а набором символов.
        2. letter_1 и letter_2 не являются буквами, а набором символов или 
        вовсе пусты.
        3. letter_1 и letter_2 не являются частью алфавита.

        Возвращаемое значение
        ---------------------
        Алфавит с изменённой парой символов.
        """
        if len(set(testAlphabet)) != len(testAlphabet) or len(letter_1) != 1 \
            or len(letter_2) != 1 or not (letter_1 in testAlphabet) or not \
            (letter_2 in testAlphabet):
            
            raise Exception("Bad Alphabet or letters for swap")
        
        new_text = ""
        for char in testAlphabet:
            if char == letter_1:
                new_text += letter_2
            elif char == letter_2:
                new_text += letter_1
            else:
                new_text += char
        
        return new_text
    
    @staticmethod
    def count_word_size_in_text_s(text: str, delimiters: list, size: int) -> int:
        """
        Функция для вычисления количества слова размером size в тексте.
        
        Параметры
        ---------
        text : str
            Текст для анализа.
        delimeters : list
            Список разделителей.
        size : int
            Размеры слов
                
        Исключения
        ----------
        1. split_text(...)

        Возвращаемое значение
        ---------------------
        Количество слов размером size
        """
        return len(D_ReplaceOneLetter.split_text_by_size_s(text, delimiters, size))
    
    def count_word_size_in_text(self, delimiters: list, size: int) -> int:
        """
        Функция для вычисления количества слова размером size в тексте атрибута _text.
        
        Параметры
        ---------
        delimeters : list
            Список разделителей.
        size : int
            Размеры слов
                
        Исключения
        ----------
        1. split_text(...)

        Возвращаемое значение
        ---------------------
        Количество слов размером size
        """
        return len(D_ReplaceOneLetter.split_text_by_size_s(self._text, delimiters, size))
    
    @staticmethod
    def word_size_in_text_frequency_s(text: str, delimiters: list, size: int) -> float:
        """
        Вычисляет частоту встречаемости слов размером size в тексте.
        
        Параметры
        ---------
        text : str
            Текст для обработки
        delimeters : list
            Список разделителей.
        size : int
            Размеры слов
                
        Исключения
        ----------
        1. split_text(...)

        Возвращаемое значение
        ---------------------
        Частота встречаемости слов размером size
        """
        return len(D_ReplaceOneLetter.split_text_by_size_s(text, delimiters, size)) / len(D_ReplaceOneLetter.split_text(text, delimiters))
    
    def word_size_in_text_frequency(self, delimiters: list, size: int) -> float:
        """
        Вычисляет частоту встречаемости слов размером size в тексте атрибута _text. 
        
        Параметры
        ---------
        delimeters : list
            Список разделителей.
        size : int
            Размеры слов
                
        Исключения
        ----------
        1. split_text(...)

        Возвращаемое значение
        ---------------------
        Частота встречаемости слов размером size
        """
        return len(D_ReplaceOneLetter.split_text_by_size_s(self._text, delimiters, size)) / len(D_ReplaceOneLetter.split_text(self._text, delimiters))


    @staticmethod
    def swap_set_characters(testAlphabet: str, set_1: str, set_2: str) -> str:
        """
        Меняет местами набор символов в тестовом алфавите. 
        
        Параметры
        ---------
        testAlphabet : str
            Алфавит в котором меняют буквы
        set_1 : str
            Первый набор.
        set_2 : str
            Второй набор.
                
        Исключения
        ----------
        1. Размеры наборов не совпадают. Также алфавиты этих наборов не совпадают.
        2. swap_letters_in_test_alphabet(...)

        Возвращаемое значение
        ---------------------
        Алфавит с изменённым набором символов.
        """
        if len(set(set_1)) != len(set(set_2)) or len(set_1) != len(set_2):

            raise Exception("Bad set_1_2 for swap")

        newText = testAlphabet
        for c in range(len(set_1)):
            newText = D_ReplaceOneLetter.swap_letters_in_test_alphabet(newText, set_1[c], set_2[c])
        
        return newText
        
        
    def export_key_json(self, 
                       alphabetFrequency: str, 
                       fileForExport: str="key_alphabet.json", 
                       nameForHeaderKey:str = "key", 
                       nameForHeaderAlphabet:str = "alphabet") -> None:
        
        if os.path.isfile(fileForExport):
            raise Exception(f"{fileForExport} уже существует")
            
        info = self.get_translate_dict_frequency(alphabetFrequency)

        info1 = {nameForHeaderKey: dict(zip(info.keys(), info.values()))}

        info2 = {nameForHeaderAlphabet: dict(zip(info.values(), info.keys()))}

        info = [info1, info2]

        json_data = json.dumps(info, sort_keys=True, indent=2, ensure_ascii=False)

        with open(fileForExport, 'w') as f:
            f.write(json_data)    