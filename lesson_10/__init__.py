# Поїзд складається з вагонів, перший вагон — локомотив.
#
# У поїзді може бути тільки один локомотив.
#
# Локомотив не може перевозити пасажирів.
#
# Кожен звичайний вагон може перевозити не більше 10 пасажирів.


class Wagon:
    MAX_PASSANGER = 10

    def __init__(self, is_locomotive: bool= False):
        self.passanger: list = []
        self.is_locomotive: bool = is_locomotive

    def add_passanger(self, passanger_name):
       if len(self.passanger) > self.MAX_PASSANGER:
           raise ValueError(f'{len(self.passanger)} > {self.MAX_PASSANGER}')
       if self.is_locomotive:
           raise ValueError(f'Локомотив не може перевозити людей')
       return self.passanger.append(passanger_name)

    def __repr__(self):
        if self.is_locomotive:
            return "LOKOMOTIVE WAGON"
        else:
            return f"WAGON with passangers {self.passanger} "

    def __str__(self):
        if self.is_locomotive:
            return "LOKOMOTIVE WAGON STR"
        else:
            return "WAGON STR"


class Train:
    def __init__(self):
        self.wagons = [Wagon(is_locomotive=True), ]

    def add_wagon(self, wagon: Wagon):
        if wagon.is_locomotive:
            raise ValueError("Can't add locomotive wagon")
        self.wagons.append(wagon)

wagon1 = Wagon()
wagon1.add_passanger('Viktor')
wagon1.add_passanger('Vanya')
wagon1.add_passanger('Sanya')
wagon2 = Wagon()
wagon2.add_passanger('LISA')

train = Train()
print(train.wagons)
print(train.wagons[0])
train.add_wagon(wagon1)
train.add_wagon(wagon2)

print(train.wagons)
print(wagon1.passanger)