import argparse
import re
from collections import Counter


def get_filename() -> str:
    """
    Parses the command line argument to get the filename
    :return: The filename
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='The name of the file')
    args = parser.parse_args().filename
    return args


def reading(filename: str) -> str:
    """
     Reads the contents of a file and returns it as a string.
    :param filename: The filename
    :return: The content of the file as a string
    """
    with open(filename,'r', encoding = 'utf-8') as file:
        return file.read()


def find_popular_name(content: str) -> tuple:
    """
    Finds the most popular name of a file.
    :param content: A string containing the text from which names will be extracted.
    :return: A tuple containing the most popular name and its count.
    """
    pattern = re.compile(r"Имя: (\w+)")
    names = re.findall(pattern, content)
    n_count = Counter(names)
    popname, count = n_count.most_common(1)[0]
    return popname, count


def main():
    filename = get_filename()
    content = reading(filename)
    popname, count = find_popular_name(content)
    print(f"Most popular name is {popname} and count is {count}")


if __name__ == "__main__":
    main()
