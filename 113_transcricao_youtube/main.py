# pip install youtube-transcript-api

from youtube_transcript_api import YouTubeTranscriptApi

video_id = "n70e_0ewXzI"  # ID do vídeo no YouTube
transcricao = YouTubeTranscriptApi().fetch(video_id=video_id, languages=["pt"])

for trecho in transcricao:
    print(trecho)
    # FetchedTranscriptSnippet(text='começo do video', start=0, duration=6)

    print(trecho.text)
    # começo do video