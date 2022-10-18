from utils import read_code, request_snippet, get_output_text
from utils import PDFMaker
import json
import tqdm
from PIL import Image


def get_data_dict(files: list, code_list: list, print_process: bool = True) -> dict:
    """
    Get data as dictionary format

    Args:
        files -> All files name
        code_list -> All code as list of string
        print_process -> Print step between each process

    Return:
        data_dict e.g.
        'lab_1.py' : {
            'code': "print('Hello, world')"
            'output': 'Hello, world'
        }
    """
    data_dict = {}
    for name, code in zip(files, code_list):
        if print_process:
            print(f":: {name}")
        data_dict[name] = {
            "code": code,
            "output": get_output_text(code),
        }
    return data_dict


def get_snippet(
    params: dict, code: str, language: str = "python", line_number: bool = False
) -> Image:
    """
    Get a code snippet from utils.request_snippet

    Args:
        params: -> Parameters to request in api
        code: -> Code as string format
        language: -> Code language 'python' by default and 'plain-text' for output
        line_number: -> Show line number in code snippet

    Return:
        img: -> PIL.image

    """
    params["code"] = code
    params["language"] = language
    params["lineNumbers"] = line_number
    img = request_snippet(params)
    return img


def run_app(params: dict, arguments: dict) -> None:
    """
    Main functions
    """
    LINE_NUMBER = bool(params["lineNumbers"])

    pdf = PDFMaker(name=arguments["name"], number=arguments["id"])
    files, code_list = read_code(directory=arguments["dir"], keyword=arguments["keyword"])
    data_dict = get_data_dict(files=files, code_list=code_list)

    with open("utils/color.json") as file:
        colors_list = json.load(file)
    for name in tqdm.tqdm(files):
        if not params["backgroundColor"].count("#"):
            params["backgroundColor"] = (
                colors_list[params["backgroundColor"]]
                if params["backgroundColor"] in colors_list
                else colors_list["Golden Poppy"]
            )

        img = get_snippet(params, code=data_dict[name]["code"], line_number=LINE_NUMBER)
        output_img = get_snippet(params, code=data_dict[name]["output"], language="plain-text")

        pdf.write_image(image=img, output=output_img, label=name)

    pdf.save_pdf(arguments["save_path"])
