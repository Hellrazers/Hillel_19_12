# list_of_nambrs = list(range(4))
#
# iter_list = iter(list_of_nambrs) #[0, 1, 2, 3]
#
# for elment in iter_list:
#     print(elment)
#     next(iter_list)

# first = next(iter_list)
#
# second = next(iter_list)
# third = next(iter_list)
# print(first, second, third)
#
#
#
# third = next(iter_list)
#


class MyIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_num:
            self.current += 1
            return self.current
        else:
            raise StopIteration



# Використання власного ітератора
my_iterator = MyIterator(5)
# for num in my_iterator:
#     print(num)

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
#


# Приклад використання ітератора для списку
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# Приклад використання ітератора для словника
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(key, value)

# Приклад використання ітератора для рядка
my_string = "Hello"
for char in my_string:
    print(char)