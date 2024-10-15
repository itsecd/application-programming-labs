import argparse
import re

def file_read(file_name: str) -> str:
    """
    Прочесть файл и вернуть его в виде строки
    """
    try:
        with open(file_name, 'r', encoding = 'utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise ValueError("Файл не найден: проверьте имя файла!")
    except IOError:
        raise ValueError("Ошибка при чтении файла: проверьте доступность файла!")
def split(string: str) -> list:
    """
    Разделить строку string, записанную в формате "1)1текст2)2текст3)текст..." на список из элементов
    ['1текст', '2текст', '3текст']
    """
    pattern = r'\d+\)'
    listed = re.split(pattern, string)
    return listed[1::]
def find(text: str, gender: str, letter: str) -> list:
    """
    Найти в тексте имена, удовлетворяющие условию
    :param text: неразделенный текст, содержащий всё
    :param gender: искомый пол (М/Ж)
    :param letter: искомая первая буква имени
    :return: список, состоящий из всех найденных имен, удовлетворяющих условию
    """
    profiles = split(text)
    suitableness = set()
    for profile in profiles:
        gender_match = re.search(r'Пол:\s*\w', profile)
        if gender_match is not None and gender_match.group()[-1] == gender:
            letter_match = re.search(r'Имя:\s\w', profile)
            if letter_match is not None and letter_match.group()[-1] == letter:
                suitableness.add(re.search(r'Имя:\s\w*', profile).group()[5::])
    return list(suitableness)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('FileName', type=str, help='name of file')
    parser.add_argument('gender', type=str, help='the desired gender')
    parser.add_argument('letter', type=str, help='the desired letter')
    args = parser.parse_args()
    data = file_read(args.FileName)
    answer = find(data, args.gender, args.letter)
    print(answer)
if __name__ == '__main__':
    main()