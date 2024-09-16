import argparse
import re


def get_filename() -> str:
    """
    Получает название файла из арнументов командной строки

    :return: название файла
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='name of the data file') 
    return parser.parse_args().filename


def read_file(filename: str) -> list:
    """
    Считывает строки из переданного имени файла и переводит полученную информацию в вид списка словарей,
    содержащих информацию о отдельной анкете

    :param filename: имя файла
    :return: список анкет
    """
    with open(filename, "r", encoding = "UTF-8") as file:
        forms = []
        data = [form.replace("\n", "").split(":")[1][1:] for form in file.readlines() \
                 if form != "\n" and ")" not in form]
        for i in range(0, len(data), 6):
            form = {
                "id" : (i//6)+1,
                "surname" : data[i],
                "name" : data[i+1],
                "sex" : data[i+2],
                "birth_date" : data[i+3],
                "phone_number" : data[i+4],
                "city" : data[i+5],
            }
            forms.append(form)
    
    return forms


def main(forms: list) -> list:
    """
    Формирует новый список на основании данного, фильтруя анкеты на основании
    номера телефона

    :param forms: список анкет
    :return: отфильтрованный список анкет
    """
    filtered_forms = []
    for form in forms:
        if re.fullmatch(re.compile(r"\+7\s+927[0-9- ]*"), form["phone_number"]):
            filtered_forms.append(form)
        
    return filtered_forms

def print_form(form: dict) -> None:
    """
    Функция для вывода информации о отдельной анкете на экран
    
    :param form: форма для вывода на экран
    """
    print(f'{form["id"]})\n' \
        + f'Фамилия: {form["surname"]}\n' \
        + f'Имя: {form["name"]}\n' \
        + f'Пол: {form["sex"]}\n' \
        + f'Дата рождения: {form["birth_date"]}\n' \
        + f'Номер телефона: {form["phone_number"]}\n' \
        + f'Город: {form["city"]}\n')


if __name__ == '__main__':
    filename = get_filename()
    forms = read_file(filename)
    filtered_forms = main(forms)
    [print_form(form) for form in filtered_forms]
        