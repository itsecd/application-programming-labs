import re
import argparse
def get_filename() -> str:
    """
    Parses the file name from the command line arguments
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name of your file')
    args = parser.parse_args().filename
    return args

def open_file(filename: str)-> str:
    """
    Reading the contents of a file
    :param filename: The file name
    :return: A string containing data from a file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        return text

def birthday(text: str)->list:
    """
    Searches for the births dates of all people
    :param text:The text that we read from the file
    :return:Array with found dates of birth
    """
    pattern = r'\d{2}.\d{2}.\d{4}'
    bd = re.findall(pattern, text)
    return bd
def bd_21century(bd: list)->int:
    """
    Looking for people born in the 21st century
    :param bd:Array with dates of birth
    :return:The number of people born in 21
    """
    count = 0
    for i in range(len(bd)-1):
        years = int(bd[i].split('.')[2])
        if years>2000:
            count+=1
    return count

def main():
    filename = get_filename()
    txt = open_file(filename)
    age = birthday(txt)
    print(bd_21century(age))


if __name__ == "__main__":
    main()
