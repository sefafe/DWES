from PIL import Image, ImageTk
import requests, threading
from io import BytesIO

class Cell:

    def __init__(self, title, url, description):
        self.title = title
        self.image_tk=threading.Thread(target=self.load_image_from_url(url)).start
        self.description = description
        self.description=description

    def load_image_from_url(self,url):
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        self.image_tk = ImageTk.PhotoImage(img_data)
