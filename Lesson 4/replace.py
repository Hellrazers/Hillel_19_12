row = "Метод .replace() використовується Для заміни входжень певної підстрічки іншою підстрічкою в для рядку. Ось приклад використання:"
print(row.count('asdasd'))
row_1 = '1, two, 1, thour'
print(row_1.replace('1', 'one'))
print(row_1.replace('1', 'one', 1)
      .replace('1', 'three'))


row_2 = row_1.replace('1', 'one', 1) # 'one, two, 1, thour'
print(row_2)
row_3 = row_2.replace('1', 'three', )
print(row_3)


row_4 = row.lower().replace('для', 'вже').title()
print(row_4)
row_4 = row.replace('для', 'вже').replace('Для', 'Вже').startswith('Метод')
print(row_4)