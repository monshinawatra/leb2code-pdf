from fpdf import FPDF
from PIL import Image


class PDFMaker(FPDF):
    def __init__(
        self,
        orientation="P",
        unit="mm",
        size="A4",
        name: str = "",
        number: str = "",
    ):
        super().__init__(
            orientation=orientation,
            unit=unit,
            format=size,
        )
        self.add_page()
        self.add_font(family="THSarabun", fname="font/THSarabun.ttf", uni=True)
        if len(name):
            self.set_font("THSarabun", size=28)
            self.cell(w=0, txt=name, align="C")
            self.ln(12)
            self.set_font("helvetica", size=16)
            self.cell(w=0, txt=number, align="C")
            self.ln(25)

        self.set_font("THSarabun", size=18)

    def save_pdf(self, path: str = "demo.pdf"):
        self.output(path)

    def write_image(self, image: Image, output: Image = None, label: str = ""):
        self.add_page()
        self.cell(60, 10, label, align="L")
        self.ln()
        self.image(image, w=self.epw)
        if output != None:
            self.image(output, w=self.epw / 2)
