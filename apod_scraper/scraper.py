import os
import pathlib
import shutil

import requests
from bs4 import BeautifulSoup
from requests.compat import urljoin

# apod images directory name
APOD_IMAGES_DIRECTORY = "apod_images"
BASE_URL = "http://apod.nasa.gov/apod/archivepix.html"

# create a directory to store images, if it does not exist already
pathlib.Path(APOD_IMAGES_DIRECTORY).mkdir(exist_ok=True)

# Downloading the index page
apod_base_page = requests.get(BASE_URL).text

for link in BeautifulSoup(apod_base_page, "lxml").find_all('a'):
    print("Following link:", link)
    href = urljoin(BASE_URL, link["href"])

    # Follow the link and pull down the image on that link page
    content = requests.get(href).text

    for img in BeautifulSoup(content, "lxml").find_all('img'):
        img_href = urljoin(href, img["src"])

        print("Downloading image:", img_href)
        img_name = img_href.split("/")[-1]

        response = requests.get(img_href, stream=True)
        with open(os.path.join(APOD_IMAGES_DIRECTORY, img_name), 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
