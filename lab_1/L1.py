import argparse
import re


def get_path() -> str:
    """
    Parses the file name from the command line arguments.
    :return: the file name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str)
    return parser.parse_args().path


def read_file(path: str) -> str:
    """
    Reads the content of the file
    :param path: file name
    :return: file content
    """
    with open(path, 'r', encoding="UTF-8") as file:
        return file.read()


def find(form: str) -> list:
    """
    Finds all mentions of the word "Мужской"
    :param form: the text to search in
    :return: the list of all matches
    """
    return re.findall("Мужской", form)


def print_number_of_matches(matches: list) -> None:
    """
    Prints the number of matches
    :param matches: the list of all matches
    :return: None
    """
    print(len(matches))


def main():
    try:
        path = get_path()
        form = read_file(path)
        matches = find(form)
        print_number_of_matches(matches)
    except ValueError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
