import requests
from commentary_phrases import get_commentary

LIVE_MATCH_URL = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

cricbuzz_api_headers = {
    "X-RapidAPI-Key": "f9a9ee5e01msh714c7d818ae41b7p1b086cjsn059f15069adc",
    "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

def fetch_live_match_commentary():
    """
    This Function Hits the Cricbuzz API Endpoint and based on the live match fetches the live commentary for the match
    """
    # Fetch the Live Match From Cricbuzz API
    response_live_match = requests.get(LIVE_MATCH_URL, headers=cricbuzz_api_headers)
    live_match_id = -1
    for stats in response_live_match.json()['typeMatches']:
        if stats['matchType'] == 'International':
            series = stats['seriesMatches'][0]
            if 'seriesAdWrapper' in series.keys():
                matches = series['seriesAdWrapper']['matches']
                for match in matches:
                    match_id = match['matchInfo']['matchId']
                    print(match_id)
                    live_match_id = match_id
    print("Live Match ID: ", live_match_id)
    # Fetch Commentary for the Live Match
    url_comm = f"https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/{live_match_id}/comm"
    commentary_word = ""
    if live_match_id != -1:
        response_comm = requests.get(url_comm, headers=cricbuzz_api_headers)
        comm_dict = response_comm.json()['commentaryList'][0]
        commentary_word = comm_dict['commText']
        commentary_word = commentary_word.replace('B0$', '').replace('B1$', '')
        # commentary_word = get_commentary()
        print("Live Commentary: ", commentary_word)
    else:
        commentary_word = 'लाइव गेम में कोई अपडेट नहीं, कुछ नया होने का इंतजार है'


    return  commentary_word

