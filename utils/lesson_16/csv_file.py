import csv
from constant import DATA_FOR_TEST_DIR



data = [
    ['where_is_from', 'Name', 'Age', 'is_married', 'City'],
    ['UA','John', 30, 'yes', 'New York'],
    ['FI','Alice', 25,  'yes', 'Los Angeles'],
    ['PL', 'Bob', 35, 'no', 'Chicago']
]


print(data[-1][1])

headers = data[0] # ['Name', 'Age', 'is_married', 'City']
list_data = data[1:] #     [['John', 30, 'yes', 'New York'], ['Alice', 25,  'yes', 'Los Angeles'],['Bob', 35, 'no', 'Chicago']]

list_data_dict = [dict(zip(headers, element)) for element in list_data]
list_data_dict_2 = [tuple(zip(headers, element)) for element in list_data]
# print(list_data_dict_2)
# print(list_data_dict)


list_data_for_zip = []
for row in list_data:
    print(headers,row)
    list_data_for_zip.append(dict(zip(headers, row)))
print(list_data_for_zip)
print(list_data_for_zip[-1].get('Name'))

#
# with open(DATA_FOR_TEST_DIR/'csv_test.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(data)
#
#


