import argparse
import re

def get_file_name() -> str:
    """
    Parses the file name from the command line arguments
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name_of_file')
    args = parser.parse_args().filename
    return args


def open_file(namefile:str) -> str:
    """
    Reading the contents of a file
    :param namefile: The file name
    :return: A string containing data from a file
    """
    with open(namefile, 'r', encoding='utf_8') as file:
        text: str = file.read()
        return text


def find_birthday(text:str) -> list:
     """
     Searches for the births dates of all people
     :param text:The text that we read from the file
     :return:Array with found dates of birth
     """
     pattern = r'\d{2}.\d{2}.\d{4}'
     date = re.findall(pattern, text)
     return date


def birthday_sort_XXI(date:list) -> int:
    """
    Looking for people born in the 21st century
    :param date:Array with dates of birth
    :return:The number of people born in 21
    """
    count = 0
    for i in range(len(date)):
        year = int(date[i].split('.')[2])
        if year > 2001:
            count +=1
    return count


def main():
    filename=get_file_name()
    text=open_file(filename)
    birth = find_birthday(text)
    quantities = birthday_sort_XXI(birth)
    print(quantities)
if __name__ == "__main__":
    main()
