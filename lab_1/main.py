import argparse
import re

def parsers():
    """
        Parses the file name from the terminal arguments
        using the 'argparse' module.
        :return: The file name
        """
    parser = argparse.ArgumentParser()  # создание экземпляра парсера
    parser.add_argument('name', type=str)  # добавление позиционного аргумента командной строки
    return parser.parse_args().name


def read(name : str) -> str:
    """
       Reads the contents of the file.
       :param name: The file name
       :return: The file contents
       """
    with open(name, "r", encoding="utf-8") as file:
        filename = file.read()
        return filename


def countable(data: str):
    """
       Using the 're' module, it finds all the men in the list
       and returns their number.
       :param data: The file contents
       :return: The number of male profiles
       """
    pattern = r"\s?Мужской" # шаблон
    numbers = re.findall(pattern, data)
    return numbers


def main():
    name = parsers()
    try:
        data = read(name)
        if len(countable(data)) == 0:
            print("no one man in file")
        print("the count of men: ", len(countable(data)))
    except FileNotFoundError:
        print(f"File '{name}' not found.")

if __name__ == "__main__":
    main()





