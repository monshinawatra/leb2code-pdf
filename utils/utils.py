from glob import glob1
import re
import os
import io
import sys
import requests
from PIL import Image
from io import BytesIO
import time
from contextlib import redirect_stdout


def read_code(directory: str = ".", keyword: str = "lab"):
    files = sorted(glob1(directory, "*.py"))
    code_files = list(filter(lambda x: bool(re.match(keyword, x)), files))
    code_texts = []
    for file in code_files:
        with open(os.path.join(directory, file), "rb") as f:
            code_texts.append(f.read().decode())
    return code_files, code_texts


def get_output_text(code: str):
    code = re.sub("(input\(.*)(['\"]\)+)", r"\1\\n\2#__leb2code-pdf", code)
    output_io = io.StringIO()
    output_var = {}
    print(code)
    with redirect_stdout(output_io):
        exec(
            code,
            globals(),
            output_var,
        )
    output_text = list(filter(lambda x: x != "", output_io.getvalue().splitlines()))
    output_var = list(filter(lambda x: type(x) in [str, int, bool, float], output_var.values()))
    var_idx = 0
    # print(output_text)
    # print(output_var)

    for line in code.splitlines():
        if not line.count("__leb2code-pdf"):
            continue
        for idx, output in enumerate(output_text):
            if not line.count(output):
                continue
            output_text[idx] = output + str(output_var[var_idx])
            var_idx += 1
    return "\n".join(output_text)


def request_snippet(
    params: dict, url: str = "https://carbonara-42.herokuapp.com/api/cook", delay: float = 1.5
):
    assert delay > 1.25
    response = requests.post(url, json=params)
    response.raise_for_status()
    img = Image.open(BytesIO(response.content))
    time.sleep(delay)
    return img
