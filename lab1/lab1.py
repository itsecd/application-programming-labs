import argparse
import re

def get_name_of_file() -> str:
    """
    Getting filename
    :return: name of file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='input name of your file')
    args = parser.parse_args()
    return args.filename

def read_file(filename: str) -> str:
    """
    Getting data from file
    :param filename: filename
    :return: file data
    """
    try:
        with open(filename, "r", encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{filename}' is not found.")
        exit(1)

def get_codes(data: list[str]) -> list[str]:
    """
    Compilating list of codes
    :param data: original data
    :return: list of codes
    """
    pattern_for_split = r'\d+\)\n'
    split_data = re.split(pattern_for_split, data, maxsplit=0)
    pattern = r'\+7 927\d{7}'
    found_data = list()
    for codes in split_data:
        if re.search(pattern, codes):
            found_data.append(codes)
    return found_data

def print_codes(found_data: list[str]) -> None:
    """
    Printing list
    :param found_data: final list of codes
    :return: None
    """
    for codes in found_data:
        print(codes)
    print()

def main():
    filename = get_name_of_file()
    data: str = read_file(filename)
    found_data = get_codes(data)
    print_codes(found_data)

if __name__ == "__main__":
    main()
