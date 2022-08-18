import os.path as path
import requests

from Utils.MemesPathInfo import MemesPathInfo
from Utils.Tokens import Tokens


class Scraper:

    SubRedditsList = open('SubReddits List.txt', 'r')

    MemesSearchAmount: int = int(input('How much memes ya want from each subreddit ? '))

    for line in SubRedditsList:
            SubReddit = Tokens.Reddit.subreddit(line.strip())

            print(f'Collecting memes from {line.strip()}!')

            for Post in SubReddit.new(limit = MemesSearchAmount):
                PostUrl: str = Post.url.lower()

                if 'png' in PostUrl or 'jpg' in PostUrl:

                    Image = requests.get(PostUrl).content
                    ImageDoesntExist: bool = not path.exists(f'{MemesPathInfo.ImagePath}{line.strip()}-{Post.id}.png')
                    
                    if ImageDoesntExist:
                        with open(f'{MemesPathInfo.ImagePath}{line.strip()}-{Post.id}.png', 'wb') as ImageDownloader:
                            ImageDownloader.write(Image)

                else:
                        print('Encounterd a post without a meme *angry face*')
