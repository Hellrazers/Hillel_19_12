row = ('Методи .startswith() та .endswith() використовуються для перевірки того,'
       ' чи рядок починається або закінчується певною підстрічкою.')

# print(type(row))
# start_1 = row.startswith('м') # False
# print(start_1)
# start_2 = row.startswith('Методи .') # True
# print(start_2)
# start_3 = row.startswith('М') # True
# print(start_3)

link = 'https://lms.ithillel.ua/'
link_2 = 'https://lms.ithillel.ua/api/v1/users?id=1'
boool_of_links = link_2.startswith(link)
print(boool_of_links)

if boool_of_links:
    print("evrything okay ")
else:
    print("Mr. we have a problem")
# end_1 = row.endswith('підстрічкою') #false
# end_2 = row.endswith('.') #TRUE
# end_3 = row.endswith('підстрічкою.') #True
# print(end_1)
# print(end_2)
# print(end_3)