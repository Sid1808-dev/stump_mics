from avatar_test import generate_ai_avatar_from_audio
from live_events import fetch_live_match_commentary
from convo import live_commentary_speech, get_all_voices
from paraphraser import paraphrase_live_commentary
from moviepy.editor import *
from os import startfile
from translate import translate_commentary

# Fetching live cricket commentary events from CricBUzz API
live_commentary = fetch_live_match_commentary()

# paraphrased_commentary = paraphrase_live_commentary(live_commentary)


# translate Commentary
# hindi_commentary = translate_commentary(live_commentary)

# Say Commentary for the live commentary
live_commentary_speech(live_commentary)
# live_commentary_speech(hindi_commentary)
# live_commentary_speech(paraphrased_commentary)
# get_all_voices()

# Generate AI Avatar
generate_ai_avatar_from_audio('output.wav', 'amitabh.png')
# #
# clip = VideoFileClip("output.mp4")
# clip.preview()

startfile('output.mp4')
