from pytube import YouTube
from sys import argv

# link = argv[1]
link = 'https://www.youtube.com/watch?v=vEQ8CXFWLZU&list=WL&index=2&t=20s'
yt = YouTube(link)

print("Title :", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_lowest_resolution()

yd.download('D:\Python Projects\YoutubeDownloader')