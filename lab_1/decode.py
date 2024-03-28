import json
from read_and_write_file import read_from_file, write_to_file
from part_2 import path

def get_dict(input_path: str, output_path: str) -> None:
    """
    Вывести информацию о частоте каждого символа.
    Arguments:
        input_path: Путь к тексту, который нужно декодировать. Тип str.
        output_path: Путь к файлу для сохранения результатов. Тип str.
    Return:
        None
    """
    try:
        data = read_from_file(input_path)
        my_dict = {}
        freq_dict={}
        for char in data:
            if char in my_dict:
                my_dict[char] = (int(my_dict.get(char)) + 1) 
            else:
                my_dict[char] =  1
        total_chars = len(data)
        for key, val in my_dict.items():
            freq_dict[key]=val/total_chars
        sorted_dict = dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))
        with open(output_path,"w") as freq_file:
            freq_file.write(json.dumps(sorted_dict,indent=1,ensure_ascii=False))
    except Exception as ex:
        raise Exception(f"Error when creat and save to dictionary!\n Exception:{ex}\n")


def decode_text(original_text_path: str, key_path: str, decode_text_path: str) -> None:
    """
    Расшифровать текст.
    Arguments:
        original_text_path: Путь к файлу, в котором есть исходный текст необходимо расшифровать. Тип str.
        key_path: ключ расшифровки. Тип str.
        decode_text_path: Путь к файлу, в котором содержит расшифрованный текст. Тип str.
    Return:
        None
    """
    try:
        data = read_from_file(original_text_path)
        with open(key_path, "r", encoding="utf-8") as key_file:
            key_dict = json.load(key_file)
        for key, value in key_dict.items():
            if key in data:
                data = data.replace(key, value)
        write_to_file(decode_text_path, data)
    except Exception as ex:
        raise Exception(f"Error when decode text!\n Exception:{ex}\n")


if __name__ == "__main__":
    input_file_path, freq_dict_path, key_dict_path, output_file_path = path.path_settings()
    try:
        get_dict(input_file_path,freq_dict_path)
        decode_text(input_file_path,key_dict_path,output_file_path)
        print("Text successfully decrypted and saved")
    except Exception as ex:
        raise Exception(f"Error when decode!\n Exception:{ex}\n")