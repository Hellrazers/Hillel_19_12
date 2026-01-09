# import time
# # import datetime
#
# # WAIT = 1
# # qulity_of_request = 10
# # time_finish = time.time() + qulity_of_request
# # print(time_finish)
# # count = 1
# # #
# #
# #
# # while time.time() < time_finish:
# #     print("-"* 80)
# #     print(f'{count}: {time.time()} зараз такий то час')
# #     time.sleep(WAIT)
# #     if count == 5:
# #         break
# #     count += 1
#     # print("FINISH")
#
# # some_int = 0
#
#
#
# # while some_int < 10:
# #     print("Hello")
# #     print(some_int)
#     # some_int += 1
#
#
# some_int = 0
# list = [1, 4, 53456, 456]
# while some_int < len(list):
#     print("Hello")
#     print(some_int)
#     some_int += 1
#
# list_of_value = 'a n m  43 jk'.split()
#
# list_value2 = (1, 5, 4, 3, 2)
# new_dict = zip(list_of_value, list_value2)
#
# print(dict(new_dict))
#
# asd = {'name': "Jonh", "surname": "Smith"}
#
# print([asd.items()])
# # sorted -> list
# list = [('name', 'Jonh'), ('surname', 'Smith')]
# #
print(bool('')) #False = 0
print(bool(tuple()))
print(bool([]))
print(bool(dict()))
print(bool(set()))
print(int(False))
print(int(True))
print(bool(None))

def aasd(some_bool: bool):
    if not some_bool:
        return "" , 25

print(aasd(False))


def new_method(firts_item: int, second_item: int) -> int:

    result  = (firts_item * 2)  + (second_item * 2)

    print(result)
    return result


new_method(1, 2 )
