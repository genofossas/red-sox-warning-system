import icalendar as ic
import os
from dotenv import load_dotenv
import requests
from datetime import date, datetime
from pathlib import Path
from pytextbelt import Textbelt
from zoneinfo import ZoneInfo

# Loaing fields from .env
load_dotenv()

# Timezone for converting
NEW_YORK = ZoneInfo("America/New_York")
api_key = os.getenv("TEXTBELT_API_KEY")

# Log files
err_log_file = open('err.log', 'a')
log_file = open('success.log', 'a')

# Write to the error log file
def write_err(msg):
    err_log_file.write(f'{datetime.today()}: {msg}\n')

def write_success(msg):
    log_file.write(f'{datetime.today()}: {msg}\n')

# Send a text
def send_text(event):
    
    recipient = Textbelt.Recipient(os.getenv("RECIPIENT"))    
    event_start_time = event.get("DTSTART").dt.astimezone(NEW_YORK).time()
    text_contents = f'Hello! This is your friendly reminder that there\'s a Boston Red Sox game at {event_start_time} today.'
    response = recipient.send(text_contents, api_key)
    return response

# Parse function for walking a calendar event. Returns
# true for events on today's date.
def parse_event(ev: ic.Event) -> bool:
    d = ev.get("DTSTART")
    if (d.dt.date() == date.today()):
        return True
    return False

# Get the calendar ics file.
def writeCalFile() -> None:
    url = os.getenv("ICAL_URL")
    result = requests.get(url)
    with open('temp.ical', 'wb') as f:
        f.write(result.content)

# Check the ical file and see if there's an event today.
def check_and_send(calendar) -> dict | None:
    events = calendar.walk("VEVENT", parse_event)
    if len(events) == 0:
        return
    elif len(events) == 1:
        return send_text(events[0])
    else:
        write_err("More than one event, writing the first one for a text.")
        return send_text(events[0])

if __name__ == '__main__':
    # Loading the relevant things from dotenv
    writeCalFile()
    ical_path = Path("temp.ical")
    calendar = ic.Calendar.from_ical(ical_path.read_bytes())
    response = check_and_send(calendar)
    if response == None:
        write_success("No game today.")
    elif response["success"]:
        write_success(f'Sent reminder message. Remaining quota: {response["quotaRemaining"]}')
    else:
        write_err(f'Failed to send message. Response: {response}')
    err_log_file.close()
    log_file.close()