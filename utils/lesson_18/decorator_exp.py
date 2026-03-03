from utils.lesson_18.decorator_retry import retry


def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

def say_hello():
    print("Hello")



def_func = decorator(say_hello)


# print(def_func())

@decorator
def say_hello2():
    print("Hello")
    raise ValueError


say_hello2()