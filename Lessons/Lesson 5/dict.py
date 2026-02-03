# null false true
# None False True
str_123 = 1 + 3
my_dict = {
    "id": 1,
    3+ 4: "asd",
    str_123: 123,
    "name": "John",
    "surname": "Doe",
    "age": 30,
    "city": "New York",
    False: 123,
    None: 123,
    (1,): 45,
    "new_dict": {
        "key": "value",
        "id": 23,
        123: 34556,
        "ids": [1, 2, 3]
    },
    "new": [
        {
            "key": "value", "id": 454,"name": "asd" },
        {
            "key": 1123
        }

    ]
    # [1, 2] : 'asd'
}
# print(my_dict[7])
# my_dict["new value"] = "new value"
# print(my_dict)
# my_dict.setdefault('new value2')
# print(my_dict)

# for k123, v234 in my_dict.items():
#     print(f'key: {k123}, value: {v234}')
#
# for value in my_dict.keys():
#     print(value)

# print(my_dict.pop('age'))
# print(my_dict)

my_dict1 = {"key": 1, "value": 2}
my_dict2 = {"id": 5, "value": 4}
my_dict3 = my_dict1 | my_dict2
my_dict1.update(my_dict2)
print(my_dict3)
print(my_dict1)


# first_step_of_dict = my_dict['new_dict']
# print(first_step_of_dict)
# print(first_step_of_dict.get('ids')[-1])
#
# first_step_of_dict2 = my_dict['new']
# print(first_step_of_dict2[0]['key'])












# print(hash((1, 3)))
# print(my_dict[False])
# print(hash(True))
#
# print(hash(False))
#
# print(hash(None))
# print(hash([1, 3]))
# str_123 = 'Aa'
# print(hash('Aa'))
# print(hash(str_123))

# print(str_123 == 'Aa')
# print(my_dict)
# print(my_dict["age"])
# strt = my_dict.get('name1', True)
# print(strt)

# assert strt == True