from decryption.D_ReplaceOneLetter import D_ReplaceOneLetter as DCrypt

try:
    with open('Solution2/encode.txt', 'r') as file:
        text = file.read()

    text = text.replace("\n", "")

    decryptor = DCrypt(text)


    with open('Solution2/encode.txt', 'r') as file:
        text = file.read()


    with open('Solution2/alphabet_for_program.txt', 'r') as file:
        goodAlphabet = file.read()

    print("\nШифр:")
    print(text)
    translate = decryptor.decryptionSortFrequency(goodAlphabet)

    print("\nАнализ:")

    for i in range(1, 20):
        lenth = decryptor.countWordSizeInText([">"], i)
        if lenth != 0:
            average = decryptor.wordSizeInTextFrequency([">"], i)
            print(f"\n{i}, {lenth}, {average}")
            print(decryptor.splitTextBySize([">"], i))
            print(DCrypt.splitTextBySize_s(translate, ["_"], i))


    print("\n\n-----------------------------------------------------------------------\n\n")

    dic = decryptor.getTranslateDictFrequency(goodAlphabet)
    print(decryptor.analysisTextAndSortFrequency())
    print('\n')
    print(list(dic.keys()))
    print(list(dic.values()))

    print("\nПрименим ключ:")
    print("\n" + translate)

    with open('Solution2/translate.txt', 'w') as file:
        file.write(translate)


    dic = decryptor.sortDictValues_s(decryptor.getTranslateDictFrequency(goodAlphabet))
    alphabet = ''.join(dic.values())[::-1]
    key = ''.join(dic.keys())[::-1].replace(" ", "_")

    with open('Solution2/alphabet.txt', 'w') as file:
        file.write(alphabet)

    with open('Solution2/key.txt', 'w') as file:
        file.write(key)
except Exception as ex:
    print(ex)
finally:
    print("\nУспешно\n")