from tortoise import api, utils
import tortoise.utils.audio as tortoise_audio
import os
import torchaudio
import torch

def generate_speech(sentence, reference_voice_clips, root_path, index):
  reference_clips = [utils.audio.load_audio(p, 22050) for p in reference_voice_clips]

  use_deepspeed = torch.backends.mps.is_available()
  print(f"Using deepspeed: {use_deepspeed}")

  tts = api.TextToSpeech(kv_cache=True, half=True, use_deepspeed=True)
  # pcm_audio = tts.tts_with_preset(sentence, voice_samples=reference_clips, preset='standard')
  voice_samples, conditioning_latents = tortoise_audio.load_voices(['random'])
  pcm_audio = tts.tts_with_preset(sentence, preset='fast', k=1, cvvp_amount=.0, return_deterministic_state=True, use_deterministic_seed=None, conditioning_latents=conditioning_latents, voice_samples=voice_samples)

  reference_voice_clips_location = os.path.join(root_path, 'data_management', 'reference_voice_clips')
  output_file_path = reference_voice_clips_location.replace("reference_voice_clips", f"translated_sentences/{index}.wav")
  save_audio_as_wav(pcm_audio=pcm_audio, output_path=output_file_path)

  return output_file_path

def save_audio_as_wav(pcm_audio, output_path, sample_rate=24000):
  if pcm_audio.dim() == 1:
    pcm_audio = pcm_audio.unsqueeze(0)
  converted_pcm_audio = pcm_audio.squeeze().cpu()
  torchaudio.save(output_path, converted_pcm_audio, sample_rate)