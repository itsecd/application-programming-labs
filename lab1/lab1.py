import argparse
import datetime
import re

def get_name_of_file() -> str:
    """
    Getting filename
    :return: name of file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='input name of your file')
    args = parser.parse_args()
    return args.filename


def read_file(filename: str) -> str:
    """
    Getting data from file
    :param filename: filename
    :return: file data
    """
    with open(filename, "r") as file:
        return file.read()


def get_codes(data: str) -> list:
    """
    Compilating list of codes
    :param data: original data
    :return: list of codes
    """
    pattern = re.findall('\\+7 927', data)
    return pattern


def count_codes(pattern: list) -> int:
    """
    Counting codes
    :param pattern: list of codes
    :return: Count of numbers
    """
    count = 0
    for code in pattern:
        count += 1
    return count


def main():
    filename = get_name_of_file()
    data = read_file(filename)
    codes = get_codes(data)
    count_of_codes = count_codes(codes)
    print(count_of_codes)


if __name__ == "__main__":
    main()
