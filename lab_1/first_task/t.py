from work_w_files import write_file, read_file

def encrypt_w_caesar_cipher(text:list[str],shift=5): 
    new_letters=[]
    for line in text:
        line.replace('ё','е')
        line.replace('Ё','Е')

    for line in text:
        for char in line:
            if(char>='а' and char<='я'):
                new_letters.append(chr((ord(char)+shift-ord('а'))%32+ord('а')))
            elif(char>='А' and char<='Я'):
                new_letters.append(chr((ord(char)+shift-ord('А'))%32+ord('А')))
            else:
                new_letters.append(char)
    return new_letters

with open("out.txt",'w', encoding='utf-8') as file:
    for char in (encrypt_w_caesar_cipher(read_file('input.txt'))):
        file.write(char)

    
print(encrypt_w_caesar_cipher(read_file('input.txt')))

