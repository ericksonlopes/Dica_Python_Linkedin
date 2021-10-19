file = open('arquivo.txt', 'rt')
data = file.read()
palavras = data.split()

print(f"Seu arquivo tem {len(palavras)} palavras.")
# Seu arquivo tem 15 palavras.
