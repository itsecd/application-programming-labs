import argparse
from collections import Counter
import re


def openfile()-> str:
    """
    Parses the file name from the command line arguments.
    :return: file name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='your file')
    args = parser.parse_args()
    name=args.file
    return name


def read(filename: str) -> str:
    """
       Reading the contents of a file
       :param filename: file name
       :return: data from a file
       """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
        return text
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Ошибка: файл '{filename}'  не найден : {e}")
    print(text)


def pat(text:str)->list:
    """
    splits data from file and writes names in names
    :param text: Data from the file
    :return: list of names from a file
    """
    pattern = r'Имя:\s*([а-яА-Я]+)'
    names=re.findall(pattern,text)
    return names


def popular(name:list):
    """
    finds the most common name
    :param name:list of names
    :return:most common name
    """
    counter=Counter(name)
    return counter.most_common(1)[0]


def main():
    filename=openfile()
    text= read(filename)
    name=pat(text)
    counter=popular(name)
    print(counter)


if __name__ == "__main__":
    main()