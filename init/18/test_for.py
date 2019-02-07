a_dict = {}
for i in range(1,11):
    a_dict[i] = 0

print(a_dict)


b_dict = {i :0 for i in range(1, 11)}
print(b_dict)


a_list= []
for i in range(1,11):
    if( i % 2 == 0):
        a_list.append(i*i)
print(a_list)


b_list = [i*i for i in range(1, 11) if(i % 2 ==0)]

print(b_list)