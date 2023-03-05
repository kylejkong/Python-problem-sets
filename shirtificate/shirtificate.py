from fpdf import FPDF
import random

core_fonts = [
            "Courier",
            "Helvetica",
            "Arial",
            "Times",
            # "Symbol",
            # "ZapfDingbats"
            ]
font_styles = [
    "B","I","U",
    "BI",
    "BU",
    "IU"
]


class PDF(FPDF):
    def __init__(self, name):

        super().__init__()

        # self._pdf = FPDF()

        self.add_page( format="A4")
        # n = random.choice(core_fonts)
        # print(n)
        # m = random.choice(font_styles)
        # print(m)
        self.set_font(random.choice(core_fonts), random.choice(font_styles), random.randint(40,60))
        self.cell(0,30, "CS50 Shirtificate",new_x="LMARGIN", new_y="NEXT", align="C")
        self.image("shirtificate.png", w=self.epw) #w=pdf.epw makes the image full width
        self.set_text_color(255,255,255)
        self.set_font(random.choice(core_fonts), random.choice(font_styles), 35)
        self.set_xy(55,85)
        self.cell(w = 100, h =35 , txt =f"{name} took CS50", border=0, align="C")









name = input("Name: ")
pdf = PDF(name)
pdf.output("shirtificate.pdf")







