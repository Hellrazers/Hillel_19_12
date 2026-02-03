# my_list = ['value to remove',1, 2, 3, 'value to remove', None, False, {'key': 'value'}, (1, 3, 45)]

# print(my_list[-1])
# print(my_list[:2])
# my_list.append("new value")
# print(my_list)

#remove
# print(my_list)
# string_value = my_list.pop(4)
# print(string_value)
# print(my_list)
# string_2 = my_list.remove('value to remove')
# print(my_list)
# print(string_2)

# my_list.insert(len(my_list) , 'add used by insert')
# print(my_list


#unpacking

my_list = ['id', 1, 2, 3, 4, 5]


[{1 : 32}, {123, 123543,}]

my_list2 = [4, 3, 2]


my_list3 = [value ** 2  for value in my_list2 if value % 2 == 0]


my_list4 = []

for value in my_list2:
    if value % 2 == 0:
        my_list4.append(value ** 2)
    else:
        print("VRONG ")

print(my_list3)


# my_list.extend(my_list2)

for e in my_list2:
    my_list.append(e)
print(my_list)
# print(my_list.index('id'))
# print(my_list[my_list.index('id')])
# first_value, *last = my_list
# print(first_value, last)
# print(type(first_value))
# print(type(other_value))

# first_value, *other_value, last_value = my_list
# print(first_value, other_value, last_value)
#
# *first_value, other_value, last_value = my_list
# print(first_value, other_value, last_value)