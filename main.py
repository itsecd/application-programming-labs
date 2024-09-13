import codecs
import argparse


def CreateParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help="Path to file")
    return parser.parse_args().filename

def ReadFile(filename:str)->list:
    """
    Reads a file, that was given to it

    :param filename: the name of the file will be read

    :return: the file converted to a list
    """
    file = codecs.open(filename, "r", "utf_8_sig")
    text = file.readlines()
    return text

def Age(txt: list)->int:
    """
    Сounts the number of people contained in the file that were born in the 21st century

    :param txt: the text in which the calculation will be performed

    :return: an amount of people that was born in 21st century
    """
    count: int = 0
    new_list=[]
    for i in range(4,len(txt),8):
        new_list.append(txt[i])
    for text in new_list:
        if int(text[-5:-1])>1999:
            count+=1
    return count


def main():
    filename=CreateParser()
    text = ReadFile(filename)
    print(Age(text))

if __name__ == "__main__":
    main()

