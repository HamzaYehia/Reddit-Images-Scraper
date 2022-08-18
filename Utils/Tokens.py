from typing import Dict
import os.path as path
import stdiomask
import pickle
import praw


class Tokens:

    def CreateToken(self) -> Dict:
        Creds: Dict = {}
    
        Creds['client_id'] = input('client_id: ')
        Creds['client_secret'] = stdiomask.getpass(prompt='client_secret: ')
        Creds['user_agent'] = input('user_agent: ')
        Creds['username'] = input('username: ')
        Creds['password'] = stdiomask.getpass(prompt='password: ')

        return Creds


    def GetToken() -> Dict:
        Creds: Dict

        if path.exists('Token.pickle'):
            with open('Token.pickle', 'rb') as Token:
                Creds = pickle.load(Token)
        else:
            Creds = Tokens.CreateToken()
            TokenFile = open("Token.pickle","wb")
            pickle.dump(Creds, TokenFile)
            
        return Creds


    # Get token file to log into reddit.
    Creds: Dict = GetToken()

    Reddit = praw.Reddit(client_id = Creds['client_id'],
                    client_secret = Creds['client_secret'],
                    user_agent = Creds['user_agent'],
                    username = Creds['username'],
                    password = Creds['password'])
