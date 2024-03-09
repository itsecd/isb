# with open("input.txt",'r', encoding='utf-8') as file:
#     lines=file.readlines()

# new_letters=[]
# rot=5
# for line in lines:
#     for char in line:
#         if (char>='А' and char<='Я'):
#             new_letters.append(chr((ord(char)-ord('А')+1+rot)%33+ord('А')))
#         elif (char>='а' and char<='е'):
#             new_letters.append(chr((ord(char)-ord('а')+rot+1)%33+ord('а')))
#         elif (char>'е' and char<='я'):
#             new_letters.append(chr((ord(char)-ord('а')+rot+2)%33+ord('а')))
#         else:
#             new_letters.append(char)
# print(new_letters)
letter = 'А'
while(letter<='я'):
    print(f'"{letter}"')
    letter=chr(ord(letter)+1)
# with open("otus.txt", "w", encoding='utf-8') as file:
#     for char in new_letters:
#         file.write(char)
