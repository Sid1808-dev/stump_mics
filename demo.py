from live_events import fetch_live_match_commentary
from convo import live_commentary_speech, get_all_voices

# Fetching live cricket commentary events from CricBUzz API
live_commentary = fetch_live_match_commentary()

# Say Commentary for the live commentary
live_commentary_speech(live_commentary)
get_all_voices()