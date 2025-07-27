import torch
import os
from songgen import (
    VoiceBpeTokenizer,
    SongGenMixedForConditionalGeneration,
    SongGenProcessor
)
import soundfile as sf

# Set up the model
ckpt_path = "LiuZH-19/SongGen_mixed_pro"  # Path to the pretrained model
device = "cuda:0" if torch.cuda.is_available() else "cpu"
model = SongGenMixedForConditionalGeneration.from_pretrained(
    ckpt_path,
    attn_implementation='sdpa').to(device)
processor = SongGenProcessor(ckpt_path, device)

# Define input text and lyrics
lyrics = """In the morning light, I see your smile
Making every moment worthwhile
Together we'll dance through the night
Our love shining so bright"""

text = "A romantic pop ballad with soft piano and gentle vocals, creating a warm and intimate atmosphere."

# Generate the song
model_inputs = processor(text=text, lyrics=lyrics)
generation = model.generate(**model_inputs,
                do_sample=True,
            )

# Save the generated audio
audio_arr = generation.cpu().numpy().squeeze()
sf.write("songgen_out.wav", audio_arr, model.config.sampling_rate)
print("Song has been generated and saved as 'songgen_out.wav'") 