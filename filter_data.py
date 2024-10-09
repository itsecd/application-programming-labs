import re
import argparse

def count_data(filename: str, data: int) -> int:
    with open(filename, "r") as file:
        text = file.readlines()
    
    pattern = r'[.]\d{4}'
    count_data = 0
    for i in range(len(text)):
        if(re.search(pattern,text[i])):
            date = re.findall(pattern, str(text[i]))
            if(int(date[0][1:]) >= 2000):
                count_data+=1
                print(date[0][1:])
    return count_data

