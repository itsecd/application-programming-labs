import argparse
import datetime
import re
import os


def parsing() -> str:
   """
      Parse command line arguments and returns the file name
      :return: file name
   """
   parser = argparse.ArgumentParser()
   parser.add_argument('file', type=str, help='The name of the file to analyze')
   args = parser.parse_args()
   return args.file


def open_file(namefile: str) -> str :
    """
       Reading the contents of a file
       :param namefile: The file name
       :return: A string containing data from a file
       """
    with open(namefile, 'r', encoding='utf=8') as file:
       text = file.read()
       return text


def separation_text(text: str) -> list[str]:
   """
          Searches for parser values in the text
          :param text: A line with the words
          :return: A row with birth dates
          """
   pattern = r'\d{2}.\d{2}.\d{4}'
   people = re.findall(pattern, text)
   return people


def counting_birth(separation: str) -> list[str]:

   current_date = datetime.datetime.now()
   b = 0
   for birthday in separation:
    dt_now = datetime.datetime.now()
    b=0
    for birthday in separation:
       birth_day=datetime.datetime.strptime(birthday,'%d.%m.%Y')
       age = (current_date - birth_day).days / 365
       if 30 <= age <= 40:
          b+=1
    return b


def main():
   filename = parsing()
   text =  open_file( filename)
   separation = separation_text(text)
   result = counting_birth(separation)
   print('Количество людей возрастом от 30 до 40 лет:', result)

if __name__ == "__main__":
   main()






