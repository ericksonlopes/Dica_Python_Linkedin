from gtts import gTTS
from playsound import playsound

# Diretorio + Nome do arquivo
audio = "voz.mp3"

# Linguagem em que o texto devera ser dito
language = 'pt-br'

# Texto para ser pronunciado no arquivo .mp3
text = "Sou programador em python"

# criar objeto com as informações passadas
sp = gTTS(text=text, lang=language, slow=False)

# Salvar arquivo
sp.save(audio)

# Ouvir arquivo mp3
playsound(audio)