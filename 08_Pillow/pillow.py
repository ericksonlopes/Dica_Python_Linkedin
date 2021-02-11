# Importando módulo utilizado
from PIL import Image

# Especificamos o arquivo, que esta na pasta raiz do projeto
file = 'imagem.jpg'

# Instanciamos o módulo Image.open() para carregar a imagem
img = Image.open(file)

# Rotacionando imagem em 45 graus
img_rotate = img.rotate(45)

# Exibindo imagem rotacionada usando um visualizador externo
img_rotate.show(file)

# Salvando imagem na pasta raiz do projeto
img_rotate.save(f'new_{file}')
