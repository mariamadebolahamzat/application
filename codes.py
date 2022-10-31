from pytube import Playlist
p = Playlist('playlist link here')

print(f'Downloading: {p.title}')

for video in p.videos:
    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download()
    #video.streams.first().download()
