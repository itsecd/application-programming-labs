import re
import argparse


def get_file_name() -> str:
    """
        get name of target file from cmd
        :return(str): name of target file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str, help='Input file.txt')
    args = parser.parse_args()
    return args.file_name

def read_file(file_name: str) -> list[str]:
    """
    read a file line by line
    :param file_name: name of target file
    :return: list of all strings in file
    """
    try:
        with open(file_name, mode='r', encoding='UTF-8') as file:
            dates = file.readlines()
        dates = [i for i in dates if i !='\n']
        return dates
    except:
        raise FileNotFoundError("File was not found")

def find_people_with_code(dates: list[str]) -> list[str]:
    """
    searches for profiles of people whose phones have the area code 927
    :param dates: list with all the profiles
    :return: list of found profiles
    """
    found = []
    i = 0
    while i < len(dates):
        pattern = re.search(r'\+7 927', dates[i])
        if pattern is not None:
            found.append(dates[i-4] + dates[i-3] + dates[i-2] + dates[i-1] + dates[i] + dates[i+1])
        i+=1
    if len(found) == 0:
        raise Exception("Not a single string matching the pattern was found.")
    return found


def print_str(dates: list[str]) -> None:
    """
    displays the necessary profiles
    :param dates: list of found profiles
    """
    if not dates:
        raise Exception("Empty array")
    for i in dates:
        print(i)

def main():
    try:
        file_name = get_file_name()
        dates = read_file(file_name)
        find_dates=find_people_with_code(dates)
        print_str(find_dates)
    except Exception as exc:
        print(f"Error: {exc}")

if __name__ == "__main__":
    main()