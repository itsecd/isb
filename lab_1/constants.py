import json

RU_ALPH = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

PATHS = 'paths.json'

def load_json(file_name) -> dict:
    """
    reading json file

    :param file_name:
    :return:
    """

    with open(file_name, 'r') as file:
        return json.load(file)

paths_dict = load_json('paths.json')

T1_COMMON_TEXT = paths_dict['t1_common_text']
T1_ENCRYPTED_TEXT = paths_dict['t1_encrypted_text']
T2_COD8 = paths_dict['t2_cod8']
T2_KEY = paths_dict['t2_key']
T2_DECIPHER_TEXT = paths_dict['t2_decipher_text']
