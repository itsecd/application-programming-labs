import argparse
import re


def pars_file_name()->str:
    """

    Считываем путь к файлу
    из командной строки
    return: путь как строку
    """
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('file_name', type=str)
        args = parser.parse_args()
        return args.file_name
    except:
        raise SyntaxError("path to file can not be blank")


def open_file(str)->str:
    """

    str: на вход путь к файлу
    открываем файл и считываем в строку
    return: полученную строку

    """
    try:
        with open(str, "r",encoding="UTF-8") as file:
            return file.read()
    except:
        raise FileNotFoundError("Wrong path input")


def look_for_women_names(text)->list:
    """

    text: строка в которой ищем женские
    имена начинающиеся на А
    после выбираем только имена
    return: список имён

    """
    pattern = r'Имя: А\w+\nПол: Ж'
    names = re.findall(pattern, text)
    names="".join(set(names))
    pattern=r'А\w+'
    names = re.findall(pattern,names)
    return names


if __name__ == '__main__':
    try:
        file_name = pars_file_name()
        text = open_file(file_name)
        print(' '.join(look_for_women_names(text)))
    except Exception as exc:
        print(exc)
