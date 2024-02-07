import argparse
from utils.audio_extraction.extractor import extract_audio, separate_vocals_and_accompaniment
from utils.speech_recognition.recognizer import transcribe_audio
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='LangFlip Video Translation Command-Line Tool')
    parser.add_argument('--file', type=str, required=True, help='Location of the video file to translate')
    parser.add_argument('--from-lang', dest='from_lang', type=str, required=True, help='Original language of the video')
    parser.add_argument('--to-lang', dest='to_lang', type=str, required=True, help='Target language for translation')

    args = parser.parse_args()

    try:
        audio_path = extract_audio(args.file)
        print(f"Audio extracted to {audio_path}")
        separate_vocals_and_accompaniment(audio_path)

        current_script_path = Path(__file__).parent.absolute()
        transcribe_audio(current_script_path.joinpath('./../data_management/vocals.wav'))
        # print(f"Translating video from {args.from_lang} to {args.to_lang} is not yet implemented.")
    except Exception as e:
        print(f"Error during audio extraction: {e}")

if __name__ == "__main__":
    main()
