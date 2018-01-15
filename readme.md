# Binary Clock

This was originally a project for Idea Hacks 2018 at UCLA, to be run on a Beaglebone Black and a 3D printed clock, but we didn't finish in time. So here's a software version.

![Screenshot](https://github.com/jachang820/BinaryClock/blob/master/Screenshot-2018-1-14.png)

## Getting Started

The binary clock runs on a Django backend with sqlite3 database, since it was intended to be mostly single-user in a consumer electronic device. It allows the user to log into their Google account to pull the next 10 events. 

### Prerequisites

I have resetted my client secrets file. To run this on your own server, you need to do the following:

* [Goole API Key](https://console.developers.google.com/apis/credentials?project=binary-clock-192007) is necessary to access the Google API in order to import events from the Google Calendar. Follow the link and click *Create credentials*, then *OAuth client ID* and follow all the steps. At the end of the process, download the JSON file to the static folder.
* At the same site, go to *Library* and search for the *Google Calendar API*, and enable it.
* Update the CLIENT_SECRET_FILE in *binaryclock/views.py* (line 9) to the downloaded JSON file.
* Add the following name-value pair to the JSON file right before "javascript-origins" (last entry):
```
"redirect_uris":"http://localhost:8000/clock/"
```

## Authors

* **Jonathan Chang** - *Initial work* - [jachang820](https://github.com/jachang820)

Also, thanks to team mates David James and Robin Zhang for design and planning of this project.

## Next steps

* Make interface more robust in support different screen sizes and cell phones.
* Create an alarm clock that would allow user to add a time and select a ringtone. The app could also read the event summaries for that day, using Amazon's Polly API. Users could turn off the alarm by swiping right on some component, then stop the event summary reading by swiping back left.
* Use Google event watch service to automatically update events. This requires a domain name.
* Use React Native to build cell versions.
* 3D print the originally planned binary clock, run server on a microcontroller connected to LEDs and a speaker.