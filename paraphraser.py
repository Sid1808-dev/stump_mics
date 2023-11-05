import openai

openai.api_key = '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'


def paraphrase_live_commentary(commentary_word: str):
    """
    This Function inputs the live commentary fetched from cricbuzz API and Paraphrases it into the custom style of AI
    Commentator to provide quirks and popular phrases used by the Commentator
    """
    chat_gpt_response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Translate {commentary_word} to Hindi"
    )

    paraphrased_commentary_style = str(chat_gpt_response['choices'][0]['text'])
    # print("Hindi paraphrased Commentary: ", paraphrased_commentary_style)
    return paraphrased_commentary_style
