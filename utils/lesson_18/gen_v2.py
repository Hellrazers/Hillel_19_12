def gen(value: int ):
    for i in range(value):
        yield i

gen_value  = gen(10000)

print(next(gen_value))


def list_values(value: int ):
    list_ = []
    for i in range(value):
        list_.append(i)

    return list_

print(list_values(10000))


print(next(gen_value))
print(next(gen_value))



def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1

# Створюємо генератор
counter = count_up_to(5)


print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
print(next(counter))  # 4
print(next(counter))  # 5
# print(next(counter))

list_comp = [x for x in range(10)]
gen_comp = (x for x in range(10))
print(gen_comp)
print(list_comp)
print(next(gen_comp))