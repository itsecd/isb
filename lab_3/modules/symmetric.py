import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from modules.file_working import *

class Symmetric:
    def __init__(self):
        self.key = None

    def key_generation(self) -> bytes:
        """
        Генерирование случайного 16-байтового ключа шифрования.

        Returns:
        self.key(bytes): ключ шифрования.
        """        
        self.key = os.urandom(16)
        return self.key
    
    def serialization_key(self, path: str)->None:
        """
        Сериализация ключа симметричного алгоритма в файл.

        Params:
        path(str): путь к файлу для записи.
        """
        write_bytes_to_txt(self.key, path)

    def deserialization_key(self, path: str)->None:
        """
        Десериализация ключа симметричного алгоритма.

        Params:
        path(str): путь к файлу с данными

        Returns:
        bytes: возвращение десериализованного ключа.
        """
        self.key = read_bytes(path)
        return self.key

    def __data_padding(self, text: str):
        """
        Заполнение данных для работы с блочным шифром - мы делаем длину
        сообщения кратной длине зашифрованного блока.

        Params: 
        text(str): Сообщение, которое необходимо заполнить.

        Returns:
        bytes: байтовое сообщение, кратное длине зашифрованного блока.
        """
        padder = padding.PKCS7(128).padder()
        btext = bytes(text, 'UTF-8')
        padded_text = padder.update(btext) + padder.finalize()
        return padded_text
    
    def text_encryption(self, text: str, key: bytes)->str:
        """
        Зашифровывание текста с помощью симметричного алгоритма.

        Params:
        text (str): текст, который должен быть зашифрован.
        key (bytes): Ключ для шифрования текста.

        Returns:
        str: зашифрованный текст.
        """
        iv = os.urandom(16)
        cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(self.__data_padding(text)) + encryptor.finalize()
        c_text = iv + c_text
        return c_text
    
    def __text_depadding(self, dc_text: bytes)->str:
        """
        Удаление отступов из расшифрованного текста.

        Params:
        dc_text (bytes): расшифрованный текст с дополнениями.

        Returns:
        str: расшифрованный текст без отступов.
        """
        unpadder = padding.PKCS7(128).unpadder()
        unpadder_dc_text = unpadder.update(dc_text) + unpadder.finalize()
        return unpadder_dc_text.decode('UTF-8')
    
    def decryption_text(self, c_text: bytes, key: bytes)->str:
        """
        Расшифровывание зашифрованного текста с помощью симметричного алгоритма.

        Params:
        c_text (bytes): Зашифрованный текст, который надо расшифровать.
        key (bytes): Ключ для расшифровки текста.

        Returns:
        str: Расшифрованный текст.
        """
        iv = c_text[:16]
        cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(c_text[16:]) + decryptor.finalize()
        unpadder_dc_text = self.__text_depadding(dc_text)
        return unpadder_dc_text
        