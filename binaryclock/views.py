from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import json

from .models import User, Event
from binaryclock.auth import *

CLIENT_SECRET_FILE = 'binaryclock/static/client_secret_519490395897-tvp2ffap7lrme2lev0nmc5ug2br7njd9.apps.googleusercontent.com.json'


def index(request):
	# Pass data to view
	user = User.objects.filter(logged_in=True)
	context = {
		'email': user[0].email if user else "",
		'events_list': Event.objects.filter(user__logged_in=True).order_by('start_time')
	}

	return render(request, 'index.html', context)

def storeauthcode(request):
	if request.method == 'POST':
		# If this request does not have header, this could be a CSRF
		if not 'CSRF_COOKIE' in request.META:
			abort(403)

		# Authorization code from logged in user
		auth_code = json.load(request)

		# Exchange auth code for access token, refresh token, and ID token
		credentials = client.credentials_from_clientsecrets_and_code(
	    CLIENT_SECRET_FILE,
	    [
	    	'https://www.googleapis.com/auth/calendar.readonly', 
	    	'https://www.googleapis.com/auth/userinfo.profile', 
	    	'https://www.googleapis.com/auth/userinfo.email'
	    ],
	    auth_code['code'])

		# Log out other users
		User.objects.all().update(logged_in=False)
		
		# Insert/update logged-in user
		user = User(
			cred=credentials.to_json(),
			email=credentials.id_token['email'],
			uid=credentials.id_token['sub'],
			logged_in=True
		)
		user.save()
		
		# Update calendar events
		update_events(user)

		# Pass data to view
		context = {
			'email': user.email,
			'events_list': Event.objects.filter(user__logged_in=True).order_by('start_time')
		}
		print(context['events_list'])
		return HttpResponse(context)

	elif request.method == 'GET':
		return redirect('/clock')