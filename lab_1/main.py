import argparse
import re


def get_filename() -> str:
    """
    Parses the filename from terminal

    :return: filename
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name of your file')
    args = parser.parse_args().filename
    return args


def read(filename: str) -> str:
    """
    Reads the contents of a file

    :param filename: the filename
    :return: contents of a file
    """
    with open(filename, "r", encoding='UTF-8') as file:
        return file.read()


def find_birthdays(data: str) -> list:
    """
    Find the birthday dates from file and creates list of them

    :param data: data about people
    :return: list of birthdays
    """
    bd_list = re.findall("\\d\\d.\\d\\d.\\d\\d\\d\\d", data)
    return bd_list


def find_21cent(bd_list: list) -> int:
    """
    Find people who was born in the 21st century

    :param bd_list: list of birthdays
    :return: the number of people who was born in 21st century
    """
    count = 0
    for i in bd_list:
        if int(i[-4::]) > 2000:
            count += 1
    return count


def main():
    filename = get_filename()
    data = read(filename)
    bd_list = find_birthdays(data)
    print(find_21cent(bd_list))


if __name__ == "__main__":
    """
    checking that the code executes as the main module
    """
    main()
