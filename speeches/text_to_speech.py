import os
import sys
import torchaudio
import torch
import  speeches.OpenVoice.se_extractor as se_extractor
from speeches.OpenVoice.api import BaseSpeakerTTS, ToneColorConverter

def generate_speech(sentence, root_path, index):
  openvoice_path = os.path.join(root_path, 'speeches', 'OpenVoice')
  checkpoints_path = os.path.join(openvoice_path, 'content', 'checkpoints')
  en_speaker_path = os.path.join(checkpoints_path, 'base_speakers', 'EN')
  converter_path = os.path.join(checkpoints_path, 'converter')

  resources_path = os.path.join(openvoice_path, 'resources')

  device="cuda:0" if torch.cuda.is_available() else "cpu"
  reference_voice_clips_location = os.path.join(root_path, 'data_management')

  base_speaker_tts = BaseSpeakerTTS(f'{en_speaker_path}/config.json', device=device)
  base_speaker_tts.load_ckpt(f'{en_speaker_path}/checkpoint.pth')

  tone_color_converter = ToneColorConverter(f'{converter_path}/config.json', device=device)
  tone_color_converter.load_ckpt(f'{converter_path}/checkpoint.pth')

  source_se = torch.load(f'{en_speaker_path}/en_default_se.pth').to(device)

  reference_speaker = f'{resources_path}/example_reference.mp3'
  target_se, audio_name = se_extractor.get_se(reference_speaker, tone_color_converter, target_dir='processed', vad=True)

  save_path = f'{reference_voice_clips_location}/output_en_default.wav'

  # Run the base speaker tts
  src_path = f'{reference_voice_clips_location}/tmp.wav'
  base_speaker_tts.tts(sentence, src_path, speaker='default', language='English', speed=1.0)

  # Run the tone color converter
  encode_message = "@MyShell"
  tone_color_converter.convert(
      audio_src_path=src_path,
      src_se=source_se,
      tgt_se=target_se,
      output_path=save_path,
      message=encode_message)
  # save_audio_as_wav(pcm_audio=pcm_audio, output_path=output_file_path)

  return "done"

def save_audio_as_wav(pcm_audio, output_path, sample_rate=24000):
  if pcm_audio.dim() == 1:
    pcm_audio = pcm_audio.unsqueeze(0)
  converted_pcm_audio = pcm_audio.squeeze().cpu()
  torchaudio.save(output_path, converted_pcm_audio, sample_rate)