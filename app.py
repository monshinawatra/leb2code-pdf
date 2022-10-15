import requests
from PIL import Image
from io import BytesIO
from pdf_maker import PDFMaker
from utils import read_code
import json
import time
import tqdm
import random

with open("color.json") as file:
    colors = json.load(file)

pdf = PDFMaker(name="ชินวัตร นาไชยธง", number="65090500408")
code_list = read_code(directory="samples", identification="lab")

for page, code in enumerate(tqdm.tqdm(code_list)):
    arguments = {
        "code": code.replace("\n", "%0A"),
        "backgroundColor": colors[random.choice(list(colors))],
        "paddingVertical": "50px",
        "paddingHorizontal": "50px",
        "theme": "Night Owl",
        "language": "python",
        "fontFamily": "Fira Code",
        "fontSize": "16px",
        "lineHeight": "133%",
        "windowControls": True,
        "widthAdjustment": True,
        "lineNumbers": True,
        "firstLineNumber": 1,
        "exportSize": "2x",
        "watermark": False,
        "squaredImage": False,
        "hiddenCharacters": False,
        "name": "",
        "width": 680,
    }

    response = requests.post("https://carbonara-42.herokuapp.com/api/cook", json=arguments)
    response.raise_for_status()
    time.sleep(3)

    img = Image.open(BytesIO(response.content))
    pdf.write_image(img, page=page)


pdf.save_pdf("output/demo_adjust.pdf")
