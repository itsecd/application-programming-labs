import csv

class ImageIterator:
    def __init__(self, annotation_file):
        self.annotation_file = annotation_file
        self.images = self.load_images()
        self.limit = len(self.images)
        self.counter = 0

    def load_images(self):
        with open(self.annotation_file, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            return [row[1] for row in reader]
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.images[self.counter - 1]
        else:
            raise StopIteration