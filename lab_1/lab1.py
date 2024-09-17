import argparse
import re

def get_filename() -> str:
    """
        Получает название файла (из командной строки)
        :return: название файла
        """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    return parser.parse_args().filename

def read_file(filename: str) -> str:
    """
        Считывает анкеты из файла
        :param filename: название файла
        :return: анкеты
        """
    with open(filename, "r", encoding='utf-8') as file:
        return file.read()


def find_date(text: str) -> list:
    """
        Находит удовлетворяющие паттерну даты из анкет
        :param text: анкеты
        :return: список дат
        """
    pattern = r"\b\d{2}\.\d{2}\.\d{4}\b"
    return re.findall(pattern, text)


def find_21stcentury(dates: list)-> int:
    """
        Подсчитывает количество дат, удовлетворяющих условию
        :param dates: список дат
        :return: число нужных дат
        """
    cnt = 0
    for i in dates:
        year = i[6:10]
        if int(year) >= 2000:
            cnt+=1
    return cnt

if __name__ == "__main__":
    filename = get_filename()
    text = read_file(filename)
    dates = find_date(text)
    print(find_21stcentury(dates))