import pytube
link = "https://www.youtube.com/watch?v=JaO6fPA99Hg"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()

'''
or
from pytube import YouTube
YouTube("https://www.youtube.com/watch?v=opHGwinvsUY").streams.first().download() '''
import os
