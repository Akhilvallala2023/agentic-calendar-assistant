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
    List upcoming events with their IDs for rescheduling/deletion.
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
        for i, event in enumerate(events, 1):
            title = event.get("summary", "No title")
            start = event["start"].get("dateTime", event["start"].get("date"))
            event_id = event.get("id", "No ID")
            # Format the datetime for better readability
            try:
                if 'T' in start:
                    start_dt = datetime.datetime.fromisoformat(start.replace('Z', '+00:00'))
                    formatted_start = start_dt.strftime('%A, %B %d at %I:%M %p')
                else:
                    formatted_start = start
            except:
                formatted_start = start
            
            msg += f"{i}. **{title}**\n"
            msg += f"   📅 {formatted_start}\n"
            msg += f"   🔑 Event ID: {event_id}\n\n"

        return msg
    except Exception as e:
        return f"❌ Failed to list events: {str(e)}"

@function_tool
def delete_event(event_id: str) -> str:
    """
    Delete a calendar event by ID.
    """
    try:
        service = get_calendar_service()
        service.events().delete(calendarId='primary', eventId=event_id).execute()
        return f"🗑️ Event with ID '{event_id}' has been deleted."
    except Exception as e:
        return f"❌ Failed to delete event: {str(e)}"

def find_event_by_title(title: str) -> str:
    """
    Helper function to find event ID by title/summary.
    """
    try:
        service = get_calendar_service()
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        events_result = service.events().list(
            calendarId='primary',
            timeMin=now,
            maxResults=20,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])

        # Look for events with matching title (case-insensitive)
        for event in events:
            event_title = event.get("summary", "").lower()
            if title.lower() in event_title:
                return event.get("id", "")
        
        return ""
    except Exception as e:
        return ""

@function_tool
def reschedule_event(event_id: str, new_start_datetime: str, duration_minutes: int = 60) -> str:
    """
    Reschedule an existing calendar event.
    """
    try:
        service = get_calendar_service()
        event = service.events().get(calendarId='primary', eventId=event_id).execute()

        new_start = datetime.datetime.fromisoformat(new_start_datetime)
        new_end = new_start + datetime.timedelta(minutes=duration_minutes)

        event['start'] = {'dateTime': new_start.isoformat(), 'timeZone': 'America/New_York'}
        event['end'] = {'dateTime': new_end.isoformat(), 'timeZone': 'America/New_York'}

        updated_event = service.events().update(calendarId='primary', eventId=event_id, body=event).execute()

        return f"⏰ Event '{event['summary']}' has been rescheduled to {new_start.strftime('%A, %B %d at %I:%M %p')}."
    except Exception as e:
        return f"❌ Failed to reschedule event: {str(e)}"

@function_tool
def reschedule_event_by_title(title: str, new_start_datetime: str, duration_minutes: int = 60) -> str:
    """
    Reschedule an existing calendar event by searching for its title.
    """
    try:
        # Find the event by title
        event_id = find_event_by_title(title)
        if not event_id:
            return f"❌ Could not find an event with title containing '{title}'. Please check your event list."
        
        # Use the existing reschedule function
        return reschedule_event(event_id, new_start_datetime, duration_minutes)
    except Exception as e:
        return f"❌ Failed to reschedule event: {str(e)}"

@function_tool
def delete_event_by_title(title: str) -> str:
    """
    Delete a calendar event by searching for its title.
    """
    try:
        # Find the event by title
        event_id = find_event_by_title(title)
        if not event_id:
            return f"❌ Could not find an event with title containing '{title}'. Please check your event list."
        
        # Get event details for confirmation
        service = get_calendar_service()
        event = service.events().get(calendarId='primary', eventId=event_id).execute()
        event_title = event.get('summary', 'Unknown')
        
        # Delete the event
        service.events().delete(calendarId='primary', eventId=event_id).execute()
        return f"🗑️ Event '{event_title}' has been deleted."
    except Exception as e:
        return f"❌ Failed to delete event: {str(e)}"
