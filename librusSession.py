from requests.cookies import cookiejar_from_dict
import getCookie
from requests import Session

def create(username, password):
    tokens = getCookie.get(username, password)
    s = Session()
    s.cookies = cookiejar_from_dict({'DZIENNIKSID': tokens['clientToken']})
    return s