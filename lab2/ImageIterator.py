import csv
import os


class ImageIterator:
    def __init__(self, path: str):
        self.path = path
        self.annotation = self.read_file(self.path)
        self.limit = len(self.annotation)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            next_el = self.annotation[self.counter]
            self.counter += 1
            return next_el
        else:
            raise StopIteration

    def read_file(self, path: str) -> list:
        with open(self.path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # skip the header
            list_of_pic = list(row[1] for row in reader)
            return list_of_pic
