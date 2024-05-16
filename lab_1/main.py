from functions_helpers import *

PATHS = 'paths.json'
paths_dict = json_loader('paths.json')

T1_TEXT = paths_dict['t1_text']
T1_TEXT_CODE = paths_dict['t1_text_code']
T2_COD3 = paths_dict['t2_cod3']
T2_KEY = paths_dict['t2_key']
T2_TEXT = paths_dict['t2_text']

def caesar_cipher_16(string: str) -> str:
    """ coding text using caesar cipher with shift 16 """
    result = ""
    for char in string:
        if char.isalpha():
            if char.lower() <= 'п':
                result += chr(ord(char) + 16)
            else:
                result += chr(ord(char) - 16)
        else:
            result += char
    return result


def encrypted_text_symbols_frequency(path: str) -> dict:
    """ symbols frequency in the text for dictionary """
    text_code = reader(path)

    data_smbls = dict()
    for key_smbls in set(text_code):
        symbol_count = text_code.count(key_smbls)
        item = float(round(symbol_count / len(text_code), 6))
        data_smbls[key_smbls] = item
    return data_smbls


def symbols_frequency_data(path: str) -> dict:
    """ function count data about symbols frequency """
    file_read = reader(path)
    list_of_frequency = file_read.split('\n')

    smbls = []
    smbls_count = []

    for i in range(len(list_of_frequency)):
        smbls.append(list_of_frequency[i][0])
        smbls_count.append(float(list_of_frequency[i][4:12]))

    data = dict(zip(smbls, smbls_count))

    for i, key_smbls in enumerate(smbls):
        data[key_smbls] = smbls_count[i]
    return data


def func_for_code_my_text(path_code: str, path_read: str) -> None:
    """ function is coding my text to 'path_read' """
    writer(path_code, caesar_cipher_16(reader(path_read)))


def func_for_decoding_cod3(path_text_code: str, path_key: str, path_write_file: str) -> None:
    """ function is decoding 'cod3' using key """
    text_code = reader(path_text_code)
    key = json_loader(path_key)

    ret_str = ''
    for char in text_code:
        ret_str += key[char]

    writer(path_write_file, ret_str)


def main(path_file_write_1: str, path_file_read_1: str, path_encrypted_text_2: str,
         path_key_2: str, path_write_file_2: str) -> None:
    """ function launch writer to task 1 and  func_helper for task 2 """
    try:
        func_for_code_my_text(path_file_write_1, path_file_read_1)
        func_for_decoding_cod3(path_encrypted_text_2, path_key_2, path_write_file_2)
    except Exception as e:
        print('error', e)


if __name__ == '__main__':
    """ go when file is going """
    main(T1_TEXT_CODE, T1_TEXT,
         T2_COD3, T2_KEY, T2_TEXT)
