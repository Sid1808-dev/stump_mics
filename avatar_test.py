import requests
from urllib.request import urlretrieve
import pandas as pd




AUDIO_URL = "https://api.d-id.com/audios"
IMAGE_URL = "https://api.d-id.com/images"
TALKS_URL = "https://api.d-id.com/talks"

headers = {
    "accept": "application/json",
    "authorization": "Basic cml0YUBzdGpvc2VwaHBhdGhhbmtvdC5jb20:jVG0OL8pEpSEJvUW0fbak"
}


def generate_ai_avatar_from_audio(audio_file: str, image_file: str):
    image_files = {"image": (image_file, open(image_file, "rb"), "image/png")}
    image_response = requests.post(IMAGE_URL, files=image_files, headers=headers)
    print(image_response.json())
    image_location = image_response.json()['url']
    print("Uploaded Avatar Image to Remote Location: ", image_location)

    audio_files = {"audio": (audio_file, open(audio_file, "rb"), "audio/mpeg")}
    audio_response = requests.post(AUDIO_URL, files=audio_files, headers=headers)
    audio_location = audio_response.json()['url']
    print("Uploaded Avatar Audio to Remote Location: ", audio_location)

    data = {'Name': ['image_url', 'audio_url'], 'Value': [image_location, audio_location]}
    df = pd.DataFrame(data)
    df.to_csv(r'C:\Code\live-streaming-demo\data.csv')

    payload = {
        "script": {
            "type": "audio",
            "subtitles": "false",
            "provider": {
                "type": "microsoft",
                "voice_id": "en-US-JennyNeural"
            },
            "ssml": "false",
            "audio_url": f"{audio_location}"
        },
        "config": {
            "fluent": "false",
            "pad_audio": "0.0"
        },
        "source_url": f"{image_location}"
    }

    talks_response = requests.post(TALKS_URL, json=payload, headers=headers)
    print(talks_response)
    print(talks_response.json()['id'])

    specific_talk_url = f"https://api.d-id.com/talks/{talks_response.json()['id']}"

    # sample_talk_url = 'https://api.d-id.com/talks/tlk_3P6LPQ3BD1P_vXQF6OumK'

    response_for_talk = requests.get(specific_talk_url, headers=headers)
    response_talk_json = dict(response_for_talk.json())
    print(type(response_talk_json))
    print(response_talk_json.keys())
    while "result_url" not in response_talk_json.keys():
        response_for_talk = requests.get(specific_talk_url, headers=headers)
        response_talk_json = response_for_talk.json()

    print(response_for_talk.text)
    print(response_for_talk.json()['result_url'])

    urlretrieve(response_for_talk.json()['result_url'], 'output.mp4')
