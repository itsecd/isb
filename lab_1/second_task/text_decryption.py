import sys
sys.path.insert(1, '../first_task')
from work_w_files import read_file

sorted_alphabet=' ОИЕАНТСРВМЛДЯКПЗЫЬУЧЖГХФЙЮБЦШЩЭЪ'

def get_statistics(text: list[str])->list[str]:
    freq={}
    for line in text:
        for char in line:
            if char!='\n':
                freq[char]=freq[char]+1 if char in freq else 1
    return [elem[0] for elem in sorted(freq.items(),reverse=True)]

print(len(get_statistics(read_file('input.txt'))))
            
