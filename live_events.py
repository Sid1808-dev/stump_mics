import requests
import openai

openai.api_key = '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'

headers = {
    "X-RapidAPI-Key": "f9a9ee5e01msh714c7d818ae41b7p1b086cjsn059f15069adc",
    "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

def fetch_live_match_commentary():
    """

    :return: fetch live commentary
    """

    headers = {
        "X-RapidAPI-Key": "f9a9ee5e01msh714c7d818ae41b7p1b086cjsn059f15069adc",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }

    url_live_match = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

    response_live_match = requests.get(url_live_match, headers=headers)
    live_match_id = -1
    for stats in response_live_match.json()['typeMatches']:
        if stats['matchType'] == 'International':
            series = stats['seriesMatches'][0]
            if 'seriesAdWrapper' in series.keys():
                matches = series['seriesAdWrapper']['matches']
                for match in matches:
                    match_id = match['matchInfo']['matchId']
                    live_match_id = match_id

    url_comm = f"https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/{live_match_id}/comm"
    #
    commentary_word = ""
    if live_match_id != -1:
        response_comm = requests.get(url_comm, headers=headers)
        comm_dict = response_comm.json()['commentaryList'][0]
        commentary_word = comm_dict['commText']
        commentary_word = commentary_word.strip('B0$')

        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"Paraphrase {commentary_word} in Danni Morrison's iconic style"
        )

        commentary_style_parraphrased_text = str(response['choices'][0]['text'])
        print(commentary_style_parraphrased_text)
    else:
        commentary_style_parraphrased_text = 'लाइव गेम में कोई अपडेट नहीं, कुछ नया होने का इंतजार है'


    return  commentary_style_parraphrased_text

