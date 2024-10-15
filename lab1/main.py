import argparse
import datetime
import re


def parsing() -> str:
   """
      Parse command line arguments and returns the file name
      :return: file name
   """
   parser = argparse.ArgumentParser()
   parser.add_argument('file', type=str, help='The name of the file to analyze')
   args = parser.parse_args()
   return args.file


def open_file(filename) -> str :
    """
       Reading the contents of a file
       :param namefile: The file name
       :return: A string containing data from a file
       """
    with open(filename, 'r', encoding='utf=8') as file:
       text = file.read()
       return text


def separation_text(text: str) -> list[str]:
   """
          Searches for parser values in the text
          :param text: A line with the words
          :return: A row with birth dates
          """
   pattern = r'\d{2}.\d{2}.\d{4}'
   date = re.findall(pattern, text)
   return date


def counting_birth(separation: str) -> list[str]:
   b = 0
   for birthday in separation:
    date_d = datetime.datetime.strptime(birthday, '%d.%m.%Y').date()
    year = date_d.year
    day =date_d.day
    mo = date_d.month
    if counting_years(day,mo,year)==1:
        b+=1
   return b


def counting_years(da: int,mo:int,yea:int)->int:
    current_day = datetime.datetime.now().date()
    day = current_day.day
    month = current_day.month
    c=0
    """
    Все работает но через капец какие костыли
    """
    if (1985>yea or 1995<yea):
        c+=0
    elif (1984<yea and 1994>yea):
        c+=1
    elif (1984==yea or 1994==yea) and (month>=mo):
        c+=1
    elif (1983==yea) and (month<=mo):
      c+=1
    elif (1993==yea) and (month<=mo):
      c+=1

    return c

def main():
   filename = parsing()
   text =  open_file(filename)
   separation = separation_text(text)
   result = counting_birth(separation)
   print('Количество людей возрастом от 30 до 40 лет:', result)

if __name__ == "__main__":
   main()






