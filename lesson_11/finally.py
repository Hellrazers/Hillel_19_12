# from import lesson_11.expamle_error.OurError

from lesson_11.expamle_error import OurError

our_error = OurError('id',1)

our_error = OurError('ids',[1, 2 ,4])

def divide(a, b):
    try:
        raise our_error
        result =   a / b
        return  result

    except (ZeroDivisionError, TypeError) as error:
        print(f'My error: {error}')

    except OurError:
        print(f'Our error: {our_error}')

    except Exception:
        print("Unhandled error")

    finally:
        print("done our func()")


divide(10, 0)
print('-' * 40)
# time.sleep(30)
divide(10, '1')
print('-' * 40)
divide(10, 5)
#
# def open_conn():
# #     # raise NotImplementedError
# #     print("Opening connection .. to db")
# #     return True
# # raise ValueError('Invalid creantional')
#
#
# def close_conn():
#     print("Closing connection .. to db")
#
#
#
# def db_execute(some_str):
#     print(f"Executing sql: {some_str}")
#
#
# try:
#     conn = None
#     conn = open_conn()
#     db_execute("select")
# except NotImplementedError:
#         print("something is wrong")
# finally:
#     if conn is not None:
#         print("I want to closing connection")
#         close_conn()
#
#
# Precondition
# open_conn()
#
# test_body
# def test_test1(():
#
#
# post condition
# def close_conn():
#
#
#
# def some_function(age):
#     # value = [1, 2, 3]
#
#     try:
#         if 18 < age < 60: