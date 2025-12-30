row = "перевірка, чи рядок складається тільки з великих літер:"
# row_upper_case = row.upper()
# print(row_upper_case)
# row_lower_case = row.lower()
# print(row_lower_case)
#
# print(row.title())
# row_with_capitalize = row.capitalize()
# print(row_with_capitalize)
#
# print(row_upper_case.isupper())
# print(row_lower_case.islower())
# print(row.title().istitle())
row = '110 USDT' # 110 usdt 110 Usdt
row_upper_case = row.lower()
if row_upper_case.endswith('usdt'):
    print(row_upper_case)


name_surname = "olskise Malk"

name_surname_upper_case = name_surname.title()
print(name_surname_upper_case == name_surname)