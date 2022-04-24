# pip install qrcode

import qrcode

url = 'https://www.python.org/'

img = qrcode.make(url)

img.save('qrcodepython.png')
