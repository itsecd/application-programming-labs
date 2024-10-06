# import re
# import argparse
# print("hello world")
#
# # Первый вариант работы с файлом
# file = open("file_name.txt", "r")
# a = file.readline()
# b = file.read()
# c = file.readlines()
# file. close()
#
# #Второй вариант работы с файлом (автоматом закрывает поток)
# with open("file_name.txt") as file:
#     text = file.readlines()
#
#
# parser = argparse.ArgumentParser()
# parser.add_argument('name', type=str, help='your name')
# parser.add_argument("-s", "--surname", type=str, help="your surname")
# args = parser.parse_args()
# print(f"Hello, {args.name}")
#
# if args.surname is not None:
#     print(f"Hello, {args.name} {args.surname}")
# else:
#     print(f"Hello, {args.name}")
#
# # Шаблоны, соответствующие одному символу
# # . - Один любой символ, кроме новой строки \n.
# # \d - Любая цифра
# # \s - Любой пробельный символ (пробел, табуляция, конец строки и т.п.)
# # \w - Любая буква (то, что может быть частью слова), а также цифры и _
# # [..] - Один из символов в скобках, а также любой символ из диапазона a-b
# # [^..] - Любой символ, кроме перечисленных
# #--------------------------------------------------------------------
# # Квантификаторы (указание количества повторений)
# # {n} - Ровно n повторений
# # {m,n} - От m до n повторений включительно
# # {m,} - Не менее m повторений
# # {,n} - Не более n повторений
# # ? - Ноль или одно вхождение, синоним {0,1}
# # * - Ноль или более, синоним {0,}
# # + - Одно или более, синоним {1,}
#
#
#
# text1 = "Список чисел: 123, 456, 789 и 123"  # строка поиска
# pattern = r'\d+'  # шаблон
# numbers = re.findall(pattern, text1)
# print(numbers)
#
# text2 = "один, два, три; четыре. пять! шесть"  # строка поиска
#
# # Разделяем строку по разделителям: точка с запятой, запятая, точка, восклицательный знак, пробельный символ
# parts = re.split(r'[;,.!\s]+', text2)
# print(parts)

# Функции библиотеки re
# Библиотека re в Python предоставляет функции для работы с регулярными выражениями.
# re.search(pattern, string) - Найти в строке string первую строчку, подходящую под шаблон pattern;
# re.fullmatch(pattern, string) - Проверить, подходит ли строка string под шаблон pattern;
# re.split(pattern, string, maxsplit=0) - Аналог str.split(), только разделение происходит по подстрокам, подходящим под шаблон pattern;
# re.findall(pattern, string) - Найти в строке string все непересекающиеся шаблоны pattern;
# re.finditer(pattern, string) - Итератор по всем непересекающимся шаблонам pattern в строке string (выдаются match-объекты);
# re.sub(pattern, repl, string, count=0) - Заменить в строке string все непересекающиеся шаблоны pattern на repl;

# r'' - буквальное интерпретирование строки

import re
import argparse
def parsing():
    parser = argparse.ArgumentParser(description='Парсинг txt-файла.')
    parser.add_argument('filename', type=str, help='Имя txt-файла для обработки')
    args = parser.parse_args()
    name = args.filename
    return name

def read(name:str) -> str:
    with open(name, 'r', encoding='utf-8') as file:
        filename = file.read()
        return filename


def count_names(data:str):
    pattern = r'Имя:\s*([^\n]+)'
    names = re.findall(pattern, data)
    return names


def task_var7(names:str) -> str:
    name_counts = {}
    for i in names:
        if i in name_counts:
            name_counts[i] += 1
        else:
            name_counts[i] = 1

    if (len(name_counts) != 0):
        max_name = max(name_counts, key=name_counts.get)
        count = name_counts[max_name]
        string = "Имя, которое встречается чаще всего:" + str(max_name) + ": " + str(count) + " раз(а)"
    else:
        string = "Имена не найдены"

    return string


def main():
    file = parsing()
    try:
        text = read(file)
        #print(text)
        print(count_names(text))
        print(f"Длина массива всех имен: {len(count_names(text))}")
        # Выполнение задания варианта
        result = task_var7(count_names(text))
        print(result)

    except FileNotFoundError:
        print(f"Файл '{file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()












