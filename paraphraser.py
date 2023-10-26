import openai


def paraphrase_live_commentary(commentary_word: str):
    """
    This Function inputs the live commentary fetched from cricbuzz API and Paraphrases it into the custom style of AI
    Commentator to provide quirks and popular phrases used by the Commentator
    """
    chat_gpt_response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Generate the commentary for {commentary_word} in Danni Morrison querky style in Danni Morrison's "
               f"iconic style"
    )

    paraphrased_commentary_style = str(chat_gpt_response['choices'][0]['text'])

    return paraphrased_commentary_style
