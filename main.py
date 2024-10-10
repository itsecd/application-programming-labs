import argparse
import re
def main() -> None:
    '''
    Command line options are created here
     -f File Name
     -g gender is Female/Male
     -l is the letter or combination with which the Name begins

    There is also a call to the find() function
    :return: None:
    '''
    p_cmd = argparse.ArgumentParser()
    p_cmd.add_argument("-f", "--file", type=str, help="file name")
    p_cmd.add_argument("-g", "--gender", type=str, help="Male/Female")
    p_cmd.add_argument("-l", "--letter", type=str, help="One Letter")
    args = p_cmd.parse_args()
    find(split(file_reader(args.file)), args.gender, args.letter)
def file_reader(file_name: str) -> str:
    '''
    This function opens a file by its path
    or name(file_name)
    and enters the contents into a string(result_string).
    If it is impossible to find the file, it displays an error
    :param file_name:
    :return: result_string:
    '''
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            result_string = file.read()
        return result_string
    except FileExistsError as exc:
        print(f"Звуки сирены: {exc}")
def split(string: str) -> list:
    '''
    This function divides the string
    into separate questionnaire lines and enters them
    into an array (list), assigning the corresponding number
    :param string:
    :return: list:
    '''
    list = re.split(r"\d+\)\n", string)
    del list[0]
    for i in range(len(list)):
        list[i] = str(i+1)+")"+list[i]
    return list

def find(profiles: list, gender:str, letter: str) -> None:
    '''
    The search function by parameters. Finds
    suitable questionnaires from the profiles list by the corresponding gender
    and letter/combination at the beginning of the name(letter)
    and outputs an array with the names found in these questionnaires (name_list)
    :param profiles:
    :param gender:
    :param letter:
    :return: None:
    '''
    name_list = []
    for profile in profiles:
        if (re.search(r"Пол:\s+"+gender, profile) is not None and re.search(r"Имя:\s+"+letter, profile) is not None):
            tmp_1 = re.findall(r"Имя:\s+\w+\n", profile)
            tmp_2 = re.split(r":\s+", tmp_1[0])
            if(tmp_2[1][:-1] not in name_list):
                name_list.append(tmp_2[1][:-1])
    if (len(name_list) != 0):
        print(name_list)

if __name__ == '__main__':
    main()
