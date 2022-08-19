import os.path as path
import requests

from Utils.ImagesPathInfo import ImagesPathInfo
from Utils.Tokens import Tokens


class Scraper:

    def Scrape():
        SubRedditsList = open('SubReddits List.txt', 'r')

        ImagesSearchAmount: int = int(input('How much Images ya want from each subreddit ? '))

        for line in SubRedditsList:
                SubReddit = Tokens.Reddit.subreddit(line.strip())

                print(f'Collecting Images from {line.strip()}!')

                for Post in SubReddit.new(limit = ImagesSearchAmount):
                    PostUrl: str = Post.url.lower()

                    if 'png' in PostUrl or 'jpg' in PostUrl:

                        Image = requests.get(PostUrl).content
                        ImageDoesntExist: bool = not path.exists(f'{ImagesPathInfo.ImagePath}{line.strip()}-{Post.id}.png')

                        if ImageDoesntExist:
                            with open(f'{ImagesPathInfo.ImagePath}{line.strip()}-{Post.id}.png', 'wb') as ImageDownloader:
                                ImageDownloader.write(Image)

                    else:
                            print('Encounterd a post without an Image *angry face*')


Scraper.Scrape()
