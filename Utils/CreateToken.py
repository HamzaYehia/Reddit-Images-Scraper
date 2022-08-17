import stdiomask

def CreateToken():
    Creds = {}

    Creds['client_id'] = input('client_id: ')
    Creds['client_secret'] = stdiomask.getpass(prompt='client_secret: ')
    Creds['user_agent'] = input('user_agent: ')
    Creds['username'] = input('username: ')
    Creds['password'] = stdiomask.getpass(prompt='password: ')

    return Creds
