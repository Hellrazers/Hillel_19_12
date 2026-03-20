import datetime
from dataclasses import dataclass



@dataclass
class ExpensesRequestPost:
    '''
    Expenses request post
    car_id : int
    mileage : int
    liters: int
    totalCost :int
    reportedAt: int = datetime.date.today()
    forceMileage : bool = False
    '''
    carId: int
    mileage: int
    liters: int
    totalCost :int
    reportedAt: int = datetime.date.today()
    forceMileage : bool = False


# {
#   "carId": 1,
#   "reportedAt": "2021-05-17",
#   "mileage": 111,
#   "liters": 11,
#   "totalCost": 11,
#   "forceMileage": false
# }