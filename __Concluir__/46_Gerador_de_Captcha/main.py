from captcha.image import ImageCaptcha

image = ImageCaptcha(width=280, height=90)

texto = 'Python 369'

data = image.generate(texto)

image.write(texto, "Captcha.png")
