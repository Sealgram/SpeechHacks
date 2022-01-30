from pytube import YouTube
import sys, os


def filter_name(name):
    name = ''.join(e for e in name if e.isalnum())
    return name + ".mp4"
    

def download_video(link):
    try:
        yt = YouTube(link)
    except:
        print("\nThat is an invalid youtube link.")
        exit(1)
    else:
        stream = yt.streams.filter(only_audio=True)[0]
        title = filter_name(yt.title)
        stream.download(None, title)
        return title


def main():
    args = sys.argv[1:]
    if len(sys.argv) != 2:
        print("Usage: ytmp3.py [YouTube link]")
        exit(1)
    download_video(sys.argv[1])

if __name__ == "__main__":
    main()