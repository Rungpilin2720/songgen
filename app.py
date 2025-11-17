from flask import Flask, render_template, request, jsonify, send_file
import torch
from songgen import (
    VoiceBpeTokenizer,
    SongGenMixedForConditionalGeneration,
    SongGenProcessor
)
import soundfile as sf
import os
from datetime import datetime

app = Flask(__name__)

# Initialize the model (lazy loading)
model = None
processor = None

def get_model():
    global model, processor
    if model is None:
        ckpt_path = "LiuZH-19/SongGen_mixed_pro"
        device = "cuda:0" if torch.cuda.is_available() else "cpu"
        model = SongGenMixedForConditionalGeneration.from_pretrained(
            ckpt_path,
            attn_implementation='sdpa').to(device)
        processor = SongGenProcessor(ckpt_path, device)
    return model, processor

# Create output directory if it doesn't exist
os.makedirs('static/output', exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_song():
    try:
        data = request.json
        lyrics = data.get('lyrics', '')
        description = data.get('description', '')
        music_type = data.get('music_type', '')

        # Get model (lazy loading)
        model, processor = get_model()

        # Generate the song
        model_inputs = processor(text=description, lyrics=lyrics)
        generation = model.generate(**model_inputs, do_sample=True)

        # Save the generated audio
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f'songgen_out_{timestamp}.wav'
        output_path = os.path.join('static/output', output_filename)
        
        audio_arr = generation.cpu().numpy().squeeze()
        sf.write(output_path, audio_arr, model.config.sampling_rate)

        return jsonify({
            'success': True,
            'audio_url': f'/static/output/{output_filename}'
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    # Get port from environment variable (for deployment) or use default
    port = int(os.environ.get('PORT', 5001))
    # Run the app on all interfaces (0.0.0.0) and specified port
    app.run(host='0.0.0.0', port=port, debug=False)
