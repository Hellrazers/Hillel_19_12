import json
from pprint import pprint

from constant import DATA_FOR_TEST_DIR



with open(DATA_FOR_TEST_DIR / 'json_test.json', 'r') as file:
    data:list[dict] = json.load(file)
#
# pprint(data)
# print(type(data))
# print(data[-1].get('name'))

# Виведення зчитаних даних
# print(data)

data_to_json = json.dumps(data, indent=4)
print(type(data_to_json))
print(data_to_json)


with open(DATA_FOR_TEST_DIR / 'json_test2.json', 'w') as file:
    # json.dump(data, file, indent=4)
    file.write(data_to_json)