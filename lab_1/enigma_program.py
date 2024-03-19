import argparse

from typing import Dict

import src.encryption.encryptors.enigma as eni

STANDART_SEED="x(ГkшЪ+4sЩJpШ)0,хRCЕD`ьQEрP2уйXыj.HЙGгЖж*фЭzhfgч№VFтцСtмнХ ЗТ}KЛ%»-Y1ПУ{кMНв3!oZепД;ЦS7:iu#яcЮmO]dОАзъ@8бБqлР/о'«9ЧvAщynЬbЁ[UаI~LewюКэaМд56B&TWФиЯЫё^ВNсrlИ="

def generateCommand(parser: argparse.ArgumentParser):
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-k', '--key', type=str, help='Key for text (random set of characters)')
    group.add_argument('-pk', '--pathKey', type=str, help='Path to the file for text')

    parser.add_argument('-x', '--fileToText', type=str, help='Path to the text file')
    parser.add_argument('-o', '--fileForExport', type=str, help='Output file name (will overwrite existing)')
    parser.add_argument('--translate', type=bool, default=False, help='Encrypt text')
    parser.add_argument('-e', '--exportKeyTxt', type=str, help="Export key to file")

    group2 = parser.add_mutually_exclusive_group(required=True)
    group2.add_argument('-s', '--seed', type=str, help="Seed for key generation")
    group2.add_argument('-sft', '--seedFileTxt', type=str, help="Seed for key generation in a file")
    
    return

def getArgs(parser: argparse.ArgumentParser) -> dict:
    
    args = parser.parse_args()
    
    with open(args.fileToText, 'r') as f:
        text = f.read()
        
    if args.seed:
        seed = args.seed
    elif(args.seedFileTxt):
        with open(args.seedFileTxt, 'r') as f:
            seed = f.read()
    else:
        seed = STANDART_SEED

    if args.key:
        key = args.key
    elif args.pathKey:
        with open(args.pathKey, 'r') as f:
            key = f.read()
    
    translate = parser.parse_args().translate
    exportKey = parser.parse_args().exportKeyTxt
    return {"text": text, "seed": seed, "key": key, "translate" : translate, "export": exportKey}


def main():


    parser = argparse.ArgumentParser(description='Program for encrypting with Enigma using a key')

    generateCommand(parser)


    args = getArgs(parser)
    
    en = eni.Enigma.createEnigmaIntoKey(key=args["key"], seed=args["seed"])

    if args["translate"]:
        cihep = en.translateUpdateRotors(args["text"])
    else:
        cihep = en.encryptUpdateRotors(args["text"])
    
    if args["export"]:
        with open(args["export"], 'w') as file:
            file.write(args["export"])

    with open(parser.parse_args().fileForExport, 'w') as file:
        file.write(cihep)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Ошибка: ", e)
        

