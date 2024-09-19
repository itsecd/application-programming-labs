# Лабораторная работа № 2
# Web Scraping

- [Теория](#теория)
  - [csv](#csv)
  - [Создание собственных итераторов](#создание-собственных-итераторов)
  - [icrawler](#icrawler)
  - [Полезные ссылки](#полезные-ссылки)
- [Задание](#задание)
  - [Общее задание](#общее-задание)
  - [Варианты](#варианты)

# Теория

## csv

Для работы с CSV файлами в Python можно использовать встроенный модуль `csv`.

Пример:

```py
import csv

# данные для записи
data = [
    ["Имя", "Возраст", "Город"],  # Заголовки
    ["Алексей", 30, "Москва"],
    ["Мария", 25, "Санкт-Петербург"],
    ["Иван", 22, "Екатеринбург"]
]

# запись данных в CSV файл
with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data) # запись всех строк

# дозапись в файл
with open('data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Ирина", 33, "Сочи"])
```

## Создание собственных итераторов

Итераторы — это объекты, которые позволяют перебирать другие объекты, такие как списки и кортежи, без необходимости обращаться к ним по индексу. Чтобы создать собственный итератор, необходимо в классе реализовать два метода: `__iter__()` и `__next__()`.

- `__iter__()` — возвращает экземпляр итератора. Обычно это просто self.
   
- `__next__()` — возвращает следующий элемент последовательности. Если элементов больше нет, он должен вызвать исключение StopIteration для уведомления о завершении перебора.

Пример создания собственного итератора:

```py
class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit  # ограничение
        self.counter = 0  # счётчик

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

iterator = SimpleIterator(3)

for val in iterator:
    print(val)
```

Результат работы:

```
0
1
2
```


## icrawler

`icrawler` предоставляет удобные инструменты для скачивания изображений из различных интернет-ресурсов. Этот модуль поддерживает несколько источников, таких как Google Images, Bing Images, Flickr и другие.

Установка:

```
pip install icrawler
``` 
или 
```
conda install -c hellock icrawler
```

Модуль icrawler включает в себя несколько классов, каждый из которых предназначен для работы с определенным источником изображений. Вот несколько ключевых элементов:

1. ImageDownloader: Класс, который будет отвечать за загрузку изображений.

1. Crawlers: Различные классы для осуществления поиска изображений из разных источников, например:
   - GoogleImageCrawler
   - BingImageCrawler
   - FlickrImageCrawler

Пример:
```py
from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': 'images'})
google_crawler.crawl(keyword='cat', max_num=100)
```

- `storage` - параметры хранения (папка, формат и т.д.). В данном случае изображения будут сохранены в папке `images`.
- `keyword` - ключевое слово для поиска.
- `max_num` - максимальное количество изображений для загрузки.

## Полезные ссылки

- [csv (doc)](https://docs.python.org/3/library/csv.html)
- [создание итераторов](https://www.pythonforbeginners.com/basics/how-to-create-an-iterator-in-python)
- [icrawler (doc)](https://icrawler.readthedocs.io/en/stable/)


# Задание
## Общее задание

- Скачайте от 50 до 1000 изображений своего варианта с помощью icrawler. 
- Составьте аннотацию в виде csv-файла, в котором будет абсолютный и относительный путь к каждому изображению.
- Напишите итератор по изображениям - используйте в качестве параметра конструктора файл-аннотации или путь к папке.

Ключевое слово для поиска (класс изображения), путь к папке для сохранения и путь к файлу аннотации необходимо передавать через аргументы командной строки.

## Варианты

1. cat
1. dog
1. bird
1. monkey
1. horse
1. hedgehog
1. cow
1. pig
1. turtle
1. snake