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
    analysisText_s(text: str) -> dict:
        Возвращает словарь частот для данного текста. Будет отсортирован по символам

    analysisText(self) -> dict:
        Возвращает словарь частот для данного текста. Будет отсортирован по символам. Работает с атрибутом _text

    @staticmethod
    sortDictValues_s(dictionary: dict) -> dict:
        Сортировка словаря по значениям частот, где первая буква - максимальная частота в тексте
    
    @staticmethod
    analysisTextAndSortFrequency_s(text: str) -> dict:
        Вернёт уже отсортированный словарь букв - частот, где первая буква - максимальная частота в тексте.

    analysisTextAndSortFrequency(self) -> dict:
        Вернёт уже отсортированный словарь букв - частот, где первая буква - максимальная частота в тексте. Работает с атрибутом _text.

    @staticmethod
    sizeAlphabet_s(text: str) -> int:
        Вернёт размер алфавита по тексту.

    sizeAlphabet(self) -> int:
        Вернёт размер алфавита по тексту. Работает с атрибутом _text.

    @staticmethod
    getTranslateDictSortFrequency_s(text: str, testAlphabet: str) -> dict:
        Объединяет словарь частот и вводимый алфавит. Самая частая буква должа быть первой в testAlphabet.
    
    getTranslateDictFrequency(self, testAlphabet: str) -> dict:
        Объединяет словарь частот и вводимый алфавит. Самая частая буква должа быть первой в testAlphabet. Работает с атрибутом _test.

    @staticmethod
    getTranslateDictSortAlphabet_s(text: str, testAlphabet: str) -> dict:
        Объединяет алфавит text, полученный функцией sorted и вводимый алфавит. Самая первая буква алфавита должа быть первой в testAlphabet. 

    getTranslateDictSortAlphabet(text: str, testAlphabet: str) -> dict:
        Объединяет алфавит text, полученный функцией sorted и вводимый алфавит. Самая первая буква алфавита должа быть первой в testAlphabet. Работает с атрибутом _text  

    @staticmethod
    __translate(text: str, dictionary: dict) -> str:
        Переводит текст по словарю.

    @staticmethod
    decryptionSortAlphabet_s(text: str, key: str) -> str:
        Функция для расшифровки текста по тестовому словарю - key. Все буквы поставятся в соответствии алфавиту текста(сам создаст алфавит на основании sorted()). Для примера словаря смотри функцию getTranslateDictAlphabet(...)

    decryptionSortAlphabet(self, key: str) -> str:
        Функция для расшифровки текста по тестовому словарю - key. Все буквы поставятся в соответствии алфавиту текста(сам создаст алфавит на основании sorted()). Для примера словаря смотри функцию getTranslateDictAlphabet(...). Работает с атрибутом _text  
    
    @staticmethod
    decryptionSortFrequency_s(text: str, key: str) -> str:
        Функция для расшифровки текста по тестовому словарю - key. Все буквы поставятся в соответствии частоте буквам текста(сам создаст алфавит на основании частот). Для примера словаря смотри функцию getTranslateDictFrequency(...). 
    
    decryptionFrequency(text: str, key: str) -> str:
        Функция для расшифровки текста по тестовому словарю - key. Все буквы поставятся в соответствии частоте буквам текста(сам создаст алфавит на основании частот). Для примера словаря смотри функцию getTranslateDictFrequency(...). Работает с атрибутом _text  
        
    @staticmethod
    splitText(text: str, delimiters: list) -> list:
        Разделяет текст на слова, где разделители удаляются.

    @staticmethod
    splitTextBySize_s(text: str, delimiters: list, size: int) -> list:
        Разделяет текст на слова, где разделители удаляются. Остаются только слова размером size

    splitTextBySize(self, delimiters: list, size: int) -> list:
        Разделяет текст на слова, где разделители удаляются. Остаются только слова размером size. Работает с атрибутом _text.

    @staticmethod
    swapLettersInTestAlphabet(testAlphabet: str, letter_1: str, letter_2: set) -> str:
        Меняет местами символы алфавита. Нужно чтобы алфавит соотвествовал некоторым критериям.
    
    @staticmethod
    countWordSizeInText_s(text: str, delimiters: list, size: int) -> int:
        Находит количество слов размером size.
    
    countWordSizeInText(self, delimiters: list, size: int) -> int:
        Находит количество слов размером size. Работает с атрибутом _text

    @staticmethod
    wordSizeInTextFrequency_s(text: str, delimiters: list, size: int) -> float:
        Возвращает частотность слов размером size. 

    wordSizeInTextFrequency_s(self, delimiters: list, size: int) -> float:
        Возвращает частотность слов размером size. Работает с атрибутом _text.

    @staticmethod
    swapSetCharacters(testAlphabet: str, set_1: str, set_2: str) -> str:
        Меняет местами определнное количество символов в алфавите. По сути расширение для swapLettersInTestAlphabet(...).
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
    def analysisText_s(text: str) -> dict:
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
    
    def analysisText(self) -> dict:
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
        return D_ReplaceOneLetter.analysisText_s(self._text)
    

    @staticmethod
    def sortDictValues_s(dictionary: dict) -> dict:
        """
        Сортирует словарь по частотам из функций analysisText_s и analisysText. Нужно для остальных функций.
        
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
    def analysisTextAndSortFrequency_s(text: str) -> dict:
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
        return D_ReplaceOneLetter.sortDictValues_s(D_ReplaceOneLetter.analysisText_s(text))
    

    def analysisTextAndSortFrequency(self) -> dict:
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
        return D_ReplaceOneLetter.sortDictValues_s(D_ReplaceOneLetter.analysisText_s(self._text))
    

    # def analysisText(self) -> dict:
        
    #     return D_ReplaceOneLetter.analysisText_s(self._text)

    @staticmethod
    def sizeAlphabet_s(text: str) -> int:
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
    
    def sizeAlphabetText(self) -> int:
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
    def getTranslateDictSortFrequency_s(text: str, testAlphabet: str) -> dict:
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
        sizeAlphabet = D_ReplaceOneLetter.sizeAlphabet_s(text)
        sizeTestAlphabet = len(set(testAlphabet))
        
        if sizeAlphabet != sizeTestAlphabet:
            raise Exception(f"Your testAlphabet is very bad size Alphabet: {sizeAlphabet}, size test Alphabet: {sizeTestAlphabet}")
        
        alphabet = list(D_ReplaceOneLetter.sortDictValues_s(D_ReplaceOneLetter.analysisText_s(text)).keys())

        translater = dict()

        for index in range(sizeTestAlphabet):

            translater[alphabet[index]] = testAlphabet[index]
        
        return  translater
    
    def getTranslateDictFrequency(self, testAlphabet: str) -> dict:
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
        return D_ReplaceOneLetter.getTranslateDictSortFrequency_s(self._text, testAlphabet)


    @staticmethod
    def getTranslateDictSortAlphabet_s(text: str, testAlphabet: str) -> dict:
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
        sizeAlphabet = D_ReplaceOneLetter.sizeAlphabet_s(text)
        sizeTestAlphabet = len(set(testAlphabet))
        
        if sizeAlphabet != sizeTestAlphabet:
            raise Exception(f"Your testAlphabet is very bad size Alphabet: {sizeAlphabet}, size test Alphabet: {sizeTestAlphabet}")
        
        alphabet = sorted(set(text))

        translater = dict()

        for index in range(sizeTestAlphabet):

            translater[alphabet[index]] = testAlphabet[index]
        
        return  translater

    def getTranslateDictAlphabet(self, testAlphabet: str) -> dict:
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
        return D_ReplaceOneLetter.getTranslateDictSortAlphabet_s(self._text, testAlphabet)


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
    def decryptionSortAlphabet_s(text: str, key: str) -> str:
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
        1. getTranslateDictSortAlphabet_s(...).

        Возвращаемое значение
        ---------------------
        Расшифрованный текст.
        """
        dictionary = D_ReplaceOneLetter.getTranslateDictSortAlphabet_s(text, key)
        return D_ReplaceOneLetter.__translate(text, dictionary)

    def decryptionSortAlphabet(self, key: str) -> str:
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
        1. getTranslateDictSortAlphabet_s(...).

        Возвращаемое значение
        ---------------------
        Расшифрованный текст атрибута _text.
        """
        return D_ReplaceOneLetter.decryptionSortAlphabet_s(self._text, key)


    @staticmethod
    def decryptionSortFrequency_s(text: str, key: str) -> str:
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
        1. getTranslateDictSortFrequency_s(...).

        Возвращаемое значение
        ---------------------
        Расшифрованный текст.
        """
        dictionary = D_ReplaceOneLetter.getTranslateDictSortFrequency_s(text, key)
        return D_ReplaceOneLetter.__translate(text, dictionary)
        

    def decryptionSortFrequency(self, key: str) -> str:
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
        1. getTranslateDictSortFrequency_s(...).

        Возвращаемое значение
        ---------------------
        Расшифрованный текст атрибута _text
        """
        return D_ReplaceOneLetter.decryptionSortFrequency_s(self._text, key)

    @staticmethod
    def splitText(text: str, delimiters: list) -> list:
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
    def splitTextBySize_s(text: str, delimiters: list, size: int) -> list:
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
        1. splitText(...)

        Возвращаемое значение
        ---------------------
        Список слов размером size
        """
        words = D_ReplaceOneLetter.splitText(text, delimiters)
        filtered_words = [word for word in words if len(word) == size]

        return filtered_words
    
    def splitTextBySize(self, delimiters: list, size: int) -> list:
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
        1. splitText(...)

        Возвращаемое значение
        ---------------------
        Список слов размером size
        """
        return D_ReplaceOneLetter.splitTextBySize_s(self._text, delimiters, size) 
        
    @staticmethod
    def swapLettersInTestAlphabet(testAlphabet: str, letter_1: str, letter_2: set) -> str:
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
    def countWordSizeInText_s(text: str, delimiters: list, size: int) -> int:
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
        1. splitText(...)

        Возвращаемое значение
        ---------------------
        Количество слов размером size
        """
        return len(D_ReplaceOneLetter.splitTextBySize_s(text, delimiters, size))
    
    def countWordSizeInText(self, delimiters: list, size: int) -> int:
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
        1. splitText(...)

        Возвращаемое значение
        ---------------------
        Количество слов размером size
        """
        return len(D_ReplaceOneLetter.splitTextBySize_s(self._text, delimiters, size))
    
    @staticmethod
    def wordSizeInTextFrequency_s(text: str, delimiters: list, size: int) -> float:
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
        1. splitText(...)

        Возвращаемое значение
        ---------------------
        Частота встречаемости слов размером size
        """
        return len(D_ReplaceOneLetter.splitTextBySize_s(text, delimiters, size)) / len(D_ReplaceOneLetter.splitText(text, delimiters))
    
    def wordSizeInTextFrequency(self, delimiters: list, size: int) -> float:
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
        1. splitText(...)

        Возвращаемое значение
        ---------------------
        Частота встречаемости слов размером size
        """
        return len(D_ReplaceOneLetter.splitTextBySize_s(self._text, delimiters, size)) / len(D_ReplaceOneLetter.splitText(self._text, delimiters))


    @staticmethod
    def swapSetCharacters(testAlphabet: str, set_1: str, set_2: str) -> str:
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
        2. swapLettersInTestAlphabet(...)

        Возвращаемое значение
        ---------------------
        Алфавит с изменённым набором символов.
        """
        if len(set(set_1)) != len(set(set_2)) or len(set_1) != len(set_2):

            raise Exception("Bad set_1_2 for swap")

        newText = testAlphabet
        for c in range(len(set_1)):
            newText = D_ReplaceOneLetter.swapLettersInTestAlphabet(newText, set_1[c], set_2[c])
        
        return newText
        




        





    
