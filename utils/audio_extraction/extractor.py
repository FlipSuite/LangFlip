import subprocess
from spleeter.separator import Separator
from pathlib import Path

def extract_audio(video_path):
    """Extracts the audio track from the video file."""
    audio_output = video_path.rsplit('.', 1)[0] + '.wav'
    command = ['ffmpeg', '-i', video_path, '-vn', '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2', audio_output]
    subprocess.run(command, check=True)
    return audio_output

def separate_vocals_and_accompaniment(audio_path):
    current_script_path = Path(__file__).parent.absolute()
    """Separates vocals and accompaniment using Spleeter."""
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(audio_path, current_script_path.joinpath('./../../data_management'), codec='wav', filename_format="{instrument}.{codec}")
