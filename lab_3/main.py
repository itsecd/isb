import argparse

from modules.asymmetric import Asymmetric
from modules.symmetric import Symmetric
from modules import file_working

def clean_text_files(file_paths: list):
    """
    Очищение текстовых файлов, указанных в списке file_paths, от данных.

    Args:
    file_paths (list): Список путей к текстовым файлам, которые необходимо очистить.
    """
    for file_path in file_paths:
        try:
            with open(file_path, 'w') as file:
                file.write('')
            print(f"Файл '{file_path}' успешно очищен.")
        except FileNotFoundError:
            print(f"Ошибка: файл '{file_path}' не найден.")
        except IOError:
            print(f"Ошибка: не удалось открыть файл '{file_path}'.")


def actions_for_generating_keys(symmetric: Symmetric, asymmetric: Asymmetric, settings: dict)->None:
    symmetric.key_generation()
    symmetric.serialization_key(settings['symmetric_key'])

    asymmetric.generating_key_pair()
    asymmetric.serialization_private_key(settings['private_key'])
    asymmetric.serialization_public_key(settings['public_key'])

    print(f'Ключи сгенерированы и сериализованы в {settings["symmetric_key"], settings["private_key"], settings["public_key"]}')


def actions_to_encrypt_symmetric_key(symmetric: Symmetric, asymmetric: Asymmetric, settings: dict)->None:
    symmetric_key = symmetric.deserialization_key(settings['symmetric_key'])
    file_working.write_bytes_to_txt(asymmetric.encrypt_symmetric_key(symmetric_key, settings['public_key']), 
                                               settings['encrypted_symmetric'])            

    print(f'Симметричный ключ зашифрован в {settings["encrypted_symmetric"]}')


def actions_to_decrypt_symmetric_key(asymmetric: Asymmetric, settings: dict)->None:
    esymmetric_key = file_working.read_bytes(settings['encrypted_symmetric'])
    symmetric_key = asymmetric.decryption_symmetric_key(esymmetric_key, settings['private_key'])            
    file_working.write_bytes_to_txt(symmetric_key, settings['decrypted_symmetric'])

    print(f'Симметричный ключ расшифрован в {settings["decrypted_symmetric"]}')

def actions_for_encrypting_text(symmetric: Symmetric, settings: dict)->None:
    symmetric_key = symmetric.deserialization_key(settings['symmetric_key'])
    text = file_working.read_txt(settings['initial_file'])
    e_text = symmetric.text_encryption(text, symmetric_key)
    file_working.write_bytes_to_txt(e_text, settings['encrypted_text'])

    print(f'Текст зашифрован в {settings["encrypted_text"]}')

def actions_for_decrypting_text(symmetric: Symmetric, settings: dict)->None:
    dec_symmetric_key = symmetric.deserialization_key(settings['decrypted_symmetric'])
    text = file_working.read_bytes(settings['encrypted_text'])
    dec_text = symmetric.decryption_text(text, dec_symmetric_key)
    file_working.write_to_txt(dec_text, settings['decrypted_text'])

    print(f'Текст расшифрован в {settings["decrypted_text"]}')


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='Режим генерации ключей', action='store_true')
    group.add_argument('-enck', '--encryption_key', help='Шифрование симметричного ключа', action='store_true')
    group.add_argument('-deck', '--decription_key', help='Дешифрование симметричного ключа', action='store_true')
    group.add_argument('-enc', '--encryption', help='Режим шифрования текста', action='store_true')
    group.add_argument('-dec', '--decryption', help='Режим дешифрования текста', action='store_true')
    group.add_argument('-c', '--clear', help='Освобождение файлов с данными, кроме файла с исходным текстом', action='store_true')
    parser.add_argument('settings', type=str, help='Настройки', default='settings.json')

    args = parser.parse_args()
    
    symmetric = Symmetric()
    asymmetric = Asymmetric()

    settings = file_working.read_json('settings.json')
    
    match args:
        case args if args.generation:
            actions_for_generating_keys(symmetric, asymmetric, settings)

        case args if args.encryption:
           actions_for_encrypting_text(symmetric, settings)

        case args if args.encryption_key:
            actions_to_encrypt_symmetric_key(symmetric, asymmetric, settings)
            
        case args if args.decription_key:
            actions_to_decrypt_symmetric_key(asymmetric, settings)

        case args if args.decryption:
            actions_for_decrypting_text(symmetric, settings)

        case args if args.clear:
            clean_text_files([settings['decrypted_symmetric'], settings['decrypted_text'],
                              settings['encrypted_text'], settings['private_key'], 
                              settings['public_key'], settings['symmetric_key']])
            print("Все файлы очищены успешно")

        case _:
            print("Выберите режим работы!")
    

if __name__ == '__main__':
    main()
    