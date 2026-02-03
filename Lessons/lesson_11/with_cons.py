# try:
#     file = open("example.txt", "w")
#
#     content = file.read()
# except Exception as e:  # Вловлювання помилки та збереження її у змінну e
#     print(f"Виникла помилка: {e}")
# finally:
#     if file is not None:
#         file.close()



# try:
#     with open("D:\work\Hillel_19_12\lesson_11\example.txt=example.txt", "w") as file:
#         file.write("Hello World")
#
#
# except FileNotFoundError:
#     print('Wrong path')

# rasise FileNotFoundError
#
# else:
#
#     with open("example.txt", "r") as file:
#         file = file.read()
#
#
# finally:
#     print(file)

with open("example.txt", "r") as file_:
            file = file_.read()
            # file = file_.read()
            print(file)

# class some with
# entre_to class -> some fucn() ->  open("example.txt", "r")
#body pass
# exit class -> some fucn() ->  if file is not None:
# #         file.close()