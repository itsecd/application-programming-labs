import datetime
import argparse
import re


def get_file_name() -> str:
    """
    Parses the file name from the terminal arguments (the 'argparse' module)
    :return: the name of file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name of file')
    args = parser.parse_args().filename
    return args


def reading(filename: str) -> str:
    """
    reads data from the file
    :param filename: name of file
    :return: data from the file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def bd(data: str) -> list:
    """
    creates the list of birthdays
    :param data: data about people
    :return: the list of bithdays ("DD.MM.YYYY")
    """
    bdlist = re.findall("\\d\\d.\\d\\d.\\d\\d\\d\\d",data)
    return bdlist


def task_f(bd_list: list) -> int:
    """
    counts the number of people from 30 to 40
    :param bd_list: the list of birthdays
    :return: the number of people from 30 to 40
    """
    k= 0
    for birthday in bd_list:
        realbd= datetime.datetime.strptime(birthday, '%d.%m.%Y')
        diff = datetime.datetime.now() - realbd
        if 30 <= (diff.days / 365) <= 40:
            k+= 1
    return k


def main():
    filename = get_file_name()
    data = reading(filename)
    bd_list =bd(data)
    task =task_f(bd_list)
    print('Количество людей возрастом от 30 до 40 лет:', task)


if __name__ == "__main__":
    """checking that the code executes as the main module"""
    main()

