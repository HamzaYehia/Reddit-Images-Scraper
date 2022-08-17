import praw
import requests
import cv2
import numpy as np
import os.path as path
import pickle

from Utils.CreateFolder import CreateFolder
from Utils.CreateToken import CreateToken


ImagesSearchAmount: int = int(input('How much memes ya want from each subreddit ? '))


# Path to save images
DirPath = path.dirname(path.realpath(__file__))
ImagePath = path.join(DirPath, "Images/")
IgnorePath = path.join(DirPath, "IgnoreImages/")

CreateFolder(ImagePath)


# Get token file to log into reddit.
if path.exists('Token.pickle'):
    with open('Token.pickle', 'rb') as Token:
        Creds = pickle.load(Token)
else:
    Creds = CreateToken()
    TokenFile = open("Token.pickle","wb")
    pickle.dump(Creds, TokenFile)


Reddit = praw.Reddit(client_id = Creds['client_id'],
                    client_secret = Creds['client_secret'],
                    user_agent = Creds['user_agent'],
                    username = Creds['username'],
                    password = Creds['password'])


SubRedditsFile = open("SubReddits List.txt", "r")
ImgNotFound = cv2.imread('IgnoreImages/ImageNF.png')


for line in SubRedditsFile:
    SubReddit = Reddit.subreddit(line.strip())

    print(f"Collecting memes from {line.strip()}!")

    for Post in SubReddit.new(limit = ImagesSearchAmount):
        PostUrl = Post.url.lower()

        if 'png' or 'jpg' in PostUrl:

            Res = requests.get(PostUrl, stream=True).raw

            Image = np.asarray(bytearray(Res.read()), dtype="uint8")
            Image = cv2.imdecode(Image, cv2.IMREAD_COLOR)

            if np.any(Image):
                if not path.exists(f"{ImagePath}{line.strip()}-{Post.id}.png"):
                    cv2.imwrite(f"{ImagePath}{line.strip()}-{Post.id}.png", Image)
            else:
                print('Encounterd a post without a meme *angry face*')
