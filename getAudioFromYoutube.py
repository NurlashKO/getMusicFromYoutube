from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
        'outtmpl': 'music/%(title)s.%(ext)s',
        'format': 'bestaudio/best[height<=480]',
        'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
}

def getAudioFromYoutube(url="https://www.youtube.com/watch?v=ejbmz0yF0wQ"):
    video = "gvsearch1:{url}".format(url=url)
    print(video)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video])
