
import re

def findItem(hero):
    with open("sanguo.txt", encoding='utf-8') as f:
    # with open("sanguo_gb18030.txt", encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        i = len(re.findall(hero, data))
        print(hero, i)
    return i



names_dict = {}

with open('name.txt') as f:
    for line in f:
        names = line.split('|')
        for name in names:
            num = findItem(name)
            names_dict[name] = num

name_sorted = sorted(names_dict.items(), key=lambda item: item[1], reverse=True)
print(name_sorted[0:10])