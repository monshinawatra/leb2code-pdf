from pdf_maker import PDFMaker
from utils import read_code, get_snippet, get_output_text
import json
import tqdm
import random

arguments = {
    "paddingVertical": "50px",
    "paddingHorizontal": "50px",
    "theme": "Night Owl",
    "language": "python",
    "fontFamily": "Fira Code",
    "fontSize": "16px",
    "lineNumbers": True,
    "name": "",
    "width": 680,
}
code_directory = "samples"


pdf = PDFMaker(name="ชินวัตร นาไชยธง", number="65090500408")
files, code_list = read_code(directory=code_directory, identification="lab")

data_dict = {}

with open("color.json") as file:
    colors = json.load(file)
for name, code in zip(files, code_list):
    print(f":: {name}")
    data_dict[name] = {
        "code": code,
        "output": get_output_text(code),
    }

for name in tqdm.tqdm(files):
    arguments["backgroundColor"] = colors[random.choice(list(colors))]

    arguments["code"] = data_dict[name]["code"]
    arguments["language"] = "python"
    arguments["lineNumbers"] = True
    img = get_snippet(arguments)

    arguments["code"] = data_dict[name]["output"]
    arguments["language"] = "plain-text"
    arguments["lineNumbers"] = False
    output_img = get_snippet(arguments)

    pdf.write_image(img, output=output_img, label=name)

pdf.save_pdf("output/demo_adjust.pdf")
