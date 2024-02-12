import whisper_timestamped

def transcribe_audio(audio_path):
    vocals_path = audio_path.replace("video.wav", "video_vocals.wav")
    results = whisper_timestamped.transcribe("tiny", vocals_path)
    
    return results

def group_until_silence(segments):
    # Initialize an empty list to hold the grouped segments
    grouped_segments = []

    # Temporary variable to hold the current group of segments
    current_group = None

    for segment in segments:
        # If there is no current group, start a new one with the current segment
        if current_group is None:
            current_group = {
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            }
        else:
            # Calculate the interval between the current group's end and the current segment's start
            interval = segment['start'] - current_group['end']

            # If the interval is less than or equal to 1.5 seconds, concatenate the current segment's text
            # and update the end to the current segment's end
            if interval <= 0.6:
                current_group['text'] += " " + segment['text']
                current_group['end'] = segment['end']
            else:
                # If the interval is more than 1.5 seconds, add the current group to the list of grouped segments
                grouped_segments.append(current_group)
                # Start a new group with the current segment
                current_group = {
                    "start": segment["start"],
                    "end": segment["end"],
                    "text": segment["text"]
                }

    # Add the last group to the list if it exists
    if current_group:
        grouped_segments.append(current_group)

    return grouped_segments