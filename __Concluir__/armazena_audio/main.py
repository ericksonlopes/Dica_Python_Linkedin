from gtts import gTTS
from playsound import playsound

audio = "voz.mp3"
language = 'pt-br'

sp = gTTS(text="Sou programador em python", lang=language, slow=False)

sp.save(audio)
playsound(audio)