# 将小说的主要人物记录在文件中
# file1 = open('name.txt','w')
# file1.write('诸葛亮')
# file1.close()
#
#
# file2 = open('name.txt')
# print(file2.read())
#
# file2.close()
#
# file3 = open('name.txt','a')
# file3.write('刘备')
# file3.close()
#
# file4 = open('name.txt')
# print (file4.readline())
#
# file5 = open('name.txt')
# for line in file5.readlines():
#     print(line)
#     print('=====')
#
#

# file6 = open('name.txt', encoding='GB18030')
# print('当前文件指针的位置 %s' %file6.tell())
# print ( '当前读取到了一个字符，字符的内容是 %s' %file6.read(1))
# print('当前文件指针的位置 %s' %file6.tell())
# # 第一个参数代表偏移位置，第二个参数  0 表示从文件开头偏移  1表示从当前位置偏移，   2 从文件结尾
# file6.seek(5,0)
# print('我们进行了seek操作')
# print('当前文件指针的位置 %s' %file6.tell())
# print ( '当前读取到了一个字符，字符的内容是 %s' %file6.read(1))
# print('当前文件指针的位置 %s' %file6.tell())
# file6.close()


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
