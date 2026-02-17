import pathlib
from pathlib import Path

#
# path_to_file = pathlib.Path(__file__).parent
# path_to_dir_where_file = pathlib.Path().cwd()
# print(path_to_file)
# root_dir = pathlib.Path().cwd().parent.parent
# breakpoint()
# LOGIN2 = os.getenv('LOGIN')




from constant import DATA_FOR_TEST_HELLO_WORD_DIR

with open(DATA_FOR_TEST_HELLO_WORD_DIR/'new_file.txt') as file:
    print(file.read())

print(DATA_FOR_TEST_HELLO_WORD_DIR.is_dir())
print(DATA_FOR_TEST_HELLO_WORD_DIR.is_file())
path_to_file = DATA_FOR_TEST_HELLO_WORD_DIR / "new_file.txt"
print(path_to_file)
print(path_to_file.is_file())


parents_dir = DATA_FOR_TEST_HELLO_WORD_DIR/ "parents_dir"/  "parents_dir_1"/ "parents_dir_2"
print(parents_dir)
parents_dir.mkdir(parents=True, exist_ok=True)
