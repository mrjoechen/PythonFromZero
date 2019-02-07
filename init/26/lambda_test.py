def add(x, y):
    return x + y

print(add(1, 2))

a = lambda x,y : x+y
print(a(1, 2))


alist = list(filter(lambda x:True if x % 3 == 0 else False, range(100)))
print(alist)


adict = {1:'a', 2:'b', 3:'c'}
for a in adict.items():
    print(a[1])

alam = lambda item:item[1]

for a in adict.items():
    print(alam(a))
