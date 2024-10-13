import argparse

import filter_data


def read_file(filename:str) -> list:
    """" Open the file and read data by lines"""
    with open(filename, "r") as file:
        text = file.readlines()
    return text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)
    args = parser.parse_args()
    try:
        content = read_file(args.filename)
        print(f"\nКол-во человек, которые родились в 21 веке: {filter_data.count_data(content, 2001)}")
    except FileNotFoundError:
        print("Файл с таким именем не найден!")


if __name__ == "__main__":
    main()
