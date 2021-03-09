import pyqrcode

url = 'https://www.python.org/'

gene_obj = pyqrcode.create(url)

gene_obj.svg('meu_qrcode', scale=8)