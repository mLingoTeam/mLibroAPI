from requests import Session
from os import path
from json import dumps, loads

api_url = 'https://api.librus.pl'
client_url = 'https://synergia.librus.pl'
client_index = 'https://synergia.librus.pl/uczen/index'

def get(username, password):
        """
        Generates a Token from username & password.
        """
        s = Session()
        s.get('https://api.librus.pl/OAuth/Authorization?\
            client_id=46&response_type=code&scope=mydata')
        api_token = s.cookies.get('DZIENNIKSID', domain='api.librus.pl')

        r = s.post(
            url='https://api.librus.pl/OAuth/Authorization?client_id=46',
            data={"action": "login", "login": username, "pass": password}
        )

        if r.status_code is not 200:
            return None

        goTo = r.json()['goTo']
        r = s.get('https://api.librus.pl' + goTo)
        if r.status_code is not 200:
            print('Failed to log in')
        client_token = s.cookies.get('DZIENNIKSID', domain='synergia.librus.pl')
        return {'apiToken': api_token, 'clientToken': client_token}