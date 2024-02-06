# LangFlip: Advanced Video Translation System

## Overview

LangFlip stands at the forefront of video translation technology, designed to automate and refine the process of translating spoken content in videos into various languages. This project leverages cutting-edge AI models and custom algorithms to transcribe, translate, and dub video content, aiming to deliver a seamless viewing experience in multiple languages with accurate subtitles and natural-sounding dubbed audio.

## Core Features

- **Automated Speech Recognition (ASR)**: Utilizes the Whisper API for extracting and transcribing spoken content from videos with high accuracy, catering to diverse accents and dialects.
- **Translation Engine**: Integrates with the LibreTranslate API for translating transcribed text into multiple target languages, emphasizing contextual accuracy and nuance preservation.
- **Dubbing and Subtitling**: Employs a combination of TTS (Text-to-Speech) technologies, including the OpenVoice API, for generating natural-sounding voiceovers in the target language, alongside generating synchronized subtitles.

## License

This project is licensed under the GNU General Public License (GPL), version 3. For more details, see the `LICENSE` file in the root directory of this source code or visit [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).

The GPL license ensures that the software and all derived works are free and open-source. It guarantees that users have the freedom to run, study, share, and modify the software.

## Technical Deep Dive

### Video Processing Workflow

1. **Preprocessing**: Analyze and preprocess video input to optimize for speech extraction, including noise reduction and audio normalization.
2. **Speech Recognition**: Deploy the Whisper model to transcribe audio tracks to text, segmenting speech by timestamps to align with video frames.
3. **Translation**: Process transcribed text through LibreTranslate, applying natural language processing (NLP) techniques to maintain context and idiomatic expressions across languages.
4. **Dubbing/Subtitles Generation**: For dubbing, text is fed into the OpenVoice API to produce voiceovers matched with the video's original speech timing. For subtitles, the translated text is formatted and time-synced with the video playback.

### Architecture Considerations

- **Modular Design**: Structured to support plug-and-play functionality for different ASR, translation, and TTS services, allowing easy integration of alternative technologies.
- **Scalability**: Designed to efficiently handle video files of varying sizes and lengths, from short clips to full-length films, through optimized processing pipelines.
- **Quality Assurance**: Incorporates automated and manual quality checks to ensure translation accuracy, proper timing of subtitles, and naturalness of dubbed audio.

## Getting Started

### Prerequisites

- Docker or Python 3.8+
- FFmpeg for video processing
- Access tokens for Whisper, LibreTranslate, and OpenVoice APIs

### Installation

```bash
git clone https://github.com/FlipSuite/LangFlip.git
cd LangFlip
pip install -r requirements.txt
