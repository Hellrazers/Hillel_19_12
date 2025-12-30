text = "Привіт"

bad = text.encode("utf-8") #перетворити текст → байти
print(bad)

bad_2 = bad.decode("cp1251") #перетворити байти → текст
print(bad_2)

fixed = bad_2.encode("cp1251")
print(fixed)

fixed_2 = fixed.decode("utf-8")
print(fixed_2)
print('------windows-1251--------')
fixed_3 = text.encode("cp1251")
fixed_4 = fixed_3.decode("cp1251")
print(fixed_3)
print(fixed_4)
