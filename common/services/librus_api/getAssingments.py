import common.services.librus_api.librusSession as librusSession
import common.services.librus_api.homeworkParser as hp
import common.config as config
import json
import sys


def get(username, password):
    cfg = config.load()
    res = librusSession.create(username, password)
    if res is None:
        return None
    session = res['session']
    r = session.get(cfg['homework_url'])
    if(r.status_code != 200):
        return None
    tasks = hp.parse(session, r.text)
    tasks['token'] = res['token']
    return tasks

def refresh(token):
    cfg = config.load()
    session = librusSession.create_with_token(token)
    r = session.get(cfg['homework_url'])
    if(r.status_code != 200):
        return None
    tasks = hp.parse(session, r.text)
    return tasks