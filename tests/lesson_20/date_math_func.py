from datetime import datetime, UTC, timedelta

from _zoneinfo import ZoneInfo

# dt_1 = datetime(2023, 12, 31, 5, 59, 59)
# dt_2 = datetime(2022, 12, 31, 23, 59, 59)
# #365 5, 59, 59  - 23, 59, 59 =  - 18 годин 365 (364d + 24h - 18h)
# print((dt_2 - dt_1))
# #-365 dniv 23, 59, 59 - 5, 59, 59 = 18годин (-365d  - 18h)
# print(abs(dt_2 - dt_1))
# print((dt_1 - dt_2))
# print( 2 - 5 )
# print( abs(2 - 5) )
# print(dt_2 > dt_1)
# print(dt_1 > dt_2)
# print(dt_1 == dt_2)
# dt_2 = datetime(2023, 12, 31, 5, 0, 0, tzinfo=ZoneInfo('Europe/Kyiv'))
# print(dt_1 == dt_2, 'with TZ')
#
# td1 = timedelta(days=10, hours=15, seconds=24, minutes=45)
#
#
#
# print(dt_1 + td1)
# dt_1.replace(tzinfo=ZoneInfo('Europe/Kyiv'))
# print(dt_1)

# # Original datetime object
# flight = datetime(2025, 3, 15, 10, 0, 0)
# print(f"Original flight time: {flight}")
#
# # Reschedule the flight to March 20th at 3:30 PM (15:30)
# rescheduled_flight = flight.replace(day=20, hour=15, minute=30)
# print(f"Rescheduled flight time: {rescheduled_flight}")
#
# # Change only the year
# next_year_flight = flight.replace(year=2026)
# print(f"Next year flight time: {next_year_flight}")
#
# dt_1 = datetime(2023, 12, 31, 3, 0, 0, tzinfo=ZoneInfo('UTC'))
# print(f"Date 1 flight time: {dt_1}")
# after_replace = dt_1.replace(tzinfo=ZoneInfo('Europe/Kyiv'),month=11, day=30, hour=15, minute=30)
# print(f"After replaced flight time: {after_replace}")

def is_diff_more_30_sec(time_A:datetime, time_B:datetime):
		# Обчислення різниці у часі
      time_difference = time_B - time_A
		# поверне True, якщо різниця більше 31 секунди
      return time_difference > timedelta(seconds=31)

# Перевірка роботи
time_a = datetime.now()  # отримаємо поточний час
time_b = time_a + timedelta(seconds=32) # штучно збільшимо його на 32 секунди
if is_diff_more_30_sec(time_a, time_b):
   print("WARNING! Різниця більше 31 секунд!")
