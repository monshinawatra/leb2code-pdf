from pdf_maker import PDFMaker
from utils import read_code, get_snippet, get_output_text
import json
import tqdm
import argparse

parser = argparse.ArgumentParser(description='make code form to pdf')
parser.add_argument('-n','--name',type=str,help='Enter you full name',required=True)
parser.add_argument('-nid','--number_id',type=int,help='Enter you student id',required=True)
parser.add_argument('-bgc','--backgroundColor',default="Golden Poppy",type=str,help='Enter color name or Hex color code')
parser.add_argument('-t','--theme',default="Night Owl",type=str,help='Enter Color theme')
parser.add_argument('-f','--font',default="Fira Code",type=str,help='Enter font name (See all names in carbon exported config)')
parser.add_argument('-fs','--fontSize',default=16,type=int,help='Enter size of font')
parser.add_argument('-ln','--lineNumbers',default=False,type=bool,help='Turn on/off line number')
parser.add_argument('-w','--width',default=680,type=int,help='Width of code snippets')
parser.add_argument('-d','--directory',default='',type=str,help='Enter code directory')
parser.add_argument('-out','--output_path',default='demo.pdf',type=str,help='Enter path for save pdf')
parser.add_argument('-sn','--select_name',default='lab',type=str,help='Enter file keyword')
args = parser.parse_args()

name = args.name
number_id = args.number_id
backgroundColor = args.backgroundColor
theme = args.theme
fontFamily = args.font
fontSize = args.fontSize
lineNumbers = args.lineNumbers
width = args.width
code_directory = args.directory
output_path = args.output_path
select_name = args.select_name

arguments = {
    "paddingVertical": "50px",
    "paddingHorizontal": "50px",
    "theme": theme,
    "language": "python",
    "fontFamily": fontFamily,
    "fontSize": str(fontSize),
    "lineNumbers": lineNumbers,
    "width": width,
}

if __name__=='__main__':
    pdf = PDFMaker(name=name, number=str(number_id))
    
    files, code_list = read_code(directory=code_directory, identification=select_name)

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
        if backgroundColor[0]=='#':
            colorcode=backgroundColor
        elif backgroundColor in colors:
            colorcode=colors[backgroundColor]
        else:
            colorcode=colors['White']
        arguments["backgroundColor"] = colorcode
        
        arguments["code"] = data_dict[name]["code"]
        arguments["language"] = "python"
        arguments["lineNumbers"] = lineNumbers

        img = get_snippet(arguments)

        arguments["code"] = data_dict[name]["output"]
        arguments["language"] = "plain-text"
        arguments["lineNumbers"] = False
        output_img = get_snippet(arguments)

        pdf.write_image(img, output=output_img, label=name)

    pdf_file=pdf.save_pdf(output_path)
