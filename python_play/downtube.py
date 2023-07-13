# pip install pytube
import os
from pytube import YouTube, Playlist

full_path = os.path.abspath(".")
playlist_url = input("Enter the playlist link: ")

playlist = Playlist(playlist_url)
path = os.path.join(full_path, playlist.title)

if not os.path.isdir(path): os.mkdir(path)

# Dive into the playlist
for url in playlist:
    try:
        video = YouTube(url)
        print(f"[+] Downloading: {video.title} ...")
        # Check whether the file already exists
        video_path = os.path.join(path, f"{video.title}.mp4")
        if os.path.isfile(video_path):
            print("Video already exists. Skipping ...")
            continue
        # Download the video
        stream = video.streams.get_highest_resolution()
        stream.download(output_path=path)
        print("[+] Downloaded successfully!")
    
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")

## [NB] Age restriction issue