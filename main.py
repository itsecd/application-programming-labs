import argparse
import re


def open_file(filename: str):
    """
    The Function opens and reads a file
    :param filename: name file
    :return: file contents as a string
    """
    with open(filename, "r", encoding="UTF-8") as file:
        return file.read()


def split(filename: str) -> list[str]:
    """
    The Function splits a string into substrings
    :return: list of questionnaires separately
    """
    pattern = r'\d+' + r'[)]' + '\n'
    return re.split(pattern, filename, maxsplit=0)


def parsing() -> str:
    """
    Parse command line arguments and returns the file name
    :return: file name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='The name of the file to analyze')
    args = parser.parse_args()
    return args.filename


def search(divided: list[str]) -> list[str]:
    """
    Function search for questionnaires of people who lives in Moscow
    :return: all questionnaires which fits in
    """
    found = [i for i in divided if re.search(r'Москва', i)]
    if len(found) == 1:
        raise IndexError("File is empty")
    return found


def out(found: list[str]) -> None:
    """
    Displaying of required questionnaires
    :param found: list of required questionnaires
    :return: nothing
    """
    print("\n")
    for j in found:
        print(j)


def main():
    filename = parsing()
    doc = open_file(filename)
    divided = split(doc)
    found = search(divided)
    out(found)


if __name__ == '__main__':
    main()
