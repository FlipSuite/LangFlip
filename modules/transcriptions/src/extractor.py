import subprocess
import os
from audio_separator.separator import Separator

current_script_path = os.path.dirname(os.path.abspath(__file__))

def extract_audio(video_path):
    """Extracts the audio track from the video file."""
    audio_output =  os.path.join(current_script_path, '..', '..', '..', 'data_management', 'video.wav')
    command = ['ffmpeg', '-i', video_path, '-vn', '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2', audio_output]
    subprocess.run(command, check=True)
    return audio_output

def separate_vocals_and_accompaniment(audio_path):
    """Separates vocals and accompaniment using Spleeter."""
    # Initialize the Separator class (with optional configuration properties below)
    separator = Separator(primary_stem_output_path=audio_path.replace("video.wav", "video_accompaniment.wav"), secondary_stem_output_path=audio_path.replace("video.wav", "video_vocals.wav"))

    # Load a machine learning model (if unspecified, defaults to 'UVR-MDX-NET-Inst_HQ_3.onnx')
    separator.load_model()

    # Perform the separation on specific audio files without reloading the model
    primary_stem_output_path, secondary_stem_output_path = separator.separate(audio_path)

    print(f'Primary stem saved at {primary_stem_output_path}')
    print(f'Secondary stem saved at {secondary_stem_output_path}')
    return primary_stem_output_path
