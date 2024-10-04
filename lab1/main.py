import argparse
import os
import re

def parser_() -> str:
    """
    Parses the name of file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name of your file')
    args = parser.parse_args().filename
    return args


def read_file(filename: str)-> str:
    """
    Read file and get text
    :param filename: the name of file
    :return: a string consists of data
    """
    if not os.path.exists(filename):
        raise FileNotFoundError('file not found')

    if not filename.endswith('.txt'):
        raise ValueError('this file is not txt file')

    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        return text


def get_bd(text: str)->list:
    """
    Get birthday date from data
    :param text: text that we got from file
    :return: list of birthday date
    """
    bd_pattern = r'\d\d.\d\d.\d\d\d\d'
    bd_list = re.findall(bd_pattern, text)
    return bd_list


def bd_count(bd_list: list)->int:
    """
    Count people who was born in 21 centry
    :param bd_list: list with birthday dates
    :return: the count of people
    """
    c = 0
    for i in range(len(bd_list)-1):
        bd = int(bd_list[i].split('.')[2])
        if bd>2000:
            c+=1
    return c

def main():
    filename = parser_()
    try:
        text = read_file(filename)
        bd_list = get_bd(text)
        print(bd_count(bd_list))

    except FileNotFoundError as f:
        print(f)
    except ValueError as v:
        print(v)

if __name__ == "__main__":
    main()