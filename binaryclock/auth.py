from googleapiclient import discovery
import httplib2
from oauth2client import client
from oauth2client import tools
from .models import User, Event
import json
import datetime


def get_calendar(user):
	# Restore credentials of logged in user from database
	credentials = client.Credentials.new_from_json(user.cred)
	http = credentials.authorize(httplib2.Http())

	# Refresh access token if expired
	if credentials.access_token_expired:
		credentials.refresh(http)
		user.cred = credentials
		user.save(['cred'])
		print('token expired')

	# Construct calendar using credentials
	return discovery.build('calendar', 'v3', http=http)


def update_events(user):
	# Delete preexisting events of logged in user
	Event.objects.filter(user__logged_in=True).delete()

	service = get_calendar(user)

	# Retrieve list of next 10 events
	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	eventsResult = service.events().list(
		calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
		orderBy='startTime').execute()
	events = eventsResult.get('items', [])

	if not events:
		print('No upcoming events found.')

	# Save events to database
	for event in events:
		e = Event(
			eid=event['id'],
			summary=event['summary'],
			start_time=event['start'].get('dateTime'),
			start_zone=event['start'].get('timeZone'),
			end_time=event['end'].get('dateTime'),
			end_zone=event['end'].get('timeZone'),
			user=user
		)
		e.save()