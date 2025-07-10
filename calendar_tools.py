from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from agents import function_tool
import datetime
import os

SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def get_calendar_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('calendar', 'v3', credentials=creds)

@function_tool
def create_calendar_event(summary: str, start_datetime: str, duration_minutes: int = 60, description: str = None) -> str:
    """
    Create a calendar event.
    """
    try:
        service = get_calendar_service()
        start = datetime.datetime.fromisoformat(start_datetime)
        end = start + datetime.timedelta(minutes=duration_minutes)

        event = {
            'summary': summary,
            'description': description or 'Scheduled via Calendar Agent',
            'start': {'dateTime': start.isoformat(), 'timeZone': 'America/New_York'},
            'end': {'dateTime': end.isoformat(), 'timeZone': 'America/New_York'},
        }

        result = service.events().insert(calendarId='primary', body=event).execute()

        return f"📅 Event created: '{summary}' on {start.strftime('%A, %B %d at %I:%M %p')}.\n🔗 Link: {result.get('htmlLink')}"
    except Exception as e:
        return f"❌ Failed to create event: {str(e)}"

@function_tool
def list_upcoming_events(max_results: int = 10) -> str:
    """
    List upcoming events.
    """
    try:
        service = get_calendar_service()
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        events_result = service.events().list(
            calendarId='primary',
            timeMin=now,
            maxResults=max_results,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])

        if not events:
            return "You have no upcoming events."

        msg = "📅 Upcoming Events:\n"
        for event in events:
            title = event.get("summary", "No title")
            start = event["start"].get("dateTime", event["start"].get("date"))
            msg += f"- {title} at {start}\n"

        return msg
    except Exception as e:
        return f"❌ Failed to list events: {str(e)}"
