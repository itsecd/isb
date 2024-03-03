from encryption.Vigener import Vigener as badEncoder


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