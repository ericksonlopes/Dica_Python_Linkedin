import qrcode

url = 'https://www.python.org/'

# converte os dados
img = qrcode.make(url)

img.save('qrcodepython.png')