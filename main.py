from avatar import generate_ai_avatar_from_audio
from convo import live_commentary_speech
from live_events import fetch_live_match_commentary
from paraphraser import paraphrase_live_commentary

# Code to Generate AI Commentary based on Live Events fetched from Cricbuzz API

# Fetching live cricket commentary events from CricBUzz API
live_commentary = fetch_live_match_commentary()

# Paraphrase the Commentary Using OpenAI ChatGPT API
paraphrase_live_commentary(live_commentary)

# Say Commentary for the live match
live_commentary_speech(live_commentary)

# Generate Avatar based on audio
audio_file_generated = "output.mp3"
image_url = "https://images2.imgbox.com/ba/4f/bwis553N_o.jpg"
generate_ai_avatar_from_audio(audio_file_generated, image_url)

