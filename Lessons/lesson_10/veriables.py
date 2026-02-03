
#глобальна обл видомості
# value = 'Hello word!'
#
#
#
# def hello_world():
#     #локальна обл видомості
#     value = 'Hello'
#
#     def hello():
#         # value = "word!"
#         print(value)
#
#     hello()
#     print(value)
#
#
#
# hello_world()
# print(value)
#


some_value = 5

def func_():
    global some_value
    some_value +=  1

print(some_value)
func_()
print(some_value)
