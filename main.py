import os
import sys

from transcriptions.extractor import extract_audio, separate_vocals_and_accompaniment
from transcriptions.recognizer import transcribe_audio, group_until_silence
from transcriptions.translator import translate


from speeches.reference_voice_clips import generate_reference_voice_clips
from speeches.auto_align_vocals import autoalign

print("Importing cloned repos")
open_voice_path = os.path.join("speeches", "OpenVoice")
full_path = os.path.abspath(open_voice_path)

if full_path not in sys.path:
    sys.path.insert(0, full_path)
print("Imported cloned repos")

from speeches.text_to_speech import generate_speech


def start_translation():
    current_script_path = os.path.dirname(os.path.abspath(__file__))
    empty_data_management_folder(current_script_path)

    video_path = os.path.join(current_script_path, "video.mp4")
    audio_path = extract_audio(video_path, current_script_path)
    print(f"Audio extracted to {audio_path}")

    separate_vocals_and_accompaniment(audio_path)
    print("Audio splitted")

    vocals_path = audio_path.replace("video.wav", "video_vocals.wav")
    accompaniment_path = audio_path.replace("video.wav", "video_accompaniment.wav")
    transcription = transcribe_audio(vocals_path)
    print("Transcription created")

    grouped_sentences = group_until_silence(transcription["segments"])
    print("Transcription grouped")

    # reference_voice_clips = generate_reference_voice_clips(vocals_path)
    print("Transcription")
    print(transcription)

    captions = []
    for index, sentence in enumerate(grouped_sentences, start=1):
        print("Translating sentence...")
        print(sentence)
        translated_sentence = translate(
            from_code="fr", to_code="en", text=sentence["text"]
        )
        audio_clip_path = generate_speech(
            translated_sentence, current_script_path, index, vocals_path
        )

        # Assuming `generate_speech` returns the path to the generated audio clip
        # And that each `sentence` has 'start' and 'end' attributes for timing
        captions.append(
            {
                "begin": sentence["start"],  # Start time of the sentence
                "end": sentence["end"],  # End time of the sentence
                "text": translated_sentence,  # The translated text
                "audio_clip_path": audio_clip_path,  # Path to the generated speech audio clip
            }
        )

        # Call to `autoalign`
        autoalign(
            video_path=video_path,
            captions=captions,
            instrumental_audio_path=accompaniment_path,
            root_path=current_script_path
        )
        print("Video alignment and audio overlay complete.")


def empty_data_management_folder(current_script_path):
    folder_path = os.path.join(current_script_path, "data_management")
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                if filename != ".gitkeep":
                    os.unlink(file_path)
            elif os.path.isdir(file_path):
                for subfilename in os.listdir(file_path):
                    subfile_path = os.path.join(file_path, subfilename)
                    if os.path.isfile(subfile_path) or os.path.islink(subfile_path):
                        if subfilename != ".gitkeep":
                            os.unlink(subfile_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s" % (file_path, e))


start_translation()
