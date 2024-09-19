import argparse
import re


def parser_create():
    """
    Parses the file name from the terminal arguments
    using the 'argparse' module.

    :return: The file name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help="Path to file")
    return parser.parse_args().filename


def read_file(filename: str) -> str:
    """
    Reads the contents of the file.

    :param filename: The file name
    :return: The file contents
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def count_of_men(data: str) -> int:
    """
    Using the 're' module, it finds all the men in the list
    and returns their number.

    :param data: The file contents
    :return: The number of male profiles
    """
    pattern = re.compile(r"Пол:\s*Мужской")
    find_male = pattern.findall(data)
    return len(find_male)


def main():
    filename = parser_create()
    data = read_file(filename)
    print("The number of profiles of men in the list:", count_of_men(data))


if __name__ == "__main__":
    main()



