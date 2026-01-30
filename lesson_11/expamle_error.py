class OurError(Exception):
    def __init__(self, key,  value):
        message = f'something was wrong our key = {key} value = {value} '
        super().__init__(message)

our_error = OurError('id',1)
#
# try:
#     raise OurError
# except OurError as e:
#     print(e)






# # Приклад використання власного виключення
# try:
#     limit = 100
#     user_input = int(input("Введіть число: "))
#
#     if user_input > limit:
#         raise TooLargeValueError(user_input, limit)
#     else:
#         print("Дякую! Ви ввели припустиме значення.")
# except TooLargeValueError as e:
#     print(f"Помилка: {e}")
# except ValueError:
#     print("Помилка: Будь ласка, введіть ціле число.")