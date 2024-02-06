# LangFlip: Advanced Video Translation System

## Overview

LangFlip stands at the forefront of video translation technology, designed to automate and refine the process of translating spoken content in videos into various languages. This project leverages cutting-edge AI models and custom algorithms to transcribe, translate, and dub video content, aiming to deliver a seamless viewing experience in multiple languages with accurate subtitles and natural-sounding dubbed audio.

## Core Features

- **Automated Speech Recognition (ASR)**: Utilizes the Whisper API for extracting and transcribing spoken content from videos with high accuracy, catering to diverse accents and dialects.
- **Translation Engine**: Integrates with the LibreTranslate API for translating transcribed text into multiple target languages, emphasizing contextual accuracy and nuance preservation.
- **Dubbing and Subtitling**: Employs a combination of TTS (Text-to-Speech) technologies, including the OpenVoice API, for generating natural-sounding voiceovers in the target language, alongside generating synchronized subtitles.
- **Lip-syncing Technology**: Implements advanced deep learning algorithms to analyze and align the facial movements in the video with the new voiceovers, ensuring the speakers' lip movements match the spoken dialogue in the target language. This feature leverages face-alignment and custom lip-sync models to provide a cohesive and immersive viewing experience by minimizing audio-visual discrepancies.

## License

This project is licensed under the GNU General Public License (GPL), version 3. For more details, see the `LICENSE` file in the root directory of this source code or visit [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).

The GPL license ensures that the software and all derived works are free and open-source. It guarantees that users have the freedom to run, study, share, and modify the software.

## Technical Deep Dive

### Video Processing Workflow

**Audio Extraction**: Utilizes the `spleeter` library, a state-of-the-art tool for music and speech separation, to extract clean audio tracks from videos. This separation allows for precise manipulation of speech content without background noise interference, essential for accurate speech recognition and dubbing.

**Speech Recognition**: Implements the `Whisper API` for converting spoken content in the extracted audio into text. Whisper is renowned for its robustness across various languages and dialects, offering high accuracy in transcribing diverse accents and noisy environments.

**Translation**: Leverages the `LibreTranslate API` for translating the transcribed text into multiple target languages. LibreTranslate is chosen for its emphasis on privacy, open-source nature, and support for a wide range of languages, ensuring translations maintain contextual accuracy and cultural nuance.

**Text Processing (Pre-Translation)**: Employs custom Python scripts and natural language processing (NLP) libraries, such as `NLTK` and `spaCy`, for cleaning and preparing the transcribed text for translation. This step includes punctuation normalization, spell checking, and splitting text into manageable segments for more accurate translation.

**Text Processing (Post-Translation)**: Utilizes the same NLP libraries to refine the translated text, ensuring that it aligns with the target language's grammatical rules and stylistic nuances. This process includes adjusting sentence structure, verb tenses, and idiomatic expressions to enhance readability and naturalness in the target language.

**Dubbing**: Engages the `OpenVoice API` for generating natural-sounding voiceovers in the target language. OpenVoice offers a diverse range of voice models, allowing for the selection of voices that best match the original speaker's tone, pitch, and emotion, ensuring a seamless audio-visual experience.

**Subtitles Generation**: Integrates `Subtitle Edit` or similar open-source subtitle creation tools for generating and synchronizing subtitles with the video. This involves timing the translated text with the video's frames, ensuring subtitles appear on-screen in sync with the corresponding spoken dialogue.

**Video Preprocessing**: Uses `ffmpeg` for initial video processing tasks, such as format conversion, resolution adjustment, and extracting raw video streams. This step prepares the video for detailed processing and ensures compatibility with subsequent workflow stages.

**Video Postprocessing**: Combines processed audio tracks with the original video while ensuring lip-sync accuracy using custom deep learning models and the `face-alignment` library. Final adjustments, including color correction and audio normalization, are performed using `ffmpeg`, culminating in a professionally dubbed video ready for distribution.



### Architecture Considerations

- **Modular Design**: Structured to support plug-and-play functionality for different ASR, translation, and TTS services, allowing easy integration of alternative technologies.
- **Scalability**: Designed to efficiently handle video files of varying sizes and lengths, from short clips to full-length films, through optimized processing pipelines.
- **Quality Assurance**: Incorporates automated and manual quality checks to ensure translation accuracy, proper timing of subtitles, and naturalness of dubbed audio.

# Project Setup

### Prerequisites

- Python 3.10
- FFmpeg
- Conda (steps to install it described below)

## Setting Up the Environment

Right now the only way to setup langflip is by using Conda. We are working on a poetry and a Python venv setup. 

### 1. Install Conda

If you haven't installed Conda, download and install it from [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/individual).

### 2. Download the project

```bash
git clone https://github.com/FlipSuite/LangFlip.git
cd LangFlip
pip install -r requirements.txt
```

### Create and Activate the Conda Environment

Navigate to the LangFlip project directory and run the following command to create a Conda environment from the `env.yml` file:

```sh
conda env create -f env.yml
conda activate langflip
```
