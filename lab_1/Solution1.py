# from encryption.Vigener import Vigener as badEncoder
from encryption.Vigener import Vigener as badEncoder



try:
    with open('Solution1/key.txt', 'r') as file:
        key = file.read()

    with open('Solution1/text.txt', 'r') as file:
        text = file.read()

    with open('Solution1/alphabet.txt', 'r') as file:
        alphabet = file.read()


    encoder = badEncoder(alphabet, key)
    encode = encoder.encrypt(text)
    translate = encoder.translate(encode)

    with open('Solution1/cipher.txt', 'w') as file:
        file.write(encode)

    with open('Solution1/translate.txt', 'w') as file:
        file.write(translate)
except Exception as exp:
    print("\n\nСмотри файлы, како возможно неправильно указал названия" + "\n\nОшибка:" + exp)
except:
    print("\n\nСмотри файлы, како возможно неправильно указал названия")
finally:
    print("Успешно")
