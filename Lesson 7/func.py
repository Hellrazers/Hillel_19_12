# #
# # def new_fucntion():
# #     for i in range(3):
# #
# #         print(f"{i} - Hello world!")
# #     return [12345, 2342,34,234,23 ]
# #
# # pass
# #
# def multy_numbers (a: str, b: int = 15) -> str:
#     """
#
#     :param a: enter your string (str)
#     :param b: enter your number (int)
#     :return: a * b
#     """
#     return a * b
#
# # sum = multy_numbers(15, 3)
# # print(sum)
# #
# # def asd(a):
# #     return a
# #
# print(multy_numbers('--------') )
# #
# #
#
#
# def greeding(name: str, surename: str, age: int, is_student: bool = True) -> None:
#     """This fuctrional wortks only for printing some senta
#
#
#     :param name: enter your name (str)
#     :param surename: enter your surename  (str)
#     :param age: enter your age (int)
#     :param is_student: optional parameter (bool = True)
#     :return: None
#     """
#     if is_student is True:
#         print(f"Hello, my name is {name} {surename}, I'm {age} years old, and I'm a student")
#     else:
#         print(f"Hello, my name is {name} {surename}, I'm {age} years old, and I'm not a student")
#
#
# greeding(name= 'Oleksii', surename= "asd", age = 33 )
#
# greeding(surename='Oleksii', name=33,  age="asd", is_student=False )
#
#
from idlelib.tree import TreeItem

# def args_fuc( *args, int_value: int) -> int | float:
#     new_list = []
#     for index, value  in enumerate(args):
#         if index % 2 == int_value and isinstance(value, int):
#             new_list.append(value)
#             print(new_list)
#     return sum(new_list)
#
# #
# #
# # print(args_fuc(1,2,3, 'asd', 4,5,6,7,8,9,10, '', True))
# # print(args_fuc(*list(range(10)), 2))
# print(args_fuc(1.5, 2,3, 4,545 , int_value = 1))
#
#
# print(*list(range(10)))
# print(list(range(10)))

# def some_kwange(table: str, **kwargs):
#     sql_string = f'SELECT FROM {table} WHERE'
#     for key, value in kwargs.items():
#         sql_string += f' {key} = {value} AND'
#     print(sql_string)
#
# some_kwange(table = 'users', id = 1, isDeleted = False, status = True)
#
# def some_sql_req(table: str, id, status ):
#     return  f'SELECT FROM {table} WHERE id = {id} AND status = {status}'
# print(some_sql_req(table = 'users', id = 1, status = True, isDeleted = False))


# some_value = lambda x: x + 1
# print(some_value(1))
#
#
#
# list_10 = list(range(10))
#
# filter_obj = filter( lambda element : element % 2 == 0, list_10)
# print(filter_obj)
# print(list(filter_obj))
#
# def is_para(a: int):
#     return a % 2 == 0
#
#
# print(list(filter(is_para, list_10)))
#
#
# new_list = []
# for element in list_10:
#     if element % 2 == 0:
#         new_list.append(element)
#
# print(new_list)
#
# new_list_LC = [element * index for index, element in enumerate(list_10) if element % 2 == 0 ]
# print(new_list_LC)


new_value = list(range(10))

def add_value(a):
    return a **a

map_value = map(add_value, new_value)
print(new_value)
print(list(map_value))
# print(map_value)
# map_value2 = map(pow(int, int), new_value)
# print(list(map_value2))

new_map_value = []
for element in new_value:
    new_map_value.append(element ** element)
print(new_map_value)

new_map_value_lc = [element ** element for element in new_value]
print(new_map_value_lc)

# some_value = 5
#
# print(type(some_value))
#
#
# class SomeClass(int):
#     pass
#
# some_calss = SomeClass(4)
#
# print(type(some_calss))
# print(isinstance(some_calss, str))
#
# print(isinstance(some_value, int))
#
# asd = {
#     "name": {
#         'name': [1, 2, 3]
#     }
# }
# value_2 = asd.get('name').get('name')[0]
# print(isinstance(value_2, int))
# print(type(value_2) is str)
#
#
#
# print(some_calss)

# print(SomeClass)
# print(type(SomeClass(3)))

# new_list_LC = [element for element in list_10 if element % 2 == 0]
# for element in list_10:
#     if element % 2 == 0:
#       new_list_LC.append(element)
list_of_words = ['apple', 'banana', 'cherry']
upper_words = list(map(str.title, list_of_words))
print(upper_words)
string_value = 'asd'


print(string_value.title())
# [
#     {id : 123,
#      value: 123,
#      isDeleted: true }
# ]
#
list_range = list(range(5, 10))
print(list_range)

for element in list_range:
    print(element > 4)
print("----" * 80)
print('List range: ', all(list_range) < 4)
all_true_1 = all([not False,not False, not False])
list_bool = [not False,not False, not False]
print(list_bool[0] is True and list_bool[1] is True and list_bool[2] is True)
all_true = all([True, True, True])
# if all_true_1:
#     print('all true')
print(all_true_1)
# print(all_true)
#
# if user[6] => 10 and user[7] => 10:
#     print('users is OKAY')

# all[user[6], usr[10] => 10]

print(any( [True, False, False]))
print(any( [False, False, False]))


# assert 1 == 2, "Some error "





# def trapp( a, b: list = []):
#     return b + a
#
# print(trapp(a= '1'))
# print(trapp(a = '2'))

# #
# #
# # # new_func_call = new_fucntion()
# # # print(new_func_call)
# # # new_fucntion()
# # # new_fucntion()
# # # new_fucntion()
