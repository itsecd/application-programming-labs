import argparse

def value_input() -> argparse.Namespace:
    """
    Функция, позволяющая осуществить ввод ключевого слова, пути к директории, кол-ва изображений, пути к файлу для аннотации
    :return: аргументы
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('keyw', type=str, help='Ключевое слово для поиска фотографий')
    parser.add_argument('-d','--dir_name', type=str, help='Путь к директории')
    parser.add_argument('-v','--value', type=int, help='Количество изображений для скачивания')
    parser.add_argument('-f', '--annotation_file', type=str, help='Путь к файлу для аннотации')
    arg = parser.parse_args()
    return arg