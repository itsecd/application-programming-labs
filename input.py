import argparse


def value_input() -> argparse.Namespace:
    """
    Функция, позволяющая осуществить ввод ключевого слова, пути к директории, кол-ва изображений, пути к файлу для аннотации
    :return: аргументы
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('path_image', type=str, help='Путь к изображению')
    parser.add_argument('path_new_image', type=str, help='Путь для сохранения нового изображения')
    arg = parser.parse_args()
    return arg