import argparse
from modules.transcriptions.src.extractor import extract_audio
from modules.transcriptions.src.recognizer import transcribe_audio
from modules.transcriptions.src.translator import translate
import os
import torch
# from tortoise.api import TextToSpeech

def main():
    parser = argparse.ArgumentParser(description='LangFlip Video Translation Command-Line Tool')
    parser.add_argument('--file', type=str, required=True, help='Location of the video file to translate')
    parser.add_argument('--from-lang', dest='from_lang', type=str, required=True, help='Original language of the video')
    parser.add_argument('--to-lang', dest='to_lang', type=str, required=True, help='Target language for translation')

    args = parser.parse_args()

    try:
        current_script_path = os.path.dirname(os.path.abspath(__file__))
        video_path = os.path.join(current_script_path, '..', 'video.mp4')
        audio_path = extract_audio(video_path)
        print(f"Audio extracted to {audio_path}")
        # separate_vocals_and_accompaniment(audio_path)

        # transcription = transcribe_audio(os.path.join(current_script_path, '..', 'data_management', 'vocals.wav'))
        # translate(from_code=args.from_lang,to_code=args.to_lang,text=transcription)
        # print(f"Translating video from {args.from_lang} to {args.to_lang} is not yet implemented.")

        # tts = TextToSpeech()  # Replace "your_model_name_here" with the model you intend to use

        # text = "Hello, this is a test string for Tortoise TTS."

        # # Generating speech
        # with torch.no_grad():
        #     audio = tts.tts(text)

        # # Saving the generated audio to a file
        # audio.save("output_audio.wav")
    except Exception as e:
        print(f"Error during audio extraction: {e}")

if __name__ == "__main__":
    main()
