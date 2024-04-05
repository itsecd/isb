import func
import paths


def main():
    dict_ = func.get_dict_from_md('paths2.md')

    # Первая часть программы
    s, permutation = func.get_parse()
    permutation_arr = [a for a in permutation]
    new_s = func.encrypt(s, permutation_arr)
    func.write_file(dict_['begin_text'], s)
    func.write_file(dict_['code'], permutation)
    func.write_file(dict_['encrypted_text'], new_s)

    # Вторая часть программы
    s2 = func.read_file(dict_['encrypted_text'])
    res = func.get_frequency(s2)
    for a in res:
        print(a)
    print()

    s_cor = func.get_correct_text(s2, dict_['before_perm'], dict_['after_perm'])

    res = func.get_frequency(s_cor)
    for a in res:
        print(a)
    print(s_cor)

    func.write_file(dict_['encrypted_text2'], s_cor)


if __name__ == '__main__':
    main()
