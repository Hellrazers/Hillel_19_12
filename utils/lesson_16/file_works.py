from constant import DATA_FOR_TEST_DIR

# with open(DATA_FOR_TEST_DIR/ 'example.txt', 'w') as file:
#     file.write("content")
#
#
#
# with open(DATA_FOR_TEST_DIR/ 'example.txt', 'a') as file:
#     file.write('\nNew Line')
#     # print(file.read())
#
#
# with open(DATA_FOR_TEST_DIR/ 'example.txt') as f:
#     content = f.read()
#     # print(content)


lines_to_write = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]


with open(DATA_FOR_TEST_DIR/ 'example2.txt', 'w') as file:
    file.writelines(['first ', 'second ', 'third '])


# with open(DATA_FOR_TEST_DIR/ 'example2.txt', 'a') as file:
#     file.write('\nNew Line')
#     # print(file.read())


with open(DATA_FOR_TEST_DIR/ 'example2.txt') as f:
    content = f.readlines()
    print(content)


# file.open()
# pass.........content = f.read()
# file.close()
# print(content)

# f.read()

