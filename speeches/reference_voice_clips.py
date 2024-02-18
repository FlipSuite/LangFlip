import subprocess
import os
import glob

def generate_reference_voice_clips(vocals_path):
  output_dir = vocals_path.replace("video_vocals.wav", "reference_voice_clips/")
  os.makedirs(output_dir, exist_ok=True)

  # Base command for FFmpeg to split the file into 10-second clips and convert them
  ffmpeg_cmd_base = [
      'ffmpeg', '-i', vocals_path, '-f', 'segment', '-segment_time', '10',
      '-ar', '22050', '-acodec', 'pcm_f32le', '-y'
  ]

  output_file_path = os.path.join(output_dir, 'segment_%03d.wav')
  ffmpeg_cmd = ffmpeg_cmd_base + [output_file_path]

  subprocess.run(ffmpeg_cmd, check=True)

  # Get the list of file paths
  file_paths = glob.glob(os.path.join(output_dir, '*.wav'))

  return file_paths
