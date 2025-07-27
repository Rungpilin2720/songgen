document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('songForm');
    const audioPlayer = document.getElementById('audioPlayer');
    const downloadLink = document.getElementById('downloadLink');
    const errorMessage = document.getElementById('errorMessage');
    const musicTypeElement = document.getElementById('music_type');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Get elements here to ensure they are available
        const loadingSection = document.getElementById('loading');
        const resultSection = document.getElementById('result');
        const outputSection = document.getElementById('output'); // Also get the output section

        if (!loadingSection || !resultSection || !outputSection || !errorMessage || !musicTypeElement) {
            console.error('Required elements not found!');
            // We can't display an error on the page if errorMessage is missing, but log to console
            return; // Stop execution if essential elements are missing
        }
        
        // Show loading state
        outputSection.classList.remove('hidden'); // Show the output section first
        loadingSection.classList.remove('hidden');
        resultSection.classList.add('hidden');
        errorMessage.classList.add('hidden'); // Hide previous errors
        
        const lyrics = document.getElementById('lyrics').value;
        const description = document.getElementById('description').value;
        const musicType = musicTypeElement.value;

        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    lyrics: lyrics,
                    description: description,
                    music_type: musicType
                })
            });
            
            const data = await response.json();
            
            if (data.success) {
                // Update audio player and download link
                audioPlayer.src = data.audio_url;
                downloadLink.href = data.audio_url;
                
                // Show result
                loadingSection.classList.add('hidden');
                resultSection.classList.remove('hidden');
            } else {
                // Display error on the page using the retrieved errorMessage element
                errorMessage.textContent = data.error || 'Failed to generate song';
                errorMessage.classList.remove('hidden');
                loadingSection.classList.add('hidden');
            }
        } catch (error) {
            // Display error on the page using the retrieved errorMessage element
            errorMessage.textContent = error.message;
            errorMessage.classList.remove('hidden');
            loadingSection.classList.add('hidden');
        }
    });
}); 