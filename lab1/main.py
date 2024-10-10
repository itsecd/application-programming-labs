import argparse
import re


def parcing()->argparse.Namespace:
    '''
    Данная функция запрашивает у пользователя название файла
    и параметр, по которому выбираются анкеты
    '''
    parser = argparse.ArgumentParser()  # создание экземпляра парсера
    parser.add_argument('file_name', type=str, help='Введите название файла (с расширением)')
    parser.add_argument('name', type=str,help='название города в именительном падеже')
    args = parser.parse_args()
    # парсинг аргументов
    return args


def list_searcher(list1:list, args:argparse.Namespace)->list:
    '''
    Данная функция выбирает нужные анкеты
    '''
    flag = True
    result_list=[]
    for i in range(len(list1)):
        if (re.search(f"{args.name}", list1[i]) != None):
            result_list.append(str(i) + ')'+'\n'+list1[i])
            flag = False
    if flag:
        print("Таких людей в списке нет")
    return result_list


def text_splitter(text:str)->list:
    '''
    Данная функция делит текст на список анкет
    '''
    pattern=r'\d+'+r'[)]+'+'\n'
    list1=re.split(pattern,text,maxsplit=0)
    return list1



def read_file(args:argparse.Namespace)->str:
    '''
    Данная функция читает данные из файла
    '''
    with open(f"{args.file_name}", "r",encoding="utf_8") as file:
        text = file.read()
    return text


def list_print(list1:list)->None:
    '''
    Данная функция распечатывает список
    '''
    for i in range(len(list1)):
        print(list1[i])


def main():
    args = parcing()
    try:
        # ВЫЗВАЛИ ИСКЛ НА ОТСУТСВИЕ ФАЙЛА
        args = parcing()
        file = read_file(args)
        if len(file) == 0:
            raise Exception("файл пуст")
        blanks = text_splitter(file)
        result_list = list_searcher(blanks, args)
        list_print(result_list)

    except FileNotFoundError:
        print("Ошибка: файл не найден")
    except Exception as exc:
        print("Ошибка:", exc)


if __name__== '__main__':
    main()
