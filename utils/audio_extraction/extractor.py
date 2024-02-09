import subprocess
from spleeter.separator import Separator
import os

current_script_path = os.path.dirname(os.path.abspath(__file__))

def extract_audio(video_path):
    """Extracts the audio track from the video file."""
    audio_output =  os.path.join(current_script_path, '..', '..', 'data_management', 'video.wav')
    command = ['ffmpeg', '-i', video_path, '-vn', '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2', audio_output]
    subprocess.run(command, check=True)
    return audio_output

def separate_vocals_and_accompaniment(audio_path):
    """Separates vocals and accompaniment using Spleeter."""
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(audio_path, os.path.join(current_script_path, '..', '..', 'data_management'), codec='wav', filename_format="{instrument}.{codec}")
