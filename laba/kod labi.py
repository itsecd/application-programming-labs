import argparse
import re

file = open("data.txt", "r", encoding='utf-8')
text = file.read()
file.close()
pattern = "Пол: Мужской"
man_count = re.findall(pattern, text)
print(len(man_count))


"""



strings = file.readline()
print(text)

"""