import argparse
import re



def get_filename() -> str:
    """
     Getting the file name from command line arguments using the `argparse` module.

    :return: Name of file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name of file')
    args = parser.parse_args().filename
    return args


def read(filename: str) -> str:
    """
    The function opens and reads the contents of the file whose name is passed as a parameter.

    :param filename:Name of file
    :return:The contents of the file as a string.
    """
    with open(filename,"r",encoding="UTF-8") as file:
        return file.read()

def counting_profiles_of_men(data:str) -> list:
    """
     The function finds all profiles of men,using the "re" module
    :param data:The contents of the file
    :return:A list of found profiles of men.
    """
    mlist=re.findall("Пол:\\s*Мужской",data)
    return mlist

def number_profiles_of_men (m_list:list) -> int:
    """
    The function counts the number  profiles of men
    :param m_list:A list of found profiles of men.
    :return:the number of profiles of men
    """
    return len(m_list)

def main():
    filename = get_filename()
    data=read(filename)
    m_list=counting_profiles_of_men(data)
    res=number_profiles_of_men (m_list)
    print("The quantity of men in the file:",res)

if __name__=="__main__":
    main()
