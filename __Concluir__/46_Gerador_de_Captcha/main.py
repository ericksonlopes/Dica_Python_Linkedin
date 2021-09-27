# Instalar biblioteca
# pip install captcha

from captcha.image import ImageCaptcha

# criar uma instância com o tamanho da imagem
image = ImageCaptcha(width=280, height=90)

# texto para inserir na imagem
txt = "python 369"

# Escrever a imagem no arquivo e salvar
image.write(txt, "Captcha.png")
