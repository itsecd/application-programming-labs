import re
import argparse
import filter_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)
    args = parser.parse_args() 
    
    if args.filename == "data.txt":
        print(f"\nКол-во человек, которые родились в 21 веке: {filter_data.count_data(args.filename, 2000)}")
    else:
        print("Файл с таким именем не найден!")
