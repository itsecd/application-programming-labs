import csv

class ImageIterator:
    def __init__(self, filename: str):
        self.file = filename
        self.images = list()
        self.index = 0
        self.limit = len(self.images)
        with open(self.file, newline='') as my_file:
            reader = csv.reader(my_file)
            next(reader)
            self.images.append(reader)


    def __iter__(self):
        return self


    def __next__(self):
        if self.index < self.limit:
            next_image = self.images[self.index]
            self.index += 1
            return next_image
        else:
            raise StopIteration