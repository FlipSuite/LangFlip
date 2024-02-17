from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import requests
import shutil
from urllib.parse import urlparse, unquote
import os


def autoalign(video_path, captions, instrumental_audio_path, root_path):
    """
    Aligns audio clips with video based on captions, then overlays an instrumental audio.
    Parameters:
    - base_id: Identifier for the base video.
    - video_data: Dictionary containing video metadata, including 'originalVideoUrl'.
    - video_file_path: Path to the video file.
    - captions: List of caption dictionaries, each containing 'begin', 'lark_record_id', and other metadata.
    - instrumental_audio_path: Path to the instrumental audio file to overlay.
    """

    # Load video
    video = VideoFileClip(video_path)

    audio_clips = []
    for caption in captions:
        audio_clip_path = caption["audio_clip_path"]
        # Here you would have your logic to obtain the audio clip file, replacing the Google Cloud Storage part
        # For the purpose of this example, it's assumed the files are already in ../tmp/

        audio_clip = AudioFileClip(audio_clip_path).set_start(caption["begin"])
        audio_clips.append(audio_clip)

    # Load the instrumental audio file
    instrumental_audio = AudioFileClip(instrumental_audio_path)

    # Combine audio clips with instrumental
    final_audio = CompositeAudioClip(audio_clips)
    combined_audio = CompositeAudioClip([final_audio, instrumental_audio])

    # Set the combined audio to the video
    video.audio = combined_audio

    # Export the video with the new audio
    video_output_path = video_path.replace("video.mp4", "video_translated.mp4")
    temp_path = os.path.join(root_path, "data_management", "temp-audio.mp3")
    video.write_videofile(
        video_output_path, temp_audiofile=temp_path, verbose=False
    )

    print(f"Video has been processed and saved to {video_output_path}")
    return video_output_path
