row = "    Привіт, світ!    "

# row_with_strip = row.strip()
# print(row_with_strip)
# print(len(row_with_strip))
#
# row_with_l_strip = row.lstrip()
# print(row_with_l_strip)
# print(len(row_with_l_strip))
#
row_with_r_strip = row.rstrip()
print(row_with_r_strip)
print(len(row_with_r_strip))


row = "+Привіт, світ!+"
print(row)
print(row.strip('+Привіт'))

row = 'aaaa a b c '
print(row.count('aa'))
