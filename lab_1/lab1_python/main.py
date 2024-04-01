import func
import paths


def main():
    # Первая часть программы
    s, permutation = func.get_parse()
    permutation_arr = [a for a in permutation]
    new_s = func.encrypt(s, permutation_arr)
    func.write_file(paths.begin_text, s)
    func.write_file(paths.code, permutation)
    func.write_file(paths.encrypted_text, new_s)

    # Вторая часть программы
    s2 = func.read_file('encrypted_text2.txt')
    res = func.get_frequency(s2)
    for a in res:
        print(a)
    print()

    s_cor = func.get_correct_text(s2)

    res = func.get_frequency(s_cor)
    for a in res:
        print(a)
    print(s_cor)

    func.write_file(paths.decrypted_text2, s_cor)


if __name__ == '__main__':
    main()
