import argparse
import re


def get_argcmd():
    """
    Запрашиваем у пользователя назваение файла и нужное имя

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='Filename')
    parser.add_argument('name', type=str, help='UserName')
    args = parser.parse_args()

    return args


def readingfile(filename: str) -> str:
    """
    Считываем информацию с файла
    :param filename: имя файла
    :return: информация с файла
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def numberofnames(name: str, file: str) -> int:
    """
    Функия, которая считает колличство анкет с именем, введенным пользователем
    :param name: имя для поиска
    :param file: содержимое файла
    :return:
    """

    pattern = f'Имя: {name}\s'
    match = re.findall(pattern, file)

    return len(match)


def main():
    try:
        args = get_argcmd()
        file = readingfile(args.file)
        Inputname = args.name
        print(f'Количество анкет с именем {Inputname}: {numberofnames(Inputname, file)}')
    except:
        print("Неправильное название файла")


if __name__ == '__main__':
    main()
