import datetime, threading, time

try:
	GPIO = __import__(Adafruit_BBIO.GPIO)
except (ImportError, NameError):
	print('System is not a Beaglebone.')


def dec_to_grey_code(dec):
	tens = format(dec // 10, 'b')
	ones = format(dec % 10, 'b')
	return (tens, ones)


# Return time in grey code string
def time_to_grey_code():
	time = datetime.datetime.now().time()
	hour = dec_to_grey_code(time.hour)
	hour = hour[0].zfill(2) + hour[1].zfill(4)
	minute = dec_to_grey_code(time.minute)
	minute = minute[0].zfill(3) + minute[1].zfill(4)
	second = dec_to_grey_code(time.second)
	second = second[0].zfill(3) + second[1].zfill(4)
	return hour + minute + second


# Use pins 21-40
def GPIO_setup():
	for i in range(21, 41):
		GPIO.setup("P8_" + str(i), GPIO.OUT)


# Time of each call
last_call = False
next_call = time.time()

def GPIO_update():
	global next_call

	str_time = time_to_grey_code()

	# Map time to pins starting from MSB
	for i in range(len(str_time)):
		pin = i + 21
		GPIO.output("P8_" + pin, GPIO.HIGH if str_time[i] == 1 else GPIO.LOW)

	# Run every 0.2s
	next_call = next_call + 200000

	# Start a timer process on a new thread
	if last_call == False:
		threading.Timer( next_call - time.time(), GPIO_update ).start()

# Turn off all pins
def GPIO_cleanup():
	GPIO.cleanup()
	last_call = True

try:
	GPIO_setup()
	GPIO_update()
except (NameError):
	print('GPIO failed.')