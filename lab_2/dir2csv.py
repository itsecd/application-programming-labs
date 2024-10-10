import csv
import os

default_name = "some.csv"

def dir2csv(dir: str, csv_path: str = default_name) -> str:
    """
    Function to convert files in directory to csv file with list of links.
    (Don't create parent dirs if don't exists.)
    
    Parameters:
    dir (str): path to directory where stored the images. 
    csv_path (str): path to csv-file for new file. Default: "some.csv".
    """

    if not os.path.split(csv_path)[-1]:
        csv_path += default_name

    if not csv_path.endswith(".csv"):
        csv_path += ".csv"

    with open(csv_path, "w", newline="") as csvfile:
        abs_dir = os.path.abspath(dir)
        names = ("Rel. path", "Abs. path")

        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(names)

        for file in os.listdir(dir):
            abs_path = os.path.join(abs_dir, file)
            rel_path = os.path.relpath(abs_path, start=csv_path)
            print(rel_path, abs_path)

            csv_writer.writerow((rel_path, abs_path))
    
    return csv_path
