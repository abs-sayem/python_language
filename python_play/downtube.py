import pytube

# Give the url of the video
url = input("Give the url: ")
print("Downloading....")

# Specify the stroge of the video
path = "C:/Users/AbsSayem/Downloads/downtube/"

# Download the video
pytube.YouTube(url).streams.get_highest_resolution().download(path)