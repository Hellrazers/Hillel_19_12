import re


text_1 = '''In this log file, we can see that user Tom logged in at 09:00. After an hour, Tom updated his profile settings. Finally, Tom logged out.'''
regex_1 = r'\b[Tt]om\b'


text_2 = '''
text 123 USD 
text 345 usd 
text 3453 in usd
text 3453 or usd
text 34253 an usd
'''



regex_2 = r'\b(\d{,4})\s(?:[A-za-z]{2})?\s?(usd|USD)'


text_3 = '''In this log file, we can see that user Tom logged (096) 123 12 12 in at 09:00. After an hour, Tom updated his profile settings. Finally, Tom logged out.'''
regex_3 = r'\(0\d{2}\)(?:\s|-)\d{3}(?:(?:\s|-)\d{2}){2}'

str_4 = 'use123r@example.com'
regex_4 = r'[A-z\d._]{1,}@(example|google)\.(com)'


# str_after_regex = re.findall(regex_4, str_4)
# print(str_after_regex)
# print(re.search(regex_4, str_4))
# for item in re.finditer(regex_4, str_4):
#     print(item.group())


print(re.findall(regex_4, str_4))
print(re.match(regex_4, str_4))
print(re.fullmatch(regex_4, str_4))


# for item in re.finditer(regex_2, text_2):
#
#     regex_tuple_group = item.groups()
#     print(len(regex_tuple_group))
#     print(item.group() + ' - regex with match')
#     print(f'{regex_tuple_group[0]} {regex_tuple_group[1]} - regex in group')



# rz-product-tile