import argparse
import re


def get_filename() -> str:
    """
    считывание имени файла из командной строки
    :return: имя файла
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type = str)
    return parser.parse_args().filename


def read_file(filename: str) -> list:
    """
    считывание файла в список
    :param filename: имя файла
    :return: содержимое файла в виде списка
    """
    with open(filename, "r", encoding = "UTF-8") as file:
        return file.readlines()


def find_surname(lst: list[str]) -> list:
    """
    Поиск анкет с фамилией Иванов или Иванова
    :param lst: список анкет
    :return: список нужных анкет
    """
    pattern = r'Иванов[а]?'
    found_list = list()
    tmp = list()
    for i in range(len(lst)):
        if re.search(pattern, lst[i][9:-1]):
            for j in range(6):
                tmp.append(lst[i+j][:-1])
            found_list.append(tmp)
            tmp = []
    return found_list


def print_people(lst: list[list[str]]) -> None:
    """
    вывод анкет на экран, каждая анкета отделяется пустой строкой
    :param lst: список нужных анкет
    """
    for item in lst:
        for element in item:
            print(element)
        print()


def main():
    filename = get_filename()
    lst = read_file(filename)
    ivanov_list = find_surname(lst)
    print_people(ivanov_list)


if __name__ == "__main__":
    main()