import csv

class ImgIterator:
    """
    The class represents an image iterator object.
    It iterate files in generated csv file with pathes to images.
    """

    def __init__(self, name: str):
        """
        Init iterator object.

        Parameters:
        name (str): name (without ext.) of csv-file.
        """

        self.csv_file = name
        if not self.csv_file.endswith(".csv"):
            self.csv_file += ".csv"

        self.file_exist = True
    
    def __iter__(self):
        """
        Iter method.
        If target file don't exist set self.file_exist as False.
        """
        
        try:
            self.file = open(self.csv_file, newline="")
        except:
            self.file_exist = False

        self.csvreader = csv.reader(self.file)
        
        return self
    
    def __next__(self):
        """
        Next method for iterations.
        If self.file_exist is not True, don't start the iteration.
        """
        
        if not self.file_exist:
            raise StopIteration
        
        try:
            return self.csvreader.__next__()
        except StopIteration:
            self.file.close()
            raise StopIteration
