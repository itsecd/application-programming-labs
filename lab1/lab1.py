import re
import argparse
def get_filename() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name of your file')
    args = parser.parse_args().filename
    return args

def open_file(filename: str)-> str:
    with open('filename', 'r', encoding='utf-8') as file:
        text = file.read()
        return text

def birthday(text: str)->list:
    pattern = r'\d{2}.\d{2}.\d{4}'
    bd = re.findall(pattern, text)
    return bd
def bd_21century(bd: list)->int:
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