from base64 import b64decode
import webbrowser
import openai


def generateIme_AndOpen(prompt, image_count):
    images=[]
    response=openai.Image.create(
        prompt=prompt,
        n=image_count,
        size='512x512',
        response_format='url'
    )

    for image in response['data']:
        webbrowser.open(image.url)


openai.api_key = "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"

generateIme_AndOpen("cats moonwalking",1)