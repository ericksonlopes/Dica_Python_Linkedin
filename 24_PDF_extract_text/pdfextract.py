# instalar biblioteca
# pip install pymupdf

import fitz

with fitz.open("docuemnto3.pdf") as doc:
    text = ""
    for page in doc:
        text += page.getText()
        print(page.getText())
# print(text)
