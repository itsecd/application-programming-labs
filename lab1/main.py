import argparse
parser = argparse.ArgumentParser()
parser.add_argument('name_file', type=str, help='name file')
args = parser.parse_args()
name_file = args.name_file + ".txt"


with open(name_file, "r", encoding='utf-8') as file:
    text = file.read()
print (text)