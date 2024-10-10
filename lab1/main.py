import argparse
import re


def get_filename() -> str:

    '''
    get name of target file from cmd
    :return(str): name of target file
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='Input file')
    args = parser.parse_args()

    return args.filename


def read_file(filename: str) -> list[str]:

    '''
    read all strings from the file to list
    :param filename(str): name of target file
    :return(list[str]): list of all strings in file
    '''

    file = open(filename, "r", encoding='utf-8')
    list_of_strings = file.readlines()
    file.close()

    return list_of_strings


def find_most_often_name(list_of_strings: list[str]) -> tuple[str, int]:

    '''
    find most count name
    :param list_of_strings(list[str]): list of all strinds in file
    :return(tuple[str, int]): most count name and count
    '''

    names_list = []
    dif_names_list = []
    pattern = r"^Имя: (.+)\n$"
    for string in list_of_strings:
        if re.fullmatch(pattern, string):
            names_list.append(string[5:-1])
            if string[5:-1] not in dif_names_list:
                dif_names_list.append(string[5:-1])

    names_dict = {name:0 for name in dif_names_list}
    for name in names_list:
        names_dict[name] += 1

    max_cnt = 0
    find_name = ""
    for name in names_dict:
        if names_dict[name] > max_cnt:
            max_cnt = names_dict[name]
            find_name = name

    return find_name, max_cnt


def main() -> None:
    try:
        filename = get_filename()
        list_of_questionnaires = read_file(filename)
        find_name, cnt = find_most_often_name(list_of_questionnaires)
        print(f'Самое частое имя: {find_name}, встречается {cnt} раз')
    except ValueError as exc:
        print(f"Error: {exc}")

if __name__ == "__main__":
    main()

#path to project (for me)
#cd C:\Users\user\PycharmProjects\lab1

#cmd comand to start
#main.py C:\Users\user\Desktop\data.txt

