def square(x):  # 计算平方数
    return x ** 2


l = list(map(square, [1, 2, 3, 4, 5]))
print(l)
list1 = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(list1)

# 提供了两个列表，对相同位置的列表数据进行相加
list2 = list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
print(list2)
