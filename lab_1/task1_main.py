import argparse
from task1 import start_to_encrypt

parser = argparse.ArgumentParser()

parser.add_argument('--path_to_text_file',
                    type=str,
                    default="text_task1",
                    help='Enter the path to the encrypted text file.(default: text_task1.txt')

parser.add_argument('--path_to_key_file',
                    type=str,
                    default='key_task1.txt',
                    help='Enter the path to the key file.(default: key_task1.txt')

if __name__ == "__main__":
    my_variables = parser.parse_args()
    start_to_encrypt(*(vars(my_variables).values()))

