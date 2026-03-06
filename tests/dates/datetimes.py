import time as time_2
from datetime import datetime, date, time


time_string_1 = '2024-02-29 23:59:59'
time_string_2 = '2023-31-12T23:59:59.12312 +04:00'
time_string_3 = '23-12-31 11:59:59 AM'
time_string_4 = '2023/12/31T23:59:59Z'

dt = datetime(2023, 12, 31, 23, 59, 59)
date_now = dt.date()
# print(date_now)
# print(dt)

def str_to_date(date_string) -> datetime:
    return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

date_1 = str_to_date(time_string_1)
# date_1.
# date_2
# date_1 > date_2
print(date_1 , ' Try func str_to_date')
date_dt_1 = datetime.strptime(time_string_1, "%Y-%m-%d %H:%M:%S")
print(date_dt_1)
# print(date_dt_1.date().day)
# date_dt_2 = datetime.strptime(time_string_2, "%Y-%d-%mT%H:%M:%S.%f %z")
# print(date_dt_2)
# print(date_dt_2.tzinfo)
# date_dt_3 = datetime.strptime(time_string_3, "%y-%m-%d %I:%M:%S %p")
# print(time_string_3)

now = time_2.time()
print(now)

# Перетвоюємо обєкт struct_time у datetime
my_datetime = datetime.fromtimestamp(now)
print("Поточна дата та час:", my_datetime)
