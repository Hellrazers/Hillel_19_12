
#
# response = [] #Faslse
# print(f"We did api call and return some obj {response}")
# print('-' * 80)
# # print(bool(response))
#
#
# if response: #true
#     print("Reponse is not empty")
# # elif not None:
# #     print("Response is not NONE")
# else:
#     print("Response is empty")
#
#


{"id": 123, 'name': None } #( None = null )
real_cart_number = None
real_cvv = 123


cart_number = 1234567890123456
cvv = None #Faslse
print('-' * 80)
# print(bool(response))


if cart_number == real_cart_number and cvv == real_cvv: #true   (False) and TRUE  = FALSE
    print("Autrization is Okay")

elif cvv is None : #(True) or (False)  = True
    print("Some value is None CVV NONE")
# elif real_cart_number is None or real_cvv is None: #(True) or (False)  = True
#     print("Some value is None")
elif cart_number != real_cart_number:
        print("cart number is not equal")
elif (cvv is False) and (cart_number is not True):
    print("Some value is empty")
else:
    pass





