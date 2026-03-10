import time


date_now = time.time()


# time.sleep(2)
print(time.time() - date_now)



current_time = time.localtime()
print(current_time)
print("Рік:", current_time.tm_year)
print("Місяць:", current_time.tm_mon)

print(time)