import requests
from bs4 import BeautifulSoup
import copy

class PaginaPrincipal():
    def __init__(self):
        self.export_json = {}
        self.webpage_searcher = "https://visortmo.com/view_uploads/76229"
        
    def open_the_page(self):
        header = {
    "Referer": "https://visortmo.com/library/manga/11338/saitama-chainsaw-shoujo"
}
        response = requests.get(self.webpage_searcher, headers=header)
        op=1
PaginaPrincipal().open_the_page()


def downloadImageWithReferer(image_url, referer_url):
    response = requests.get(image_url, headers={"Referer": referer_url}, verify=False)

    if response.status_code == 200:
        filename = "downloaded_image.webp"

        with open(filename, "wb") as file:
            file.write(response.content)

        print(f"Image downloaded and saved as '{filename}'")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

# URL of the image you want to download
image_url = "https://japanreader.com/uploads/20231201/b72ca230fb1a84fa9c92ac8d5b6d6fc7/3cef39e8.webp"
# The referer URL to include in the header
referer_url = "https://visortmo.com/viewer/b72ca230fb1a84fa9c92ac8d5b6d6fc7/cascade"

    # Download the image
#downloadImageWithReferer(image_url, referer_url)