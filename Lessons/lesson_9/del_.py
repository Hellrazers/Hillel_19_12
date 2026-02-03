class Person(object):
    def __init__(self, name, age:int = None):
        self.name = name
        self.age = age if age != 0 else print("Validatrion erorr")
        # self.some_list = some_list or []

    # def __del__(self):
    #     print(f"object with name {self.name} and age {self.age} deleted")

    def __str__(self):
        return f"My name is: {self.name} and my age is: {self.age}"

    def __repr__(self):
        return f"Class Person with name {self.name} and age {self.age}"


    def __call__(self):
        print(f"My name is {self.name} and my age is {self.age}")

    def prtint_somtheing(self):
        print(f"My name is {self.name} and my age is {self.age}")


    def __setattr__(self, key, value):
         super.__setattr__(self, key, value)
    #     if key == "age" and value is None:
    #         raise AttributeError(f"Cannot set age attribute, becouse {value} is None")
    #     elif key == "age" and value == 0:
    #         raise ValueError(f'our age are: {value}')
    #     if key == "name" and len(value) == 0:
    #         raise ValueError(f"Cannot set name attribute, becouse {value} is None")

    def __getattr__(self, key):
        return f"Getting {key}"

    def __len__(self):
        return self.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age




class Student:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age




    # def __eq__(self, other):
    #     if isinstance(other, Person):
    #         return self.age == other.age
    #     elif isinstance(other, int):
    #         return self.age == other
    #     elif isinstance(other, str):
    #         return self.age == int(other)
    #     raise NotImplementedError

# __gt__ (greater than ) >
# __ge__ (greater and equals ) >=
# __lt__ (less than ) <
# __le__ (less and equals ) <=
# __eq__ (equals) ==
bob = Person(name = "Bob", age = 18)
viktro = Person(name = "Viktro", age = 25)


bob.prtint_somtheing()
bob()
print(callable(bob), 'callable obj')
# bob()
print(bob == 18)
print(bob == '18')

print(bob == viktro)


print(bob.name)
print(bob.__getattr__('name'))
print(getattr(bob, 'name'))

# def values(a, b, c = []):
#     c.append(a + b)
#     return c
#
# list_1 = values(1, 2)
# print(list_1)
# list_2 = values(4, 4)
# print(list_2)
#
# class Ivan(object):
#     pass
# class Student:
#     pass
# # def some_value(self):
#     #     print(f"My name is {self.name} and my age is {self.age}")
#
# bob = Person(name = "Bob", age = 18)
# bob.name = ""
# # viktor = Person("Viktor", 19)
# #
# # .get('asd', 'asdasd')
# # ['asdasd']
#
# print(getattr(bob, "email", "Not exist"))
# setattr(bob, "email", "admin@gmail.com")
# # delattr(bob, "email")
# # print(bob.email)
# print(bob.age)
# setattr(bob, "age", None)
# print(bob.age)
#
#
# # viktor.age = 30
# # print(bob.age > viktor.age )
# #
# # print(bob > viktor, 'gt' )
# # print(bob.__gt__(viktor))
# # print(viktor >= bob, 'ge')
# # print(bob == viktor, 'eq')
# #
# # #
# # int_value = int(bob)
#
# # rep_value = repr(bob)
# # print(rep_value, "System print")
# # print(int_value)
# # some_str = bob
# # bob.some_value()
# # print(str(bob))
# # print([bob, viktor])
#
#
# # bob2 = Person("Bob2", 20)
# # del bob
#
# # print(bob)
#
#
# # class FileHandler:
# #     def __init__(self, filename, mode):
# #         self.filename = filename
# #         self.mode = mode
# #         self.file = open(filename, mode)
# #
# #     def read_data(self):
# #         return self.file.read()
# #
# #     def __del__(self):
# #         self.file.close()
# #         print(f"File {self.filename} has been closed.")
# #
# # # Використання об'єкта та автоматичний виклик деструктора
# # file_handler = FileHandler("example.txt", "r")
# # data = file_handler.read_data()
# # print(data)
# # del file_handler
# #
# # with open("example.txt", ) as file:
# #     data2 = file.read()
# #     print(data2)
# #
# # file
# bob.some_list = [1, 3, 45]
# print(bob.some_list)
# #
# #
# # while True:
# #     print(True)