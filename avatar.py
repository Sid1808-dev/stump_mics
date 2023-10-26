import requests

AUDIO_URL = "https://api.d-id.com/audios"
TALKS_URL = "https://api.d-id.com/talks"

headers = {
    "accept": "application/json",
    "authorization": "Basic c2lkZGhhcnRoc2hhcm1hMTgwOEBnbWFpbC5jb20:_3ABHIBAIXQlehYB2Iqae"
}

talks_headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic YzJsa1pHaGhjblJvYzJoaGNtMWhNVGd3T0VCbmJXRnBiQzVqYjIwOl8zQUJISUJBSVhRbGVoWUIySXFhZQ=="
}


def generate_ai_avatar_from_audio(audio_file: str, source_image_url: str):
    """
    This Function inputs the generated Audio File for the Over and AI Avatar Image Created using midjourney AI and
    creates a custom animation for the AI Commentator
    """

    # Upload Image
    files = {"audio": (audio_file, open(audio_file, "rb"), "audio/mpeg")}
    audio_upload_response = requests.post(AUDIO_URL, files=files, headers=headers)

    # Generate Avatar using d-id api
    payload = {
        "script": {
            "type": "audio",
            "subtitles": "false",
            "provider": {
                "type": "microsoft",
                "voice_id": "en-US-JennyNeural"
            },
            "ssml": "false",
            "audio_url": f"https://jumpshare.com/s/jgO87om55dDmEIFhhCQj/{audio_file}"
        },
        "config": {
            "fluent": "false",
            "pad_audio": "0.0"
        },
        "source_url": source_image_url
    }

    talks_response = requests.post(TALKS_URL, json=payload, headers=talks_headers)
    print(talks_response.content)
