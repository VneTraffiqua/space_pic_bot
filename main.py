import requests
from pathlib import Path
import urllib.parse
import os


def get_extension_file(user_url):
    parsed_url = urllib.parse.urlsplit(user_url)
    return os.path.splitext(parsed_url.path)[1]


def get_images(file_path, images_url):
    response = requests.get(images_url)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)


def get_APOD():
    url1 = 'https://api.nasa.gov/planetary/apod'
    settings = {
        'api_key': '8CZXBJ3Z1L4oYihhgJ1ZPC9uXqJafUydUNf7XetN',
    }
    responce = requests.get(url1, params=settings)
    responce.raise_for_status()
    return responce.json()


def get_url_pic_spacex(spacex_url):
    response = requests.get(
        f'{spacex_url}'
    )
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


if __name__ == '__main__':
    Path('./images').mkdir(parents=True, exist_ok=True)
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    for img_num, spacex_url in enumerate(get_url_pic_spacex(url), 1):
        #print(img_num, spacex_url)
        #print(get_extension_file(spacex_url))
        path = f'./images/spacex{img_num}{get_extension_file(spacex_url)}'
        get_images(path, spacex_url)
