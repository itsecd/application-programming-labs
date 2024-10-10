import argparse
import re


def name() -> str:
    """
    getting file name from user via terminal
    :return: name of file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type=str)
    args = parser.parse_args()
    return args.name


def read_file(filename: str) -> str:
    """
    extracting info from file
    :param filename: name of file
    :return: data in string form
    """
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            doc = file.read()
            return doc
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        exit(1)


class NoPatternFoundError(Exception):
    """
    Custom exception for when the split pattern is not found
    """
    pass


def split(doc: str) -> list[str]:
    """
    dividing string into substrings, each substring is separate questionnaire
    :param doc: single string containing all questionnaires
    :return: list of questionnaires
    """
    trigger = r'\d+' + r'[)]' + '\n'
    divided = re.split(trigger, doc)
    if len(divided) == 1:
        raise NoPatternFoundError("pattern is not found in the text")
    return divided


def find_number(divided: list[str]) -> list[str]:
    """
    searching all people with this area code
    :param divided: list of questionnaires
    :return: list of required questionnaires
    """
    found = [i for i in divided if re.search(r'\+7 927', i)]
    if len(found) == 1:
        raise NoPatternFoundError("pattern is not found in the text")
    return found


def out(found: list[str]) -> None:
    """
    displaying of required questionnaires
    :param found: list of required questionnaires
    :return: nothing
    """
    print("\n")
    for j in found:
        print(j)


def main() -> None:
    filename = name()
    doc = read_file(filename)
    divided = split(doc)
    found = find_number(divided)
    out(found)


if __name__ == "__main__":
    main()
