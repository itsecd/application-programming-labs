import re
import argparse

def create_parce() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='filename', default='data.txt')
    path = parser.parse_args()
    return path

def open_file(path) -> str:
    try:
        with open(path.file, "r", encoding="utf-8") as file:
            data = file.read()
        return data
    except:
        raise FileExistsError ("Некорректный файл")

def find_pattern(data) -> list:
    pattern = (r'Фамилия:\s*(.+?)\s*'
           r'Имя:\s*(.+?)\s*'
           r'Пол:\s*(.+?)\s*'
           r'Дата\s*рождения:\s*(.+?)\s*'
           r'Номер\s*телефона:\s*(.+?)\s*'
           r'Город:\s*(\w[^1-9,\n]+)')
    info = re.findall(pattern, data)
    return info

def check_city(info, i) -> bool:
    return info[i][5] == "Москва"

def print_info(info, i) -> None:
    print("Фамилия: ", info[i][0])
    print("Имя: ", info[i][1])
    print("Пол: ", info[i][2])
    print("Дата рождения: ", info[i][3])
    print("Номер: ", info[i][4])
    print("Город: ", info[i][5], "\n")

def main() -> None:
    info = find_pattern(open_file(create_parce()))
    count = 0
    for index in range(len(info)):
        if check_city(info, index) == 1:
            print_info(info, index)
            count+=1
    print(count)

if __name__ == "__main__":
    try:
        main()
    except FileExistsError as exc:
        print(exc)
