from decryption.D_ReplaceOneLetter import D_ReplaceOneLetter as DCrypt

with open('Solution2/encode.txt', 'r') as file:
    text = file.read()

text = text.replace("\n", "")
decryptor = DCrypt(text)

# алфавит основанный на вероятности, так как decryptor имеет функции для вероятностей
testAlphabet = "_ОИЕАНТСРВМЛДЯКПЗЫЬУЧЖГХФЙЮБЦШЩЭ"

# расшифрованный ключ для вероятностей на основе частотного анализа подробнее как его получили 
# смотри Solution2.ipynb, а также см. файл Solution2/history.txt - представлены замены символов
# которые использовались в функциях замены 
goodAlphabet = "_ОЕТИАСНВЛРМПДКЯГЧЖЫБЮЬЙЦЩЭХУЗФШ"


print("С неправильным ключом вероятности:")
print(text)
translate = decryptor.decryptionSortFrequency(testAlphabet)
print("\n" + translate)

print("\nС правильным ключом вероятности:")
print(text)
translate = decryptor.decryptionSortFrequency(goodAlphabet)
print("\n" + translate)

with open('Solution2/translate.txt', 'w') as file:
    file.write(translate)

dic = decryptor.sortDictValues_s(decryptor.getTranslateDictFrequency(goodAlphabet))

alphabet = ''.join(dic.values())[::-1]
key = ''.join(dic.keys())[::-1].replace(" ", "_")

with open('Solution2/key_and_alphabet.txt', 'w') as file:
    file.write("alphabet:\n" + alphabet + "\nkey:\n" + key)