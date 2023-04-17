
# def remove_bgmusic_from_audio(audio_file):
#     from pydub import AudioSegment
#     from pydub.playback import play

#     # Read and get the two mono file from audio
#     sound_stereo = AudioSegment.from_file(audio_file, format=&quot; mp3&quot;)
#     sound_monoL = sound_stereo.split_to_mono()[0]
#     sound_monoR = sound_stereo.split_to_mono()[1]

#     # Invert phase of the Right audio file
#     sound_monoR_inv = sound_monoR.invert_phase()

#     # Merge two L and R_inv files, this cancels out the centers
#     sound_CentersOut = sound_monoL.overlay(sound_monoR_inv)

#     # Export merged audio file
#     fh = sound_CentersOut.export(&quot; audio_without_music.mp3&quot;, format=&quot; mp3&quot;)

def remove_bgmusic_from_video(video_file):
    import moviepy
    from moviepy.editor import VideoFileClip

    # Read the audio file
    video_file = input("video_file_name:")

    # Remove background music
    final_video_file = VideoFileClip(video_file).without_audio()

    # Export merged audio file
    final_video_file.write_videofile(f"new_{video_file}")
    