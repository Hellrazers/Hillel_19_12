my_set = {1, 2, 3}

value = 123 + 123
my_set2 = {1, (1, 23), None, False, "asd", 123.45, value}

# list_ids = [1, 2, 3, 4]
# my_set3 = set(list_ids)
# print(f'len {len(list(my_set))}')
# print(list(my_set))
# assert list(my_set) != list_ids
# assert len(list(my_set)) == len(list_ids)

set_2 = {1, 2, 3,}
set_3 = (2, 3, 4, '123123')
list_4 = [3, 4]
print(set_2.union(set_3))
print(set_2.intersection(set_3))
# print(set_2.difference(list_4))

list = {user : [
    {id : 123},
    {id: 345}
]}
print(set_2.symmetric_difference(set_3))
# for element in list_4:
#     if element in set_2:
#         print('TRUE')
# # print(set_2.difference(set_3))
# print(set_2.symmetric_difference(set_3))
# # set_2.update(set_3)
# print(set_2)

some_string = 'Hello word!'
#
# print(list(some_string))
# print(set(some_string))
# print((some_string, ))
# print(set('123'))

#
# print(my_set2)
# # my_set.add([1, 3])
# print(my_set)
#
# my_set.add(4)
# print(my_set)
#
# my_set.add(3)
# print(my_set)
#
# my_set.remove(1)



#
# value = my_set.pop()
# print(value)
# print(my_set.pop())
# print(my_set)