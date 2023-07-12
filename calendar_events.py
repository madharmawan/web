#Set-ExecutionPolicy Unrestricted -Scope Process

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


"""
credentials = Credentials.from_authorized_user_file('C:/Users/anddh/projects/web_project/webapp/client_secret_642157501724-hamebvpcero1cug5f0gfo5h0kmmjc48i.apps.googleusercontent.com.json')

service = build('calendar', 'v3', credentials=credentials)

calendar_id = 'primary'  # Use 'primary' for the primary calendar associated with the account
events_result = service.events().list(calendarId=calendar_id).execute()
events = events_result.get('items', [])

if not events:
    print('No events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(f"Event: {event['summary']}")
    print(f"Start time: {start}")
    print(f"Location: {event.get('location', 'N/A')}")
    print('---')
"""

# I could not get the refresh token from the credentials when I ran the code above

from google_auth_oauthlib.flow import InstalledAppFlow

# Define the required scopes
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# Specify the path to your credentials JSON file
credentials_file = 'C:/Users/anddh/projects/web_project/webapp/client_secret_642157501724-hamebvpcero1cug5f0gfo5h0kmmjc48i.apps.googleusercontent.com.json'

# Create the flow object
flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)

# Run the authorization flow
credentials = flow.run_local_server(port=0)

# Print the refresh token
print(f"Refresh Token: {credentials.refresh_token}")