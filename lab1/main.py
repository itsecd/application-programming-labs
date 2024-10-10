import argparse
import re


def get_arguments() -> tuple:
    """
    Get filename and user name from command line arguments.
    :return:  filename and user name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name of file')
    parser.add_argument('name', type=str, help='User name')
    args = parser.parse_args()
    return args.filename, args.name.lower()


def reading(filename: str) -> str:
    """
    Reads data from the file
    :param filename: name of file
    :return: data from the file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def namelist(data: str) -> list:
    """
    Create a list of names and the substring "Имя,", then remove the substrings "Имя."
    :param data: data from file
    :return: list of names
    """
    namelist = re.findall(r"Имя:\s*(\w+)", data)
    namelist = [i.lower() for i in namelist]
    return namelist


def input_name() -> str:
    """
    The user enters a name via command line arguments.
    :return: name provided by the user
    """
    parser = argparse.ArgumentParser(description='Enter your name via command line.')
    parser.add_argument('name', type=str, help='Your name')
    args = parser.parse_args()
    return args.name.lower()


def countnames(namelist: list, input_name: str) -> int:
    """
    Counting the number of names
    :param namelist: list of names
    :param input_name: name by user
    :return: count of names
    """
    return namelist.count(input_name)


def main():
    filename, inputname = get_arguments()
    data = reading(filename)
    nl = namelist(data)
    print(countnames(nl, inputname))


if __name__ == "__main__":
    """Checking that the code executes as the main module"""
    main()
