import requests

# url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
#
# headers = {
#     "content-type": "application/x-www-form-urlencoded",
#     "Accept-Encoding": "application/gzip",
#     "X-RapidAPI-Key": "5eff0fa301msh428aa8b86859bdap140dd3jsn58e3154ffd59",
#     "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
# }

url = "https://translate281.p.rapidapi.com/"

headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "3ab25692bfmsh0b425ebe7557144p10911bjsne21c724bd77e",
	"X-RapidAPI-Host": "translate281.p.rapidapi.com"
}




def translate_commentary(commentary: str):
    # payload = {
    #     "q": commentary,
    #     "target": "hi",
    #     "source": "en"
    # }

    payload = {
        "text": commentary,
        "from": "en",
        "to": "hi"
    }

    response = requests.post(url, data=payload, headers=headers)
    print(response.json())
    # hindi_comm = response.json()['data']['translations'][0]['translatedText']

    hindi_comm = response.json()['response']
    print("Hindi Commentary: ", hindi_comm)
    return hindi_comm


if __name__ == '__main__':
    hindi_comment = translate_commentary("Hello World")
