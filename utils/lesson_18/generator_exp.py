def func():
    yield 1
    yield 2
    yield 3


values_generator = func()
# print(next(values_generator))
# print(next(values_generator))




def preparing():
    print("starting test_preparing")

    yield

    print("Finishing test_preparing")
    yield

test_preparing = preparing()
next(test_preparing)

print(" TEST BODY ")

next(test_preparing)

#цього робити не можна
def generator2():
    return 2
    yield 1


def generator():
    yield [(1,2)], 123, None, True
    return [(1,2)], 123, None, True

generator = generator()
print(next(generator))
try:
    next(generator)
except StopIteration as e:
    print(e.value)
