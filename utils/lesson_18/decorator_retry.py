# Параметризований декоратор для встановлення максимальної кількості повторних спроб
import time


def retry(max_retries, delay = 5):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    # Спроба виклику функції, яку декоруємо
                    return func(*args, **kwargs)
                except Exception as e:
                    # Обробка помилки та вивід повідомлення про спробу
                    print(f"Помилка: {e}. Повторна спроба {retries + 1}/{max_retries}")
                    retries += 1
                    time.sleep(delay)

                # except Exception as e:
            # Викидаємо виняток, якщо досягнуто максимальну кількість спроб
            raise Exception("Досягнуто максимальну кількість спроб")
        return wrapper
    return decorator

# retry(max_retries = 5, delay = 5)(connect_to_server)
# @retry(max_retries = 5, delay = 5)

# Параметризоване застосування декоратора
@retry(max_retries=3, delay=5)
def connect_to_server():
    # Спроба з'єднатися з сервером
    # raise ConnectionError("Не вдалося підключитися до сервера")
    raise ValueError


#
# @retry(max_retries=3, delay=5)
# def func_add(a, b):
#      raise
# Виклик функції
# connect_to_server()

# func_add(5, 5)