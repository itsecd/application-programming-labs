import re
import argparse


def open_file(filename: str):
    """
    This function opens and reads the file in one line

    :return: reworked text in one line
    """
    with open(filename, "r", encoding="utf-8") as file:
     text = file.read()
    return text


def parsing() -> str:
    """
    Parse command line arguments and returns the file name

    :return: file name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='The name of the file to analyze')
    args = parser.parse_args()
    return args.file


def find_man(text: str) -> int:
    """
    Finds the number of occurrences of the word "Мужской"

    :return: number of men
    """
    pattern = r"Мужской"
    man = re.findall(pattern, text)
    return (len(man))


def main():
    filename = parsing()
    open_text = open_file(filename)
    print("The number of profiles of men:", find_man(open_text))


if __name__ == '__main__':
  main()