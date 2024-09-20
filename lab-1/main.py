import argparse
import re


def get_filename() -> str:
    """
     Parses the file name from the terminal arguments
    using the 'argparse' module.

    :return:The file name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name of file')
    args = parser.parse_args()
    return args


def read(filename: str) -> str:
    """
    Reads the contents of the file.

    :param filename:The file name
    :return:The file contents
    """
    with open("data.txt","r",encoding="UTF-8") as file:
        return file.read()

def count_of_men(data:str) -> int:
    """
     Using the 're' module, it finds all the men in the list
    and returns their number.
    :param data:The file contents
    :return:The number of male profiles
    """
    m_list=re.findall("Пол:\\s*Мужской",data)
    return len(m_list)

def main():
    filename = get_filename()
    data=read(filename)
    print("The quantity of men in the file:",count_of_men(data))

if __name__=="__main__":
    main()