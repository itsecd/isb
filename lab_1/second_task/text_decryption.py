import sys
sys.path.insert(1, '../first_task')
from work_w_files import read_file

def get_statistics(text: list[str])->list[str]:
    freq={}
    for char in text:
        if char!='\n':
            freq[char]=freq[char]+1 if char in freq else 1
    return [elem[0] for elem in sorted(freq.items(),key=lambda item:item[1], reverse=True)]

def get_new_text(text: list[str])->list[str]:
    for line in text:
        for i in range(len(sorted_alphabet)):
            print(line.replace(get_statistics(text)[i],sorted_alphabet[i]))
    return text


            
