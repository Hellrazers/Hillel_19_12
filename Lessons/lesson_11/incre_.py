class Animal: #Employee

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cat(Animal): #developer

    ANIMAL_TYPE = "Cat"

    def __init__(self, cat_value, **kwargs):
        super().__init__(**kwargs)
        self.cat_value = cat_value


class DOG(Animal): #Manager
    ANIMAL_TYPE = "Dog"

    def __init__(self, dog_value,  **kwargs):
        super().__init__(**kwargs)
        self.dog_value = dog_value


class CatDog(Cat, DOG):
    ANIMAL_TYPE = "CatDog"

    def __init__(self, name, age, cat_value):
        super().__init__(name = name,
                        age = age,
                        dog_value = 123123,
                        cat_value= cat_value)

        # self.dog_value = dog_value



print(CatDog.mro())
cat_dog = CatDog("CatDog", 40, 'dog_value')
print(cat_dog.dog_value)