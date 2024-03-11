import argparse

from modules.encryption_function import *

def main():
    parser = argparse.ArgumentParser(description='Text encryption and decryption')
    
    
    parser.add_argument('action', choices=[Mode.ENCRYPT.value, Mode.DECRYPT.value], 
                        help='choose an action: encrypt or decrypt') 
       
    parser.add_argument('-m', '--method', choices=[Method.CAESAR.value, Method.FREQUENCY.value], 
                        help='choose the decryption method: Caesar cipher,'
                          'or frequency analysis method')
    
    parser.add_argument('-k', '--key', type=str, 
                        help='the encryption key for Caesar encryption')
    
    parser.add_argument('-inpf', '--input_file',
                        help='the path to the text file')
    
    parser.add_argument('-outf', '--output_file',
                        help='the path to the file for writing the text')
    
    args = parser.parse_args()
    match args.method:
        case Method.CAESAR.value:
            encryption_or_decryption_Caesar(args.action, args.key, args.input_file, args.output_file)
        case Method.FREQUENCY.value:
            decryption_frequency_analysis(args.key, args.input_file, args.output_file)
        case _:
            raise ValueError("a non-existent method is selected")

  
    
if __name__ == '__main__':    
    main()
else: 
    print('Error')
