class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age



class Cat(Animal):

    ANIMAL_TYPE = "Cat"

    def __init__(self, name, age, value, value2):
        super().__init__(name, age, value2)
        # self.value = value
        # Animal.__init__(self, name, age)
        # super().__init__(name, age)
        self.value = value


    def __str__(self):
        return f"This class is cat with {self.ANIMAL_TYPE}, {self.name}, {self.age}"

    @staticmethod
    def make_sound():
        print("MRRR...")

class DOG(Animal):
    ANIMAL_TYPE = "Dog"

    def __init__(self, name, age, value2):
        super().__init__(name, age)
        # Animal.__init__(self, name, age)
        # Animal.__init__(self, name, age)

        # self.name = name
        # self.age = age
        self.value2 = value2

    def __str__(self):
        return f"This class is cat with {self.ANIMAL_TYPE}, {self.name}, {self.age}"

    @staticmethod
    def make_sound():
        print("GRRR...")


# cat = Cat('cat', 25, 34)
# dog = DOG('dog', 45, 56)
# print(cat)
# print()
# print(dog)

class CatDog( Cat, DOG ):
    ANIMAL_TYPE = "CatDog"

    def __init__(self, name, age, value, value2):
        super().__init__(name, age, value, value2)
        # Cat.__init__(self, name, age, value)
        # DOG.__init__(self, name, age, value2)

    @staticmethod
    def make_sound():
        Cat.make_sound()
        print(Cat.ANIMAL_TYPE)
        DOG.make_sound()
#

def test_name_in_classes():
    print('Starting our test')
    cat_dog = CatDog("Cat Dog", 10, 20, 54)

    assert cat_dog.name == "Cat Dog"

    assert cat_dog.age == 10

    print('Ending our test')



test_name_in_classes()
# class DogCat( DOG, Cat ):
#     ANIMAL_TYPE = "CatDog"
#
#     def __init__(self, name, age, value, value2):
#         # super().__init__(name, age, value, value2)
#         Cat.__init__(self, name, age, value)
#         DOG.__init__(self, name, age, value2)
#
#     @staticmethod
#     def make_sound():
#         Cat.make_sound()
#         print(Cat.ANIMAL_TYPE)
#         DOG.make_sound()
print(CatDog.mro(), 'CatDog( Cat, DOG ) спочаттку Cat потім Dog')

catDOG = CatDog("Cat", 15, 2, 4)


# print(DogCat.mro(), 'DogCat( DOG, Cat ) спочаттку Dog потім Cat')

# catDOG =CatDog("Cat", 15, 2, 4)
# print(catDOG.make_sound())
# print(catDOG)



# class Animal:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#
# class Cat(Animal):
#
#     ANIMAL_TYPE = "Cat"
#
#     def __init__(self, name, age, value, value2):
#         super().__init__(name, age, value2)
#         self.value = value



# # Base_loging
#
# def __init__(self, api):
#     self.api = api
#     def_url = "127.0.0.1"
#
#
# login page (Base_loging)
#
#     super.__init__(api)
#     url = def_url + '/api/v1/login'