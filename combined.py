from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdin

keyboard = Controller()
string = "This is a really long string"

# gets password and features (intervals) from input:
password = raw_input()
features = raw_input()

# formats password into an appropriate string format
password = password.split(",")
password = password[:len(password)/2 + 1]
password = "".join(password)

# formats features into 2 lists:
# - Key Press Time
# - Key Interval Time
features = [float(a) for a in features.split(",")]
key_press = features[:len(features)/2 + 1]
key_int = features[len(features)/2 + 1:]

# prints password acconding to the KPT and KIT:
for i in range(len(password)):
	keyboard.press(password[i])
	sleep(key_press[i])
	keyboard.release(password[i])
	# There won't be KIT for the last characters,
	# so don't try to find the interval (doesn't exist):
	if (i != len(password)-1):
		sleep(key_int[i])

# keyboard.press(Key.enter)
# keyboard.release(Key.enter)

# tcflush(stdin, TCIFLUSH)
