# Instalar biblioteca
# pip install pytube

from pytube import YouTube

# link do video que sera baixado
link = 'https://youtu.be/pHEz5jGqaW4'

# Criando obj com o link
video = YouTube(link)

# especifica que será feito o download da mais alta qualidade disponível.
stream = video.streams.get_highest_resolution()

# Realiza o download, e salva dentro da pasta 'videos'
stream.download(output_path='videos')
