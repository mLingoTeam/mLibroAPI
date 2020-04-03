from bs4 import BeautifulSoup
import config
import uuid
import datetime
import time

cfg = config.load()

def parse(session, html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find_all('table')[1]

    tasks = {
        'assingments': {
            'na_dzisiaj': [],
            'pozostale': []
        }
    }
    today = datetime.datetime.today()

    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if(len(columns) == 10):
            button = columns[9].find_all('input')
            onclick_attr = button[0]['onclick']
            url = get_view_url(onclick_attr)
            desc = get_task_desc(session, url)
            task = {
                "id": str(uuid.uuid4()),
                'przedmiot': columns[0].get_text().strip(),
                'tytul': columns[2].get_text().strip(),
                'tresc': desc,
                'data_zadania': columns[4].get_text().strip(),
                'termin_oddania': columns[6].get_text().strip()
            }
            task_end = datetime.datetime.strptime(task['termin_oddania'], '%Y-%m-%d')

            if(is_valid(today, task_end)):
                if(is_today(today, task_end)):
                    tasks['assingments']['na_dzisiaj'].append(task)
                else:
                    tasks['assingments']['pozostale'].append(task)
            
    return tasks


def get_task_desc(session, url):
    r = session.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    table = soup.find_all('table')[0]
    desc = table.find_all('tr')[6].find_all('td')[1].get_text()
    return desc.strip()

def get_view_url(attr):
    url = cfg['client_url'] + attr.split('\'')[1]
    return url

def is_valid(today, end_date):
    if today < end_date:
        return True
    else:
        return False

def is_today(today, end_date):
    if today == end_date:
        return True
    else:
        return False