row = ("Метод        ','.join(str) використовується        для об'єднання (комбінування)"
       " рядка        зі списку        або ітерабельного           об'єкту за допомогою певного роздільника. Ось приклад використання:")

# row_1 = ['My', 'name', 'is']
# print(row_1)
# print('                '.join(row_1))
#
# list_1 = row.split()
# print(list_1)
# print(' '.join(list_1))
# full_name = list_1[0] + list_1[1]
# full_name += " " + list_1[2]
# print(full_name)


str_1 = 'Hello'
print(id(str_1))

ist_string = ['He', 'llo']
join_str = ''.join(ist_string)
print(id(join_str))
print(str_1 == join_str)
print(str_1 is join_str)