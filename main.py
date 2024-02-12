from modules.transcriptions.src.extractor import extract_audio, separate_vocals_and_accompaniment
from modules.transcriptions.src.recognizer import transcribe_audio
from modules.transcriptions.src.translator import translate
import os
import shutil
import whisper_timestamped

def start_translation():
  current_script_path = os.path.dirname(os.path.abspath(__file__))
  empty_data_management_folder(current_script_path)
  video_path = os.path.join(current_script_path, 'video.mp4')
  audio_path = extract_audio(video_path)
  print(f"Audio extracted to {audio_path}")
  separate_vocals_and_accompaniment(audio_path)
  print("Audio splitted")
  vocals_path = audio_path.replace("video.wav", "video_vocals.wav")
  results = whisper_timestamped.transcribe("tiny", vocals_path)
  print(results)
  # transcription = transcribe_audio(os.path.join(current_script_path, '..', 'data_management', 'video_acco.wav'))
  # translate(from_code=args.from_lang,to_code=args.to_lang,text=transcription)
  # Further processing for translation would go here

def empty_data_management_folder(current_script_path):
    folder_path = os.path.join(current_script_path, 'data_management')
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

start_translation()