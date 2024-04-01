import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', dest='text', help='Текст для зашифровки', type=str)
    parser.add_argument('-p', dest='permutation', help='Перестановка текста', type=str)
    args = parser.parse_args()
    print(args.text)
    print(args.permutation)


if __name__ == '__main__':
    main()
