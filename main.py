import argparse
import datetime
import re



def get_file_name() -> str:
    """
    Считывает название файла с БД из командной строки
    :return: Имя файла с БД
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='input file name')
    args = parser.parse_args().filename
    return args


def read_file(file_name: str) -> str:
    """
    Считывает данные из файла

    :param file_name: Имя файла
    :return: Содержание файла
    """
    with open(file_name, "r") as file:
        return file.read()


def get_birthdays(data: str) -> list:
    """
    Составляет список дней рождения
    :param data: Исходные данные о людях(бд)
    :return: Список дней рождения, где каждый элемент имеет вид "DD.MM.YYYY"
    """
    bd_list = re.findall("\d\d.\d\d.\d\d\d\d", data)
    return bd_list


def count_people(bd_list: list) -> int:
    """
    Считает количество людей возрастом от 30 до 40 лет включительно
    :param bd_list: Список дней рождения
    :return: Число подходящих под заданные требования людей
    """
    count = 0
    for birthday in bd_list:
        cur_bd = datetime.datetime.strptime(birthday, '%d.%m.%Y')
        difference = datetime.datetime.now() - cur_bd
        if 30 <= (difference.days / 365) <= 40:
            count += 1
    return count


def main() -> None:
    filename = get_file_name()
    data = read_file(filename)
    birthdays_list = get_birthdays(data)
    num_of_needed_people = count_people(birthdays_list)
    print(num_of_needed_people)


if __name__ == "__main__":
    main()
