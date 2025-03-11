import json
from file import open_file
from file import save
from code import caesar_code
from decode import*


def main():

    cfg = open_file("settings.json")

    key_ = open_file("key.json")

    text1 = open_file(cfg['input_file'])

    code_text = caesar_code(text1, key_['shift'], cfg['alphabet_ru'])

    save(cfg['output_file'], code_text)



    cfg2 = open_file("settings2.json")

    russian_freq = open_file("freq.json")

    text2 = open_file(cfg2['input_file'])

    my_freq = calculate_frequencies(text2)

    save(cfg2['freq'], my_freq)

    key = create_key(russian_freq, my_freq)

    save(cfg2['key'],key)

    final_text = decode_text(text2,key)

    save(cfg2['output_file'], final_text)

if __name__ == "__main__":
    main()


