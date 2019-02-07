list = [1, 2, 3]

for i in list:
    print(i)

iterator = iter(list)
print(next(iterator))
print(next(iterator))

print('-------')

for i in range(10, 20):
    print(i)
print('-------')


for i in range(10, 20, 2):
    print(i)
print('-------')

def frange(start, stop, stem):
    x = start
    while x < stop:
        yield x
        x = x + stem


for i in frange(10, 20, 0.5):
    print(i)