def divide(a, b):
    try:
        result =   a / b
    except (ZeroDivisionError, TypeError) as error:
        print(f'My error: {error}')
    except Exception:
        print("Unhandled error")
    else:
        print('My result is', result)
        return result ** 2
    finally:
        print("done our func()")



divide(10, 0)
print('-' * 40)
# time.sleep(30)
divide(10, '1')
print('-' * 40)
print(divide(10, 5))
