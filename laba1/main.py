import argparse
import codecs
import re


def create_parser():
    """
    User enters the name of the file to be read
    :return: the name of the file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help="Path to file")
    return parser.parse_args().filename


def read_file(filename:str)->list:
    """
    Reads a file, that was given to it
    :param filename: the name of the file will be read
    :return: the file converted to a list
    """
    file = codecs.open(filename, "r", "utf_8_sig")
    text = file.readlines()
    return text


def age(txt: list)->int:
    """
    Сounts the number of people contained in the file that were born in the 21st century
    :param txt: the text in which the calculation will be performed
    :return: an amount of people that was born in 21st century
    """
    count: int = 0
    new_list=[]
    for i in range(len(txt)):
        new_list.append(txt[i])
    for text in new_list:
        match = re.search(r'\b(\d{4})\b', text)
        if match:
            found_year = int(match.group(1))
            if found_year > 1999:
                count += 1
    return count


def main():
    filename=create_parser()
    text = read_file(filename)
    print(age(text))


if __name__ == "__main__":
    main()