from pytube import YouTube

link = 'https://youtu.be/pHEz5jGqaW4'

video = YouTube(link)

stream = video.streams.get_highest_resolution()
stream.download()
