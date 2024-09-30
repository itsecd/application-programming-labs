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

def find_popular_name(content: str) -> str:

    """
    Finds the most popular name of a file.

    The most_common(n) method is used, which returns a list of one element,
    which occurs most often, in the form of a tuple (element, quantity)

    :param content: A string containing the text from which names will be extracted.
    :return: A string indicating the most popular name and its count in the text.
    """

    pattern = re.compile(r"Имя: (\w+)")
    names = re.findall(pattern, content)

    n_count = Counter(names)
    popname, count = n_count.most_common(1)[0]

    return f"Most popular name is {popname} and count is {count}"

def main():
    filename = get_filename()
    content = reading(filename)
    result = find_popular_name(content)
    print(result)

if __name__ == "__main__":
    main()