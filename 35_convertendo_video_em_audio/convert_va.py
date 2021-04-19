# instalar biblioteca
# pip install moviepy

import moviepy.editor

# Passe o local
video = moviepy.editor.VideoFileClip('video.mp4')

audio_video = video.audio

audio_video.write_audiofile('audio.mp3')