from pytube import YouTube


def filter_name(name):
    name = ''.join(e for e in name if e.isalnum())
    return name + ".mp4"
    

def download_video(link):
    yt = YouTube(link)
    stream = yt.streams.filter(only_audio=True)[0]
    title = filter_name(yt.title)
    stream.download(None, title)
    return title


if __name__ == "__main__":
    download_video("https://www.youtube.com/watch?v=MpybogxYGsI")