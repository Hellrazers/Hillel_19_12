".py"

import os
from constant import BASE_DIR


for items in os.walk(BASE_DIR):
    path_to_file, list_dir, file_extension = items
    if '.venv' in path_to_file:
        continue

    for py_file in  file_extension:
        if py_file.endswith('.txt'):
            print(f'{path_to_file}\\{py_file}')

