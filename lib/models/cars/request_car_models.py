from dataclasses import dataclass


@dataclass
class CarRequestPost:
    carBrandId: int = 1
    carModelId: int = 1
    mileage: int = 1

# @dataclass
# class CarRequestPut: