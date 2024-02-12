import argparse
import subprocess
from modules.transcriptions.src.extractor import extract_audio, separate_vocals_and_accompaniment
from modules.transcriptions.src.recognizer import transcribe_audio
from modules.transcriptions.src.translator import translate
import os
import shutil
# from tortoise.api import TextToSpeech

def main():
    parser = argparse.ArgumentParser(prog='langflip', description='LangFlip Video Translation Command-Line Tool')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Parser for the "translate" command
    translate_parser = subparsers.add_parser('translate', help='Translate video files')
    translate_parser.add_argument('--file', type=str, required=True, help='Location of the video file to translate')
    translate_parser.add_argument('--from', dest='from_lang', type=str, required=True, help='Original language of the video')
    translate_parser.add_argument('--to', dest='to_lang', type=str, required=True, help='Target language for translation')

    # Parser for the "ui" command
    ui_parser = subparsers.add_parser('ui', help='Launch the UI for the LangFlip tool')

    args = parser.parse_args()

    if args.command == 'translate':
        try:
            current_script_path = os.path.dirname(os.path.abspath(__file__))
            empty_data_management_folder(current_script_path)
            video_path = os.path.join(current_script_path, '..', 'video.mp4')
            audio_path = extract_audio(video_path)
            print(f"Audio extracted to {audio_path}")
            separate_vocals_and_accompaniment(audio_path)
            print("Audio splitted")
            # transcription = transcribe_audio(os.path.join(current_script_path, '..', 'data_management', 'video_acco.wav'))
            # translate(from_code=args.from_lang,to_code=args.to_lang,text=transcription)
            # Further processing for translation would go here

        except Exception as e:
            print(f"Error during audio extraction: {e}")

    elif args.command == 'ui':
        print(subprocess.run(["flet", "run", "--web", "ui/flet_interface.py"]))

if __name__ == "__main__":
    main()


# print(f"Translating video from {args.from_lang} to {args.to_lang} is not yet implemented.")

# tts = TextToSpeech()  # Replace "your_model_name_here" with the model you intend to use

# text = "Hello, this is a test string for Tortoise TTS."

# # Generating speech
# with torch.no_grad():
#     audio = tts.tts(text)

# # Saving the generated audio to a file
# audio.save("output_audio.wav")
    
def empty_data_management_folder(current_script_path):
    folder_path = os.path.join(current_script_path, '..', 'data_management')
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))