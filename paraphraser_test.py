import requests

url = "https://paraphrase-genius.p.rapidapi.com/dev/paraphrase/"

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "d7ae87876fmsh0ca729c7e7190d4p123775jsn411abd163c59",
    "X-RapidAPI-Host": "paraphrase-genius.p.rapidapi.com"
}


def paraphrase_live_commentary(commentary_word: str):
    payload = {
        "text": "Hemantha to Kohli, 1 run, to long-off",
        "result_type": "single"
    }

	response = requests.post(url, json=payload, headers=headers)
	paraphrased_commentary = str(response.json()[0])

	return  paraphrased_commentary







