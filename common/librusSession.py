from requests.cookies import cookiejar_from_dict
import common.getCookie as getCookie
from requests import Session

def create(username, password):
    tokens = getCookie.get(username, password)
    if tokens is None:
        return None
    s = Session()
    s.cookies = cookiejar_from_dict({'DZIENNIKSID': tokens['clientToken']})
    return {'session': s, 'token': tokens['clientToken']}

def create_with_token(token):
    s = Session()
    s.cookies = cookiejar_from_dict({'DZIENNIKSID': token})
    return s