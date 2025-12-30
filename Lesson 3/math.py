# print(5/2) #2.5
# print(5//2) #2
# # print(30/0)
# try:
#     print(30/0)
# except ZeroDivisionError:
#     print("Division by zero is not allowed")
#
#
# print(pow(2, 3))
# print(2**3)
#
# list = (1, 2 , 3)
# print(min(list))
# print(max(list))


# my_name = input("Enter your name: ")
# print(f'My name is {my_name} {{a}}')
# my_age = int(input("Enter your age: "))
# print(f'My age is {my_age - 1}\n123123')
# print(110%25)
# coount = 10
# assert coount == (110%25)
# 4 + 1
# 4/2 + 1 / 2
list_list = [1, 2, 3, 5, 'str', 'str'] #len(list_list) == 6
print(list_list)
set_list = set(list_list)
print(set_list)
# assert len(set_list) == len(list_list)
list_2 = tuple(set_list) #len(list_list) == 5
for element  in list_2:
    print('ELEMENT of SET is : ', element)
    assert element == list_list[list_2.index(element)]
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
my_tuple = (1, 2)
my_tuple = (1, 2, 3)

lst = [1, 2, 3, 3, 4, 4]

my_set = set()

for element in lst:
    if lst.count(element) > 1:
        print(element)

print(my_set)