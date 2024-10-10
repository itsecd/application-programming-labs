import re
import argparse


def get_argcmd():

    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='Filename')
    parser.add_argument('name', type=str, help='UserName')
    args = parser.parse_args()

    return args


def readingfile(filename: str) -> str:

    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def numberofnames(name: str, file: str) -> int:

    pattern = f'Имя: {name}\s'
    match = re.findall(pattern, file)

    return len(match)


def main():
        file = readingfile(get_argcmd().file)
        Inputname = get_argcmd().name

        print(f'Количество анкет с именем {Inputname}: {numberofnames(Inputname, file)}')


if __name__ == '__main__':
    main()