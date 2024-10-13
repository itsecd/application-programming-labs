import csv
import argparse
import os
from icrawler.builtin import GoogleImageCrawler


def parsing():
    """
    Парсинг аргументов командной строки
    """
    parser = argparse.ArgumentParser(description='Download images and create annotations.')
    parser.add_argument('keyword', type=str, help='Keyword for image search')
    parser.add_argument('save_dir', type=str, help='Directory to save images')
    parser.add_argument('annotation_file', type=str, help='Path to the annotation CSV file')
    args = parser.parse_args()
    return args

def download_images(keyword, save_dir, num_images=50):
    """
    Скачивание изображений в save_dir
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    crawler = GoogleImageCrawler(storage={'root_dir': save_dir})
    crawler.crawl(keyword=keyword, max_num=num_images)

def create_annotation_csv(save_dir, annotation_file):
    """
    Создание аннотации к изображениям
    """
    with open(annotation_file, 'w', newline='') as csvfile:
        fieldnames = ['absolute_path', 'relative_path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames) #Создание объекта DictWriter модуля csv для записи данных в формате словаря, где список строк fieldnames используется в качестве заголовков столбцов csv файла
        writer.writeheader() #Запись строки заголовков в csv файл

        for root, _, files in os.walk(save_dir): #Рекурсивный обход файлов в директории (отсутствие dirs - _)
            for file in files:
                if file.endswith(('jpg', 'jpeg', 'png')):
                    abs_path = os.path.join(root, file) #Соединение в абсолютный путь
                    rel_path = os.path.relpath(abs_path, start=save_dir) #Поиск относительного пути. Функция os.path.relpath вычисляет относительный путь от abs_path до save_dir. Например, если abs_path = '/save_dir/subdir1/file1.jpg' и save_dir = '/save_dir', то rel_path будет subdir1/file1.jpg.
                    writer.writerow({'absolute_path': abs_path, 'relative_path': rel_path}) #Запись путей по колонкам csv файла

class ImageIterator:
    """
    Класс Итератора для картинок
    """
    def __init__(self, annotation_file=None, folder_path=None):
        self.images = []
        if annotation_file:
            with open(annotation_file, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.images.append(row['absolute_path'])
        elif folder_path:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(('jpg', 'jpeg', 'png')):
                        self.images.append(os.path.join(root, file))
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.images):
            image_path = self.images[self.index]
            self.index += 1
            return image_path
        else:
            raise StopIteration

def main():
    args = parsing()
    try:
        download_images(args.keyword, args.save_dir)
        print("\n\nКартинки загружены успешно")
        create_annotation_csv(args.save_dir, args.annotation_file)
        print("Папка аннотаций успешно создана")

        # Проверка итератора
        print("Проверка итератора с файлом аннотации:")
        iterator = ImageIterator(annotation_file=args.annotation_file)
        for image_path in iterator:
            print(image_path)

        print("\nПроверка итератора с папкой:")
        iterator = ImageIterator(folder_path=args.save_dir)
        for image_path in iterator:
            print(image_path)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()