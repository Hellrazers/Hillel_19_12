# raise ValueError('Value error  123')
# raise PermissionError('Permission error')


# def is_older(age):
#     if 18 < age < 60 :
#         return True
#     elif age == 0:
#         raise ValueError('Your age connot be 0')
#     else:
#         raise TypeError(f'Not valid age: {age}')
#
#
#
# # print(is_older(18))
# # print(is_older(45))
# try:
#     is_older = is_older(14)
# except (ValueError, PermissionError) as e:
#     print(e)
#
#
# 
#
