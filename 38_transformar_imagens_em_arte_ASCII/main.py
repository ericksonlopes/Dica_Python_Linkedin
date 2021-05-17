from pywhatkit import image_to_ascii_art

# Caminho da imagem
entrada_img = 'python.png'

# Caminho da saida
saida_arquivo_txt = 'ascii_python.txt'

# Esta função cria um arquivo e é possível imprimir a arte
print(image_to_ascii_art(imgpath=entrada_img, output_file=saida_arquivo_txt))
