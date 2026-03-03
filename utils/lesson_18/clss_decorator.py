class MyClass:
    MAX_VALUE = 1000


    def __init__(self, value):
        self.__value = value
        self.new_value = 0


    @property
    def value(self):
        return self.__value

    # def value(self):
    #     return self.__value
    @classmethod
    def class_validate(cls, value):
        cls.function_validate(value)
        return cls.MAX_VALUE

    @classmethod
    def add_to_init(cls):
        # self.new_value = self.MAX_VALUE
        cls.new_value  = cls.MAX_VALUE
        return cls.new_value

    @value.setter
    def value(self, value):
        if self.__value > 0:
            print('More than zero')
        elif self.__value == 0:
            print('Zero')
        else:
            raise ValueError
        self.function_validate(value)
        self.__value += value

    def update_value(self, value):
        self.__value = value

    @staticmethod
    def function_validate(some_value):
        if some_value > 0:
            print('More than zero')
        elif some_value == 0:
            print('Zero')
        else:
            raise ValueError

        return True



class NewClass(MyClass):
    MAX_VALUE = 1
    def __init__(self, value):
        super().__init__(value)
        # self.new_value = self.add_to_init()


    def update_value(self, value):
        MyClass.function_validate(value)
        self.value = value

class FirstClass(MyClass):
    MAX_VALUE = 5
    def __init__(self, value):
        super().__init__(value)
        # self.new_value = self.add_to_init()


    def update_value(self, value):
        MyClass.function_validate(value)
        self.value = value


# print(MyClass(1).add_to_init())
print(FirstClass(1).new_value, 'Значення до виклику нашого методу @classMethod')
print(FirstClass.add_to_init() , 'Викликаєм @classMethod')
print(FirstClass.new_value, 'Значення після виклику нашого методу @classMethod')
# print(MyClass.new_value)
# print(NewClass.class_validate(1))
print(NewClass(1).new_value, 'Значення до виклику нашого методу @classMethod')
print(NewClass.add_to_init() , 'Викликаєм @classMethod')
print(NewClass.new_value, 'Значення після виклику нашого методу @classMethod')

# some_int = 1
#
# my_class = MyClass(5)
#
# print(my_class.value)
#
# my_class.function_validate(some_int)
#
# # my_class.update_value(10)
# my_class.value = 1
#
#
# print(my_class.value)
