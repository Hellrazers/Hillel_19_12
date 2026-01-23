class Car:
    def __init__(self, make, model):
        self.make = make          # Public attribute
        self._model = model        # Protected attribute
        self.__year = 2022         # Private attribute

    def display_model(self):
        print(f"Model: {self._model}")

    def update_year(self, new_year):
        self.__year = new_year
        print(self.__year)


    def __setattr__(self, key, value):
        if key == '_Car__year' and value < 2000:
            raise ValueError(f"Our lover than 2000 ")


class Bmw(Car):
    def __init__(self, make, model, year):
        super().__init__(self, make)
        self.year = year
        self.model = model

# bmw = Bmw("BMW", "BMW", "2001")
car = Car ("car", "car")

# print(bmw.model)

car.update_year(1000)

#
# bmw = Car("BMW", "x-5")

# print(bmw._model)
#
# bmw.display_model()
#
# bmw.update_year(2001)

# print(bmw._Car__year)
