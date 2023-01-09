import requests

def getImage(link,to) -> None:
    img = requests.get(link).content
    with open(to, 'wb') as handler:
        handler.write(img)
