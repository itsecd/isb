from constants import *
from encrypt_text_with_key import *
from frequency_analysis import *
from merge_key import *
from create_caesar_key import *

if __name__ == "__main__":
    create_caesar_key(11, key1)
    encrypt_text_with_key(text1, key1, encrypted_text)
    frequency_analysis(cipher, probabilities)
    merge_key(ru, probabilities, key2)
    encrypt_text_with_key(cipher, key2, unsecret_text)