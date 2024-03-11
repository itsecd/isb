# Основы информационной безопасности

## Лабораторная №1 "Простейшие методы шифрований текстовых сообщений"

В лабораторной работе изучается метод кодирования текста шифром простой подстановки и декодирования при помощи частотного анализа 
текстовой последовательности. 

### Задание на лабораторную работу:
1. Закодировать любой связный текст (не менее 500 символов), любым произвольным шифром простой подстановки (моноалфавитная замена) или перестановки. 
2. Расшифровать текст из методички, закодированный шифром простой подстановки (моноалфавитная замена) в соответсвии со своим вариантом.

### Результаты выполнения лабораторной работы:

- исходные коды для выполнения обоих заданий лабораторной работы (подразумевается python), [cypher](modules\cypher.py),
    [decypher](modules\decypher.py)
- исходный шифруемый текст для задания 1 [src_text](texts\first_part\src_text.txt);
- результат шифрования текста для задания 1, [encrypted_text](texts\first_part\encrypted_text.txt);
- ключ шифрования текста для задания 1, [encryption_key](texts\first_part\encryption_key.json);
- исходный зашифрованный текст для задания 2 согласно варианту, [cod5](texts\second_part\cod5.txt);
- результат дешифровки текста для задания 2, [decrypted_text](texts\second_part\decrypted_text.txt);
- найденный ключ шифрования текста для задания 2. [encryption_key](texts\second_part\encryption_key.json).

### Инструкция работы с терминалом

- зашифровать текст шифром Цезаря              
    python main.py encrypt -m caesar -k 'texts\first_part\encryption_key.json' -inpf 'texts\first_part\src_text.txt' -outf 'texts\first_part\encrypted_text.txt'

- расшифровать текст методом Цезаря
    python main.py decrypt -m caesar -k 'texts\first_part\encryption_key.json' -inpf 'texts\first_part\encrypted_text.txt' -outf 'texts\first_part\decrypted_text.txt' 

- расшифровать текст методом частотного анализа
    python main.py decrypt -m frequency -k 'texts\second_part\encryption_key.json' -inpf 'texts\second_part\cod5.txt' -outf 'texts\second_part\decrypted_text.txt'



