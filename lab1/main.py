import re
import argparse


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


def separation_birth(year: int,month: int,day: int) -> int:
   """
             Check the condition of occurrence of birthdays
             :param text: Year,month,day
             :return:  1 if it fits
             """
   count=0
   if ((1983 == year) and (month >= 9) and (day > 25)):
      count += 1
   if (1984 <= year and 1993 >= year):
      count += 1
   if ((1994 == year) and (month <= 9) and (day <= 25)):
      count += 1
   return count


def counting_birth(people: str) -> list[str]:
   """
              Divides the date of the birthday into components and goes through all
               :param text: A line with the words
               :return: the number of suitable dates
               """
   count=0
   for i in range(len(people) - 1):
      year = int(people[i].split('.')[2])
      month = int(people[i].split('.')[1])
      day = int(people[i].split('.')[0])
      count+=separation_birth(year,month,day)
   return count


def main():
   filename = parsing()
   text =  open_file( filename)
   separation = separation_text(text)
   Quantity = counting_birth(separation)
   print('Количество людей возрастом от 30 до 40 лет:', Quantity)

if __name__ == "__main__":
   main()






