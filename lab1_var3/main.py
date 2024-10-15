import argparse
import datetime as dt
import re


def parsing() -> str:
    """
      Parse command line arguments and returns the file name      :return: file name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='The name of the file to analyze')
    args = parser.parse_args()
    return args.file


def open_file(namefile: str) -> str:
    """
    Reading the contents of a file
    :param namefile: The file name       :return: A string containing data from a file
    """
    with open(namefile, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def separation_text(text: str) -> list[str]:
    """
    Searches for parser values in the text
    :param text: A line with the words
    :return: A row with birthdates
    """
    pattern = r'\d{2}.\d{2}.\d{4}'
    people = re.findall(pattern, text)
    return people


def convert_stodt(birthday_strings: list[str]) -> list[dt.date]:
    """
    Check the condition of occurrence of birthdays
    :param birthday_strings: a list of formatted strings
    :return: list of dates converted from strings
    """
    formatting = "%d.%m.%Y"
    birth_dates = [dt.datetime.strptime(bd, formatting).date() for bd in birthday_strings]
    return birth_dates


def age_calculating(birthday: dt.date) -> int:
    today = dt.date.today()
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))


def is_suitable_age(age: int) -> bool:
    return 30 <= age <= 40


def counting_birth(people: list[str]) -> int:
    """
    Divides the date of the birthday into components and goes through all
    :return: the number of suitable dates
    """
    count = 0
    converted_birthdays = convert_stodt(people)
    for i in converted_birthdays:
        if is_suitable_age(age_calculating(i)):
            count += 1
    return count


def main():
    filename = parsing()
    text = open_file(filename)
    separated_text = separation_text(text)
    quantity_of_suit_bdays = counting_birth(separated_text)
    print('Количество людей возрастом от 30 до 40 лет:', quantity_of_suit_bdays)


if __name__ == "__main__":
    main()
