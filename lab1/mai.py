import argparse
import re


def parsing():
    """
    Парсинг аргументов командной строки
    """
    parser = argparse.ArgumentParser(description='Парсинг txt-файла.')
    parser.add_argument('filename', type=str, help='Имя txt-файла для обработки')
    args = parser.parse_args()
    name = args.filename
    return name

def read(name: str) -> str:
    """
    Создание потока
    """
    with open(name, 'r', encoding='utf-8') as file:
        filename = file.read()
        return filename

def count_names(data: str):
    """
    Подсчет всех имен в файле
    """
    pattern = r'Имя:\s*([^\n]+)'
    names = re.findall(pattern, data)
    return names

def create_tuple(names: list) -> dict:
    """
    Составление словаря имен с их количеством
    """
    name_tuple = {}
    for i in names:
        if i in name_tuple:
            name_tuple[i] += 1
        else:
            name_tuple[i] = 1
    return name_tuple


def popular_name(name_tuple: dict) -> str:
    """"
    Нахождение самого встречаемого имени (Задание варианта)
    """
    if len(name_tuple) != 0:
        max_name = max(name_tuple, key=name_tuple.get)
        #count = name_tuple[max_name]
        #result = f"Имя, которое встречается чаще всего: {max_name}: {count} раз(а)"
        result = str(max_name)
    else:
        result = "0"

    return result

def main():
    file = parsing()
    try:
        text = read(file)
        names_list = count_names(text)
        print(f"Список найденных имен: \n{names_list}")
        print(f"Длина массива всех имен: {len(names_list)}\n")
        name_dict = create_tuple(names_list)
        print(f"Созданный словарь: \n{name_dict}")

        # Выполнение задания варианта - передаем созданный словарь в popular_name
        result = popular_name(name_dict)

        if result != "0":
            print(f"Имя, которое встречается чаще всего: {result}")
        else:
            print("Имена не найдены")

    except FileNotFoundError:
        print(f"Файл '{file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()