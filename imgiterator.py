import csv

class ImageIterator:
    def __init__(self, csv_path: str) -> None:
        self.csv_path = csv_path
        self.path_list = self.__load_csv()
        self.limit = len(self.path_list)  # ограничение
        self.counter = 0  # счётчик

    def __iter__(self) -> 'ImageIterator':
        return self

    def __next__(self) -> str:
        if self.counter < self.limit:
            next_element = self.path_list[self.counter]
            self.counter += 1
            return next_element
        else:
            raise StopIteration

    def __load_csv(self) -> list:
        with open(self.csv_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader) # skip the header
            path_list = list(row[1] for row in reader)
            return path_list
