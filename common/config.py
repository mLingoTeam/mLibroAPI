import json

def load():
    with open('common/config.json') as config_file:
        data = json.load(config_file)
        return data

