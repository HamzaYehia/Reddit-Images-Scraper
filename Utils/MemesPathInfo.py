from typing import Dict

import praw
import os.path as path

from Utils.Folder import Folder
from Utils.Token import Token


class MemesPathInfo:

    # Path to save images
    ImagePath: str = Folder.GetImgPath('')

    Folder.CreateFolder(ImagePath)

    # Get token file to log into reddit.
    Creds: Dict = Token.GetToken()


    Reddit = praw.Reddit(client_id = Creds['client_id'],
                        client_secret = Creds['client_secret'],
                        user_agent = Creds['user_agent'],
                        username = Creds['username'],
                        password = Creds['password'])
