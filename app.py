import requests
from PIL import Image
from io import BytesIO
from pdf_maker import PDFMaker
from utils import read_code

pdf = PDFMaker(name="ชินวัตร นาไชยธง", number="65090500408")
code_list = read_code(directory="samples")[0]
arguments = {
    "code": code_list.replace("\n", "%0A"),
    "language": "python"
}
response = requests.post("https://carbonnowsh.herokuapp.com/", json=arguments)
response.raise_for_status()
img = Image.open(BytesIO(response.content))
pdf.write_image(img)
pdf.save_pdf("output/demo.pdf")
