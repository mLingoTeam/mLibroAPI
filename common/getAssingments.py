import common.librusSession as librusSession
import common.homeworkParser as hp
import common.config as config
import json
import sys


def get(username, password):
    cfg = config.load()
    session = librusSession.create(username, password)
    r = session.get(cfg['homework_url'])
    tasks = hp.parse(session, r.text)
    return tasks