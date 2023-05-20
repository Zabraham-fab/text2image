from base64 import b64decode
import webbrowser
import openai

def generateIme_AndSave(prompt, image_count):
    images=[]
    response=openai.Image.create(
        prompt=prompt,
        n=image_count,
        size='512x512',
        response_format='b64_json'
    )

    for image in response['data']:
        images.append(image.b64_json)

    preffix='Img'
    for index, image in enumerate(images):
        with open(f"{preffix}_{index}.jpg","wb") as file:
            file.write(b64decode(image))



openai.api_key = "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"
generateIme_AndSave("cats moonwalking",1)