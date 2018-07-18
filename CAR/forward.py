import RPi.GPIO as GPIO
import time
import sys
import Tkinter as tk
from picamera import PiCamera
import os 

GPIO.setwarnings(False)

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.OUT)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)


def forward(tf):
	GPIO.output(7, False)
	GPIO.output(11, True)
	GPIO.output(13, True)
	GPIO.output(15, False)
	time.sleep(tf)
	GPIO.cleanup()

	
def reverse(tf):
	GPIO.output(7, True)
	GPIO.output(11, False)
	GPIO.output(13, False)
	GPIO.output(15, True)
	time.sleep(tf)
	GPIO.cleanup()
	
def turn_left(tf):
	GPIO.output(7, True)
	GPIO.output(11, True)
	GPIO.output(13, True)
	GPIO.output(15, False)
	time.sleep(tf)
	GPIO.cleanup()

def turn_right(tf):
	GPIO.output(7, False)
	GPIO.output(11, True)
	GPIO.output(13, False)
	GPIO.output(15, False)
	time.sleep(tf)
	GPIO.cleanup()

def pivot_left(tf):
	GPIO.output(7, True)
	GPIO.output(11, False)
	GPIO.output(13, True)
	GPIO.output(15, False)
	time.sleep(tf)
	GPIO.cleanup()
	
def pivot_right(tf):
	GPIO.output(7, False)
	GPIO.output(11, True)
	GPIO.output(13, False)
	GPIO.output(15, True)
	time.sleep(tf)
	GPIO.cleanup()

def camera_on():
	#camera = PiCamera()
	#camera.start_preview()
	#sleep(1)
	#camera.stop_preview()
	os.system("raspivid -o - -t 0 -hf -w 400 -h 200 -fps 24 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8160}' :demux=h264")


#def camera_off():
	#camera = PiCamera()
	#camera.start_preview()
	#sleep(.03)
	#camera.stop_preview()
	
def key_input(event):
	init()
	global current_duty
	servo = 12
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(servo,GPIO.OUT)
	increment = .5
	print 'Key:', event.keysym
	key_press = event.keysym
	sleep_time = 0.03
	
	if key_press.lower() == 'w':
		forward(sleep_time)
	elif key_press.lower() == 's':
		reverse(sleep_time)
	elif key_press.lower() == 'a':
		turn_left(sleep_time)
	elif key_press.lower() == 'd':
		turn_right(sleep_time)		
	elif key_press.lower() == 'q':
		pivot_left(sleep_time)
	elif key_press.lower() == 'e':
		pivot_right(sleep_time)	
	elif key_press.lower() == 'o':
		if current_duty+increment < 13: 
			p.ChangeDutyCycle(current_duty+increment)
			time.sleep(.03)
			GPIO.cleanup()
			current_duty = current_duty + increment
		
		else:
			p.ChangeDutyCycle(13)
			time.sleep(.03)
			GPIO.cleanup()
			current_duty = current_duty
		
	elif key_press.lower() == 'p':
		if current_duty-increment > 2.5: 
			p.ChangeDutyCycle(current_duty-increment)
			time.sleep(.03)
			GPIO.cleanup()
			current_duty = current_duty - increment
		else:
			p.ChangeDutyCycle(2.5)
			time.sleep(.03)
			GPIO.cleanup()
			current_duty = current_duty	
	elif key_press.lower() == 'u':
		camera_on()
	elif key_press.lower() == 'i':
		camera_off()
	else:
		GPIO.cleanup()


servo = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo,GPIO.OUT)
p=GPIO.PWM(servo,50)# 50hz frequency
p.start(7.5)
global current_duty
current_duty = 7.5	
command = tk.Tk()
command.bind('<KeyPress>',key_input)
command.mainloop()
