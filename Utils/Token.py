import os.path as path
from typing import Dict
import stdiomask
import pickle


class Token:

    def CreateToken() -> Dict:
        Creds = {}
    
        Creds['client_id'] = input('client_id: ')
        Creds['client_secret'] = stdiomask.getpass(prompt='client_secret: ')
        Creds['user_agent'] = input('user_agent: ')
        Creds['username'] = input('username: ')
        Creds['password'] = stdiomask.getpass(prompt='password: ')

        return Creds


    def GetToken():
        if path.exists('Token.pickle'):
            with open('Token.pickle', 'rb') as Token:
                Creds = pickle.load(Token)
        else:
            Creds = Token.CreateToken()
            TokenFile = open("Token.pickle","wb")
            pickle.dump(Creds, TokenFile)
            
        return Creds
