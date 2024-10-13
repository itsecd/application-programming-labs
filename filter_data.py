import re


def count_data(text: list, year: int) -> int:
    """" Displays the number of records that were born later than the specified year"""
    pattern = r'[.]\d{4}'
    count_of_data = 0
    for i in range(len(text)):
        if(re.search(pattern,text[i])):
            date = re.findall(pattern, str(text[i]))
            if(int(date[0][1:]) >= year):
                count_of_data+=1
    return count_of_data

