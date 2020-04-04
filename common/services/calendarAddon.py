import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']

def sync(tasks):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'common/services/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    for task in tasks:
        event = create_gc_event_obj(task)
        service.events().insert(calendarId='primary', body=event).execute()

def create_gc_event_obj(task):
    return {
        'summary': task['tytul'],
        'description': task['tresc'],
        'start': {
            'dateTime': task['termin_oddania'],
            'timeZone': 'Europe/Berlin',
        },
        'end': {
            'dateTime': task['termin_oddania'],
            'timeZone': 'Europe/Berlin',
        }
    }
