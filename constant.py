import pathlib
from pathlib import Path

BASE_DIR: Path = pathlib.Path(__file__).parent
BASE_DIR_2: Path = pathlib.Path().cwd()
DATA_FOR_TEST_DIR: Path = BASE_DIR / "data_for_tests"
DATA_FOR_TEST_HELLO_WORD_DIR = DATA_FOR_TEST_DIR / "hello_world"
DATA_FOR_TEST_REQUEST_DIR = DATA_FOR_TEST_DIR / "requst_model"
# DATA_FOR_WINDOWS  = r"D:\work\Hillel_19_12\data_for_tests\hello_word\new_file.txt {BASE_DIR} \n asdasd"
# DATA_FOR_WINDOWS_not_row  = "D:\work\Hillel_19_12\data_for_tests\hello_word\\new_file.txt {BASE_DIR} \\n asdasd"
# print(DATA_FOR_WINDOWS)
# print(DATA_FOR_WINDOWS_not_row)