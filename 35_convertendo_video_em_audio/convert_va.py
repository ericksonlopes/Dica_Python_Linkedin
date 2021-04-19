# instalar biblioteca
# pip install moviepy

import moviepy.editor

# Como parametro, passe a localização do video
video = moviepy.editor.VideoFileClip('video.mp4')

audio_video = video.audio

# Como parametro, passe o local onde sera salvo o audio
audio_video.write_audiofile('audio.mp3')