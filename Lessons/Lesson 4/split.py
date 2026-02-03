row = ('Функція split()+використовується для розділення рядка на частини на основі певного роздільника та повертає список отриманих'
       ' частин. Основні варіанти використання split():Функція 1 23 2435 +5 ')


row = '1 two 1 4'
row_after_split = row.split(maxsplit=1, sep=' ')
print(row_after_split)
print(row_after_split[1])
print(len(row_after_split))
# print(type(row))
# sp_list = row.split()
# print(*sp_list, sep='+')
# print(type(sp_list))
# print('Довжина def splita ', len(sp_list))
# sp_list = row.split('split() ')
# print(*sp_list, sep='\n')
# print('Довжина ', len(sp_list))
# sp_list = row.split('Функція')
# print(*sp_list, sep='\n')
# print('Довжина ', len(sp_list))
# print('3 елемент в масиві: ',sp_list[2])
# import re
# рядок = "apple1 orange2,banana3"
# частини = re.split(r'\d', рядок)
# print(частини)