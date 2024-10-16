import argparse
import re

def pars()->str:
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='path to file')
    args = parser.parse_args().filename
    return args
def get_text(filename:str)->str:
    with open(filename,"r", encoding = "utf_8") as file:
        text: str = file.read()
        return text
def find(text:str)->list:
    pattern_date = r'\d\d.\d\d\.\d\d\d\d'
    date = re.findall(pattern_date, text)
    return date
def datesearch(date:list)->int:
    counter = 0
    for i in range(len (date)):
        birthday = int(date[i].split('.')[2])
        if birthday > 2000:
            counter+=1
    return counter
def main():
    filename = pars()
    text = get_text(filename)
    date = find(text)
    print(datesearch(date))
if __name__ == "__main__":
    main()