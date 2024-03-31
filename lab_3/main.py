import os
import logging
import tabulate
import argparse

import src.hybrid_tripleDES as hybrid

import src.serialization as ser
from src.encryption_algorithms.TypeArgument import TypeArgument

from src.consts import DEFAULT_KEY_SIZE_ASYMMETRIC
from src.encryption_algorithms.consts import DEFAULT_KEY_BYTES_FOR_TRIPLEDES, KEY_COUNT_BITS_FOR_TRIPLEDES

def main():
        
    try:
        
        parser = generate_args()
        args = parser.parse_args()
        
        if args.safe_logs:        
            logging.basicConfig(
                filename=args.safe_logs,
                filemode='w',
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(name)s:%(lineno)d - %(message)s')
            logger = logging.getLogger("main")
        
        if args.generate_keys:
            
            symmetrical_encrypted, private_key = hybrid.generate_hybrid_tripleDes(args.len_rsa_key, 
                                                                                  args.len_symmetrical_key, 
                                                                                  args.type_len_symmetrical)
            ser.safe_private_key(args.file_private_key, 
                                 private_key)
            ser.safe_symmetricTripleDES(args.file_encrypted_symmetric_key, 
                                        symmetrical_encrypted)

        elif args.encrypt:
    
            private_key = ser.read_private_key(args.file_private_key)
            symmetrical_encrypted = ser.read_symmetricTripleDES(args.file_encrypted_symmetric_key)
            text = ser.read_bytes(args.file_input)
            
            cipher = hybrid.encrypt_text(text, symmetrical_encrypted, private_key)
            ser.safe_bytes(args.path_object_output, cipher)
            
        elif args.decryption:

            private_key = ser.read_private_key(args.file_private_key)            
            symmetrical_encrypted = ser.read_symmetricTripleDES(args.file_encrypted_symmetric_key)
            cipher = ser.read_bytes(args.file_input)
            
            transalte = hybrid.decrypt_cipher(cipher, symmetrical_encrypted, private_key)
            ser.safe_bytes(args.path_object_output, transalte)        
    
    except Exception as e:
        
        if logger:
            logger.error(f"ERROR: {e}")
        else:
            raise RuntimeError("Very bad, cloun", e)
        
    finally:
        
        if args.safe_logs and args.logs_pretty:
            with open(args.safe_logs, 'r') as f:
                logs = f.readlines()

            table = tabulate.tabulate(
                [log.split(' - ') for log in logs],
                headers=['Time', 'Level', 'File', 'Message'],
                tablefmt='fancy_grid'
            )

            with open(args.safe_logs, 'w') as f:
                f.write(table)

def generate_args() -> argparse.ArgumentParser:
    
    parser = argparse.ArgumentParser(description="Single entry point for key generation, encryption, and decryption.")
    
    group = parser.add_mutually_exclusive_group(required=True)
    
    group.add_argument('-gen', '--generate_keys',
                       action='store_true',
                       help='Run key generation mode.')
    
    group.add_argument('-enc', '--encrypt',
                       action='store_true',
                       help='Run encryption mode.')
    
    group.add_argument('-dec', '--decryption',
                       action='store_true',
                       help='Run decryption mode.')
    
    
    parser.add_argument('-fpk', '--file_private_key',
                        type=str,
                        default=os.path.join("private_key.pem"),
                        help=f'Path to file private key hybrid default:({os.path.join("private_key.pem")})')
    
    parser.add_argument('-fsk', '--file_encrypted_symmetric_key',
                        type=str,
                        default=os.path.join("encrypted_symmectrical.pkl"),
                        help=f'Path to file encrypted symmetrical key hybrid default:({os.path.join("encrypted_symmectrical.pkl")})')


    parser.add_argument('-x', '--file_input',
                        type=str,
                        default=os.path.join("input.int"),
                        help=f'Path to read decode file.txt default:({os.path.join("input.int")})')
    
    parser.add_argument('-o', '--path_object_output',
                        type=str,
                        default=os.path.join("output.out"),
                        help=f'Path to safe output hybrid default:({os.path.join("output.out")})')
    
    
    parser.add_argument('-lrsa', '--len_rsa_key',
                        type=int,
                        default=DEFAULT_KEY_SIZE_ASYMMETRIC,
                        help=f'Size key rsa for generate default({DEFAULT_KEY_SIZE_ASYMMETRIC}).')
    
    parser.add_argument('-lsym', '--len_symmetrical_key',
                        type=int,
                        default=DEFAULT_KEY_BYTES_FOR_TRIPLEDES,
                        help=f'Size key symmetrical in byte for generate using:[{KEY_COUNT_BITS_FOR_TRIPLEDES}] bits default:{DEFAULT_KEY_BYTES_FOR_TRIPLEDES} byte.')
    
    parser.add_argument('-tl', '--type_len_symmetrical',
                        type=TypeArgument,
                        default=TypeArgument.BYTE,
                        help=f'Size key symmetrical in byte for generate using:[{TypeArgument.BIT} = bit, {TypeArgument.BYTE} = byte] bits default:{TypeArgument.BYTE} byte.')
    
    
    parser.add_argument('-l', '--safe_logs',
                        type=str,
                        default=None,
                        help=f'Path to the file safe logs default({os.path.join(__name__ + ".log")}).')

    parser.add_argument('-lp', '--logs_pretty',
                        type=bool,
                        default=False,
                        help=f'Path to the file safe pretty logs default({os.path.join(__name__ + ".log")}).')
    return parser

if __name__ == "__main__":
    try:
       
        main()
        
    except Exception as e:
        
        print(e)