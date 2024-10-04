import argparse
import re
from collections import Counter
import os


def get()-> str:
    """
    пользователь вводит название файла
    :return:название файла
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='your name file')
    args = parser.parse_args()
    return args.filename


def openfile(file_name:str) -> str:
    """
    берёт данные из файла
    :param file_name:название файла
    :return:данные из файла
    """
    try:
        with open(file_name,"r", encoding="utf-8") as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("Файл не найден.")

def razdel(text:str)->list[str]:
    """
    разделяет данные из файла и записывает имена
    в names
    :param text:данные в виде строки
    :return:имена из анкет
    """
    pattern = r'Имя:\s*([а-яА-ЯёЁ]+)'
    names=re.findall(pattern,text)
    return names


def popular(name:list):
    """
    находит самое частоповторяемое имя
    :param name:список имён
    :return:самое частое имя
    """
    counter=Counter(name)
    return counter


def vyv(counter)-> None:
    """
    выводит самое частое имя
    :param counter: самое частое имя
    :return: none
    """
    print(counter.most_common(1))


def main():
    """
    вызываем функции поочерёдно
    :return: none
    """
    try:
        file_name=get()
        text= openfile(file_name)
        name=razdel(text)
        counter1=popular(name)
        vyv(counter1)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
