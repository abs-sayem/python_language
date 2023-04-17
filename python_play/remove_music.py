from moviepy.editor import VideoFileClip
from tkinter.filedialog import *

def convert_to_mp3(video_file):
    demo_file = VideoFileClip(video_file)
    audio_file = demo_file.audio
    audio_file.write_audiofile(f"new_file.mp3")

def remove_bgmusic_from_audio(audio_file):
    from moviepy.editor import AudioFileClip

    # Remove background music
    print("\n[INFO] Removing audio...")
    final_audio_file = AudioFileClip(audio_file).without_audio()

    # Export merged audio file
    print("\n[INFO] Writing final video file...")
    final_audio_file.write_audiofile("bgmusic_removed_audio.mp3")
    # # Return the video file
    # return(final_video_file)

def remove_bgmusic_from_video(video_file):
    import moviepy
    from moviepy.editor import VideoFileClip

    # Remove background music
    print("\n[INFO] Removing audio...")
    final_video_file = VideoFileClip(video_file).without_audio()

    # Export merged audio file
    print("\n[INFO] Writing final video file...")
    final_video_file.write_videofile("bgmusic_removed_video.mp4")
    # # Return the video file
    # return(final_video_file)

def only_vocals(music_file):
    # install spleeter - <pip install spleeter>
    from spleeter.separator import Separator
    from tensorflow import signal
    seperator = Separator()
    seperator.separate(music_file)

# Read the file
#file = askopenfilename()
only_vocals("new_file.mp3")
#remove_bgmusic_from_video(video_file)