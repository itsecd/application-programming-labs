import argparse
import re


def get_filename() -> str:
    """
    Reading a file name from the console
    :return: file name
    """
    parser = argparse.ArgumentParser(description="Find all female names that start with the letter 'A'.")
    parser.add_argument('filename', type=str, help="print the file name (with extension)")
    return parser.parse_args().filename

def read_file(filename: str) -> str:
    """
    Reading data from a file.
    :param filename: file name
    :return: string containing data from a file
    """
    try:
        with open(filename, "r", encoding="UTF-8") as data:
            tmp = data.read()
        return tmp
    except:
        raise FileNotFoundError("File not found")



def find_female_names_at_a(data: str) -> set:
    """
    searches female profiles from all profiles and finds names starting with the letter 'A'
    :param data: string containing data from a file
    :return: list of female names starting with the letter 'A'
    """
    pattern_profiles = r"\d[)]\n"
    profiles = re.split(pattern_profiles, data)
    if len(profiles) <= 1:
        raise EOFError("Error in file content")

    names = list()
    pattern_female = r"Женский"
    pattern_name_at_a = r"Имя: А[а-я]+"
    for i in profiles:
        if re.search(pattern_female, i) and re.search(pattern_name_at_a, i):
            names += (re.findall(pattern_name_at_a, i))
    if len(names) == 0:
        raise ValueError("Not found names")
    for j in range(len(names)):
        names[j] = names[j][5:]
    result = set(names)
    return result


def main():
    try:
        filename = get_filename()
        data = read_file(filename)
        result = find_female_names_at_a(data)
        print(result)
    except Exception as exc:
        print("Error:", exc)

if __name__ == '__main__':
    main()