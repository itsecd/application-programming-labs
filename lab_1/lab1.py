import argparse
import re


def get_filename() -> str:
    """
    Parses the file name from the command line arguments.

    :return: The file name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    return parser.parse_args().filename


def read_file(filename: str) -> str:
    """
    Reads the contents of the file.

    :param filename: The file name
    :return: The file contents
    """
    with open(filename, "r") as file:
        return file.read()


def find_numbers(text: str) -> list:
    """
    Finds the country and operator code for each number.

    :param text: The string to search in
    :return: The list ot country and operator codes
    """
    pattern = r"\+7\s+\d{3}"
    return re.findall(pattern, text)


def find_codes(numbers: list) -> dict:
    """
    Finds the dictionary of encountered operator codes with an
    indication of the number of meetings.

    :param numbers: The list of numbers
    :return: The dictionary of encountered operator codes with an
             indication of the number of meetings
    """
    codes_dict = dict()
    for i in numbers:
        code = i[i.find("+7") + 2:].strip()
        if code in codes_dict.keys():
            codes_dict[code] += 1
        else:
            codes_dict[code] = 1
    return codes_dict


def print_most_common(codes_dict: dict):
    """
    Prints the most common operator code.

    :param codes_dict: The dictionary of operator codes with an
                       indication of the number of meetings
    """
    print("The most common operator code is",
          max(codes_dict, key=codes_dict.get))


if __name__ == "__main__":
    filename = get_filename()
    text = read_file(filename)
    numbers = find_numbers(text)
    codes = find_codes(numbers)
    print_most_common(codes)
