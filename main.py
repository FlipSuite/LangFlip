import os
import sys

from transcriptions.extractor import extract_audio, separate_vocals_and_accompaniment
from transcriptions.recognizer import transcribe_audio, group_until_silence
from transcriptions.translator import translate

from speeches.reference_voice_clips import generate_reference_voice_clips
print("Importing cloned repos")
open_voice_path = os.path.join('speeches', 'OpenVoice')
full_path = os.path.abspath(open_voice_path)

if full_path not in sys.path:
    sys.path.insert(0, full_path)
print("Imported cloned repos")

from speeches.text_to_speech import generate_speech

def start_translation():
  current_script_path = os.path.dirname(os.path.abspath(__file__))
  empty_data_management_folder(current_script_path)

  video_path = os.path.join(current_script_path, 'video.mp4')
  audio_path = extract_audio(video_path, current_script_path)
  print(f"Audio extracted to {audio_path}")

  separate_vocals_and_accompaniment(audio_path)
  print("Audio splitted")

  vocals_path = audio_path.replace("video.wav", "video_vocals.wav")
  transcription = transcribe_audio(vocals_path)
  print("Transcription created")

  grouped_sentences = group_until_silence(transcription["segments"])
  print("Transcription grouped")

  reference_voice_clips = generate_reference_voice_clips(vocals_path)

  for index, sentence in enumerate(grouped_sentences, start=1):
    translated_sentence = translate(from_code="en",to_code="fr",text=sentence["text"])
    print(f"Translated sentence: {translated_sentence}")
    print("Start generating speech")
    generate_speech(translated_sentence, current_script_path, index)
    print(f"Translated sentence: {translated_sentence}")


def empty_data_management_folder(current_script_path):
    folder_path = os.path.join(current_script_path, 'data_management')
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                if filename != '.gitkeep':
                    os.unlink(file_path)
            elif os.path.isdir(file_path):
                for subfilename in os.listdir(file_path):
                    subfile_path = os.path.join(file_path, subfilename)
                    if os.path.isfile(subfile_path) or os.path.islink(subfile_path):
                        if subfilename != '.gitkeep':
                            os.unlink(subfile_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

start_translation()