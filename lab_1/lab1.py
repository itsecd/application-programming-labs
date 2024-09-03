import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str)
args = parser.parse_args()

with open(args.filename, "r") as file:
    text = file.read()

pattern = r"\+7\s+\d{3}"
codes = re.findall(pattern, text)

codes_dict = dict()
for i in codes:
    code = i[i.find("+7") + 2:].strip()
    if code in codes_dict.keys():
        codes_dict[code] += 1
    else:
        codes_dict[code] = 1

print(f"The most common operator code is {max(codes_dict, key=codes_dict.get)}.")
