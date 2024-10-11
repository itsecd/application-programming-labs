import re
def read_file(filename:str) -> list:
    """" Open the file and read data by lines"""
    with open(filename, "r") as file:
        text = file.readlines()
    return text

def count_data(filename: str, data: int) -> int:
    """" Displays the number of records that were born later than the specified year"""
    text = read_file(filename)
    pattern = r'[.]\d{4}'
    count_data = 0
    for i in range(len(text)):
        if(re.search(pattern,text[i])):
            date = re.findall(pattern, str(text[i]))
            if(int(date[0][1:]) >= data):
                count_data+=1
    return count_data

