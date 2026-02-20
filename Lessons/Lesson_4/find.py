string = "Це приклад для пошуку приклад у рядку."

# print(string.find('приклад')) #число
# print(string.find('Це')) #число
# print(type(string.find('приклад')))
# print(string.find('asdsada'))

str_to_seacrch = 'приклад'
len_str_to_seacrch = len(str_to_seacrch)

str_index_value = string.find(str_to_seacrch)
print(str_index_value)
total_index_value = len(string)



# для пошуку приклад у рядку.
string_2 = string[str_index_value + len_str_to_seacrch:].find(str_to_seacrch)
print(string_2)

string_3 = string[:str_index_value]
print(string_3)

total_value_beetween_str_search_and_len_word =  str_index_value + len_str_to_seacrch
print('Total value приклад' ,total_value_beetween_str_search_and_len_word)

#find (що ми хочемо знати, з відки , до якого місця ми будемо шукати )
value_2 = string.find('приклад', 10, 15)

print("Index value 2 :", value_2)
print(string[value_2])


link = 'https://lms.ithillel.ua/'
link_2 = 'www:https://lms.ithillel.ua/api/v1/users?id=1'
print(link_2.find('v1/users?'))