# #
# # list = [1, 2, 3, 1, 5, 6 ,4 ,3,2,1,]
# #
# # # print(list.sort(reverse=True))
# # # print(list )
# # # string = ' asd nasdn asnd ansdn asndn asnd nasdgds fdg dfg dfgewr,wel;r dfg;'.split()
# # # list_2 = sorted(string) #Return LIST
# # # print(list_2)
# #
# #
# #
# # my_dict = {
# #     "id": 1,
# #     3+ 4: "asd",
# #     "name": "John",
# #     "surname": "Doe",
# #     "age": 30,
# #     "city": "New York",
# #     False: 123,
# #     None: 123,
# #     (1,): 45,
# #     "new_dict": {
# #         "key": "value",
# #         "id": 23,
# #         123: 34556,
# #         "ids": [1, 2, 3]
# #     },
# #     "new": [
# #         {
# #             "key": "value", "id": 454,"name": "asd" },
# #         {
# #             "key": 1123
# #         }
# #
# #     ]
# #     # [1, 2] : 'asd'
# # }
# #
# #
# #
# # new_dict = my_dict.copy()
# # print(new_dict)
# #
# #
# # import copy
# # new_dict_3 = copy.deepcopy(my_dict)
# #
# # my_dict['new_dict']['id'] = True
# #
# # new_dict['age'] = True
# # # print(f"new_dict['age']    - {new_dict['age']}")
# # # print(f"my_dict['age']    - {my_dict['age']}")
# #
# # # print(new_dict_3)
# # new_dict['new_dict']['ids'] = []
# #
# # print(f"new_dict['new_dict']['ids']    - {new_dict['new_dict']['ids']}")
# # print(f"my_dict['new_dict']['ids']    - {my_dict['new_dict']['ids']}")
# #
# # print(my_dict)
# # print(new_dict)
# # print(new_dict_3)
# #
# #
# #
# # # print(type(range(10)))
# # # print(set(range(10))) #[0,.....9]
# # # print(range(10, 15))#[10.....14]
# #
# #
# #
# #
# #
# #
# # squares = {x: x**2  for x in range(10)}
# # print(squares)
# # print(type(squares))
#
# list_1 = [1, 2, 3, 4, 5]
# list_2 = ['123 123', 234, 234]
# some_value = 1
#
#
# # list_1.append(list_2)
# # list_1.extend(some_value)
# # print(list_1[-1])
# for element in list_2:
#     list_1.append(element)
#
#
# print(list_1)


tuple_of_elements = (1 , 2 , 3, 4, 5)

new_sorted_value = sorted(tuple_of_elements)

print(new_sorted_value)
