import os
import sys
import torchaudio
import torch
import  speeches.OpenVoice.se_extractor as se_extractor
from speeches.OpenVoice.api import BaseSpeakerTTS, ToneColorConverter
from transformers import AutoProcessor, BarkModel
import scipy

def generate_speech(sentence, root_path, index, voice_audio_file):
  openvoice_path = os.path.join(root_path, 'speeches', 'OpenVoice')
  checkpoints_path = os.path.join(openvoice_path, 'content', 'checkpoints')
  en_speaker_path = os.path.join(checkpoints_path, 'base_speakers', 'EN')
  converter_path = os.path.join(checkpoints_path, 'converter')

  resources_path = os.path.join(openvoice_path, 'resources')

  processor = AutoProcessor.from_pretrained("suno/bark")
  model = BarkModel.from_pretrained("suno/bark")

  voice_preset = "v2/fr_speaker_0"

  inputs = processor("Bonjour je m'appele rémy et je test bark pour voir si ça marche", voice_preset=voice_preset)

  audio_array = model.generate(**inputs)
  audio_array = audio_array.cpu().numpy().squeeze()
  
  sample_rate = model.generation_config.sample_rate
  scipy.io.wavfile.write("bark_out.wav", rate=sample_rate, data=audio_array)

  # device="cuda:0" if torch.cuda.is_available() else "cpu"
  # reference_voice_clips_location = os.path.join(root_path, 'data_management')

  # base_speaker_tts = BaseSpeakerTTS(f'{en_speaker_path}/config.json', device=device)
  # base_speaker_tts.load_ckpt(f'{en_speaker_path}/checkpoint.pth')

  # tone_color_converter = ToneColorConverter(f'{converter_path}/config.json', device=device)
  # tone_color_converter.load_ckpt(f'{converter_path}/checkpoint.pth')

  # source_se = torch.load(f'{en_speaker_path}/en_default_se.pth').to(device)

  # target_se, audio_name = se_extractor.get_se(voice_audio_file, tone_color_converter, target_dir='processed', vad=True)

  # save_path = f'{reference_voice_clips_location}/output_en_default.wav'

  # Run the base speaker tts
  # src_path = f'{reference_voice_clips_location}/tmp.wav'
  # base_speaker_tts.tts(sentence, src_path, speaker='default', language='French', speed=1.0)

  # Run the tone color converter
  # encode_message = "@MyShell"
  # tone_color_converter.convert(
  #     audio_src_path=src_path,
  #     src_se=source_se,
  #     tgt_se=target_se,
  #     output_path=save_path,
  #     message=encode_message)
  # save_audio_as_wav(pcm_audio=pcm_audio, output_path=output_file_path)

  return "done"

def save_audio_as_wav(pcm_audio, output_path, sample_rate=24000):
  if pcm_audio.dim() == 1:
    pcm_audio = pcm_audio.unsqueeze(0)
  converted_pcm_audio = pcm_audio.squeeze().cpu()
  torchaudio.save(output_path, converted_pcm_audio, sample_rate)