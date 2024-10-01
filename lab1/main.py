import argparse
import re


def get_file_name() -> str:

    """
    Extracts the file name from the command line arguments using the 'argparse' module
    :return:the file name
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name of file')
    args = parser.parse_args().filename
    return args


def reading(filename: str) -> str:
    """
    reads data from the file
    :param filename: name of file
    :return:data from the file
    """

    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def namelist(data:str) -> list:
    """
    Create a list  of names and the substring "Name," then remove the substrings "Name."
    :param data: data from file
    :return: list of names
    """
    namelist = re.findall("Имя: \\w+", data)
    namelist = [i.replace("Имя: ", "") for i in namelist]
    namelist = [i.lower() for i in namelist]
    return namelist

def input_name() -> str:
    """
    The user enters a name.
    :return: name by user
    """
    inputname = input("Enter name: ")
    inputname = inputname.lower()
    return inputname

def countnames(namelist: list, input_name: str) -> int:
    """
    Counting the number of  names
    :param namelist: list of names
    :param input_name: name by user
    :return: count of names
    """
    count = 0
    for string in namelist:
        if string == input_name:
            count += 1
    return count



def main():

    filename = get_file_name()
    data = reading(filename)
    nl = namelist(data)
    inputname = input_name()
    print(countnames(nl, inputname))


if __name__ == "__main__":
    """checking that the code executes as the main module"""
    main()





    