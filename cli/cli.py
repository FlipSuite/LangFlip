import argparse
from main import start_translation

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
            start_translation()
        except Exception as e:
            print(f"Error during audio extraction: {e}")

    elif args.command == 'other':
        print("Coming soon")

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
