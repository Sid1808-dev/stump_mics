import requests
import soundfile as sf
import soundcard as sc

CHUNK_SIZE = 1024
headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": "4b43efcdba17ff4db7a1cbe25e6c389d"
}


def get_all_voices():
    all_voices_url = "https://api.elevenlabs.io/v1/voices"
    response = requests.get(all_voices_url, headers=headers)

    print(response.text)
    return response.text


def live_commentary_speech(commentary_word: str):
    eleven_labs_url = "https://api.elevenlabs.io/v1/text-to-speech/VWyhi825p9udhEUu7YNn"

    data = {
        "text": f"{commentary_word}",
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "style_exaggeration": 0.42
        }
    }

    response = requests.post(eleven_labs_url, json=data, headers=headers)
    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

    default_speaker = sc.default_speaker()
    samples, samplerate = sf.read('output.mp3')

    default_speaker.play(samples, samplerate=samplerate)
