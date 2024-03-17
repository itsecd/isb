import argparse

from src.Encryption.decryption.D_ReplaceOneLetter import D_ReplaceOneLetter as DCrypt
           
CONST_LETTERS_MAX_IN_ENCODE = 20
            
def main():
    
    
    parser = argparse.ArgumentParser(description='Программма для шифрации Энигмой по ключу')
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--alphabet', type=str, help='Алфавит для дешифрации')
    group.add_argument('-fta', '--fileForTxtAlphabet', type=str, help='Путь к файлу алфавита для дешифрации .txt')
    
    parser.add_argument('-x', '--encodeFile', type=str, help='Путь к файлу шифра')
    parser.add_argument('-o', '--fileForExport', type=str, help='Название файла вывода(перезапишет существующий)')
    parser.add_argument('-dc', '--characterDelimetrInCihep', type=str, help='Символ разделитель в шифре')
    parser.add_argument('-e', '--exportKeyJson', type=str, help="Экспорт ключа в файл")
    
    args = parser.parse_args()
    
    if args.alphabet:
        goodAlphabet = args.alphabet
    elif args.fileForTxtAlphabet:
        with open(args.fileForTxtAlphabet, "r") as f:
            goodAlphabet = f.read()
        
    with open(args.encodeFile, 'r') as file:
        text = file.read()
    text = text.replace("\n", "")
    
    decryptor = DCrypt(text)
    
    print("-------------------------------------------------------------------------------")
    print("\n\nЧастота:\n")

    print(decryptor.analysisTextAndSortFrequency())
    
    print("-------------------------------------------------------------------------------")
    print("\nЗамены:")
    print()
    forWatch = decryptor.getTranslateDictFrequency(goodAlphabet)
    print(list(forWatch.keys()))
    print(list(forWatch.values()))
    print()
    print(forWatch)
    
    print("-------------------------------------------------------------------------------")
    print("\n\nРасшифровка:\n")
    print(text)
    translate = decryptor.decryptionSortFrequency(goodAlphabet)
    print()
    print(translate)
    
    if args.characterDelimetrInCihep and len(args.characterDelimetrInCihep) == 1:
        print("-------------------------------------------------------------------------------")
        print("\nАнализ: (кол-во символов, кол-во слов, частота всех слов)")
        for i in range(1, CONST_LETTERS_MAX_IN_ENCODE):
            lenth = decryptor.countWordSizeInText([args.characterDelimetrInCihep], i)
            if lenth != 0:
                average = decryptor.wordSizeInTextFrequency([args.characterDelimetrInCihep], i)
                print(f"\n{i}, {lenth}, {average}")
                print(decryptor.splitTextBySize([args.characterDelimetrInCihep], i))
                print(DCrypt.splitTextBySize_s(translate, [forWatch[args.characterDelimetrInCihep]], i))
    
    if args.exportKeyJson:
        decryptor.export_KeyJSON(goodAlphabet, args.exportKeyJson)
    
    with open(args.fileForExport, 'w') as file:
        file.write(translate)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Ошибка", e)
