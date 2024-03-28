from functions_for_task1 import read_file_txt, encrypt_text, write_file, set_right_directory
# Импортировать consts необходимо именно после functions_for_task1,
# т.к. в functions_for_task1 меняется рабочая директория,
# что необходимо для правильной работы consts
import consts




if __name__ == "__main__":
    text = read_file_txt(consts.FILES["text_start"])
    key = read_file_txt(consts.FILES["key"])

    encrypt_text = encrypt_text(text, key)

    print(encrypt_text)

    write_file(consts.FILES["text_end"], encrypt_text)



