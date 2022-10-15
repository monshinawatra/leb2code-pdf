from glob import glob1
import re
import os


def read_code(directory: str = ".", identification: str = "lab"):
    files = sorted(glob1(directory, '*.py'))
    code_files = list(filter(lambda x: bool(re.match(identification, x)),
                             files))
    code_texts = []
    for file in code_files:
        with open(os.path.join(directory, file), 'rb') as f:
            code_texts.append(f.read().decode())
    return code_texts
