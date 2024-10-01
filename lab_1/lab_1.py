import re
import argparse

def get_file_name() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name_of_file')
    args = parser.parse_args().filename
    return args


def open_file(namefile:str) -> str:
    with open(namefile, 'r', encoding='utf_8') as file:
        text: str = file.read()
        return text


def birthday(text:str) -> list:
     pattern = r'\d{2}.\d{2}.\d{4}'
     date = re.findall(pattern, text)
     return date


def date_sort(date:list) -> str:
    count = 0
    for i in range(len(date)-1):
        year = int(date[i].split('.')[2])
        if year > 2000:
            count +=1
    return count


def main():
    filename=get_file_name()
    text=open_file(filename)
    birth = birthday(text)
    quantities = date_sort(birth)
    print(quantities)
if __name__ == "__main__":
    main()
