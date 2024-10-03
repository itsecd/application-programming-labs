import argparse


def parser_()-> str:
    """Create parser and return filename"""
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='Path to file')
    return parser.parse_args().filename


def read_file(filename: str)-> list:
    """Read file and getting data from file
       param:filename
       return: list
     """

    with open(filename, "r", encoding='utf-8') as file:
        return file.readlines()


def count_age(text: list)-> int:
    """
    Counting dates
    param: list
    return: number(int)
    """

    counter = 0
    new_list=[]
    for i in range(4,len(text),8):
        new_list.append(text[i])
    for text in new_list:
        if int(text[-5:-1])>1999:
            counter+=1
    return counter


def main():
    filename=parser_()
    text = read_file(filename)
    print(count_age(text))




if __name__ == "__main__":
        main()
