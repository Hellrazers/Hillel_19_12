import zoneinfo
from datetime import datetime, timedelta, timezone
import time

from zoneinfo import available_timezones

from _zoneinfo import ZoneInfo

# 1. Получаем текущее время (timestamp)
now = time.time()
print("Timestamp:", now)

# 2. Преобразуем timestamp в объект datetime (локальное время)
my_datetime = datetime.fromtimestamp(now)
print("Локальная дата та час:", my_datetime)

# 3. Создаем часовой пояс +4 часа (timezone)
tz_plus_4 = timezone(timedelta(hours=4))

# 4. Изменяем часовой пояс для объекта datetime
update_tz = my_datetime.astimezone(tz_plus_4)
print("Час у часовому поясі +4:", update_tz)

tz_euroope = [zones for zones in available_timezones() if zones.startswith("Europe") and zones.endswith("v")]
print(tz_euroope)


update_kyiv = my_datetime.astimezone(ZoneInfo('UTC'))
print("Час у часовому поясі +4:", update_kyiv)

print(update_tz.tzinfo)

print(update_kyiv.tzinfo)
