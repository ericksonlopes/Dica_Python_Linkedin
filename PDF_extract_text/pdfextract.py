# instalar biblioteca
# pip install pymupdf

import fitz

with fitz.open("documento.pdf") as doc:
    text = ""
    for page in doc:
        text += page.getText()

print(text)
