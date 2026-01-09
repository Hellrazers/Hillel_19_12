response = [
    {'Name': {
        'id': 0,
        'name': 'anderii',
        'skills': None,
        'age': 32,
        'isPersonWork': True

    }},
    {'Name' : {
        'id': 1,
        'name': 'John',
        'skills':[ 'Python', 'Java'],
        'age': 23,
        'isPersonWork': False

    }},
    {'Name': {
        'id': 2,
        'name': 'Viktor',
        'skills': ['Python', 'Java'],
        'age': 45,
        'isPersonWork': False

    }},
    {'Name': {
        'id': 3,
        'name': 'Den',
        'age': 60,
        'isPersonWork': True

    }},
    {'Name': {
        'id': 4,
        'name': 'Evgen',
        'skills': None,
        'age': 30,
        'isPersonWork':
            {
            'id': 3,
            'name': 'Den',
            'age': 60,
            'isPersonWork': True
            }

    }},
]

# new_list = dict()
# чи людина має 60 років
# чи він працює
#
# # print(len(response))
# for item in response:
#     value_in_dict = item.get('Name')
#     for name, value in value_in_dict.items():
#         print(f"{name}: {value}")

    # print(key)
    # if value_in_dict.get('age') <= 60 and value_in_dict.get('isPersonWork'):
    #     print(f"ID: { {value_in_dict.get('id')}} {value_in_dict.get('name')} йому менше  60 та він працює ")
    # else:
    #     print(f'ID: { {value_in_dict.get('id')}} {value_in_dict.get('name')}')
# list_1 = [1, 2, 3, 4, 5]
# list_2 = []
#break - якщо дохзодить до цього, то воно припиняє цикл
#contionuim - вона каже, якщо дохожить
for e in range(1, 6): # [1 ...4]
    if e == 4:
        break
    for k in range(6, 10): #[6 ...9]
        if e == 2:
            print(e)
            continue
        if k == 9:
            break
        print(f'{e} * {k} = {e * k}')
# else:
#     print('Цикл завершено')
# if json is None:
#     break

# for item in list_1:
#     if item%2 == 0:
#         print(f"This item is correct {item}\n")
#         list_2.append(item)
#     else:
#         print(f"This item is wrong {item}\n")
# print(list_2)


# list_1 = [1, 2, 3, 4, 5] [0, 1 ....5]

#
# for index, value  in enumerate(list_1):
#     if index % 2 == 0:
#         print(value)

