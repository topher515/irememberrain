from __future__ import print_function
from pytube import YouTube
from time import time


def to_kb(bytes_int):
    return "%skb" % (bytes_int / 1024)

def main():

    yt = YouTube('https://www.youtube.com/watch?v=BOa0zQBRs_M')
    stream = yt.streams.filter(res='1080p').first()
    bytes_total = stream.filesize

    last_time = None

    def on_progress(stream, chunk, file_handle, bytes_remaining):
        if last_time != int(time()):
            print(
                'Downloading (%s/%s): %d%%' % (to_kb(bytes_total-bytes_remaining), to_kb(bytes_total), (bytes_total - bytes_remaining)/bytes_total * 100),
                end='\r'
            )

    yt.register_on_progress_callback(on_progress)
    
    stream.download(filename='rainwalk')

if __name__ == '__main__':
    main()