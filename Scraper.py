import os.path as path
import numpy as np
import requests
import cv2

from Utils.MemesPathInfo import MemesPathInfo
from Utils.Tokens import Tokens


class Scraper:

    SubRedditsList = open("SubReddits List.txt", "r")
    ImgNotFound = cv2.imread('IgnoreImages/ImageNF.png')

    ImagesSearchAmount: int = int(input('How much memes ya want from each subreddit ? '))

    for line in SubRedditsList:
            SubReddit = Tokens.Reddit.subreddit(line.strip())

            print(f"Collecting memes from {line.strip()}!")

            for Post in SubReddit.new(limit = ImagesSearchAmount):
                PostUrl: str = Post.url.lower()

                if 'png' or 'jpg' in PostUrl:

                    Res = requests.get(PostUrl, stream=True).raw

                    Image = np.asarray(bytearray(Res.read()), dtype="uint8")
                    Image = cv2.imdecode(Image, cv2.IMREAD_COLOR)

                    if np.any(Image):
                        if not path.exists(f"{MemesPathInfo.ImagePath}{line.strip()}-{Post.id}.png"):
                            cv2.imwrite(f"{MemesPathInfo.ImagePath}{line.strip()}-{Post.id}.png", Image)
                    else:
                        print('Encounterd a post without a meme *angry face*')
