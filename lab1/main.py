import argparse
import re


def get_filename() -> str:
    """
    Parses the file name from the command line arguments.
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('name_file', type=str, help='name file')
    args = parser.parse_args()
    filename = args.name_file + ".txt"
    return filename


def read_file(filename: str) -> str:
    """
    Reading the contents of a file
    :param filename: The file name
    :return: A string containing data from a file
    """
    with open(filename, "r", encoding='utf-8') as file:
        text = file.read()
    return text


def find_women(text: str) -> list:
    """
    Search for profiles of women among all profiles
    :param text: Data from the file
    :return: List of profiles of women
    """
    people = re.split(r"\d[)]", text)[1:]
    women = list()
    for i in people:
        if re.search("Пол: Женский", i) and re.search("Имя: А", i):
            women.append(i)
    return women


def find_name_at_a(women: list) -> set:
    """
    Search for names starting with the letter a
    :param women: The list of women among whom the search is performed
    :return: Set of names starting with the letter a
    """
    names = list()
    for i in women:
        names += (re.findall(r"Имя: А[а-я]+", i))
    for i in range(len(names)):
        names[i] = names[i][4:]
    res = set(names)
    return res


def main():
    filename = get_filename()
    text = read_file(filename)
    women = find_women(text)
    ans = find_name_at_a(women)
    print(ans)


if __name__ == "__main__":
    main()
