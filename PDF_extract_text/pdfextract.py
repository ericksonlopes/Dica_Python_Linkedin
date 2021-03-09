import PyPDF2
pdf_obj = open('documento.pdf')
pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
pageobj = pdf_reader.getPage(0)
print(pageobj.extractText())