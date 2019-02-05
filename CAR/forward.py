import RPi.GPIO as GPIO
import time
import sys
import Tkinter as tk
from picamera import PiCamera
import os 
from time import sleep

GPIO.setwarnings(False)

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.OUT)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)
	GPIO.setup(40, GPIO.OUT)




def forward(tf):
	GPIO.setup(40, GPIO.OUT)
	GPIO.output(7, False)
	GPIO.output(11, True)
	GPIO.output(13, True)
	GPIO.output(15, False)
	GPIO.output(40, GPIO.HIGH)
	time.sleep(tf)
	GPIO.cleanup()

	
def reverse(tf):
	GPIO.setup(38, GPIO.OUT)
	GPIO.output(40, GPIO.LOW)
	GPIO.output(7, True)
	GPIO.output(11, False)
	GPIO.output(13, False)
	GPIO.output(15, True)
	GPIO.output(38, GPIO.HIGH)
	time.sleep(tf)
	GPIO.cleanup()
	
def turn_left(tf):
	GPIO.setup(40, GPIO.OUT)
	GPIO.output(7, True)
	GPIO.output(11, True)
	GPIO.output(13, True)
	GPIO.output(15, False)
	GPIO.output(40, GPIO.HIGH)
	time.sleep(tf)
	GPIO.cleanup()

def turn_right(tf):
	GPIO.setup(40, GPIO.OUT)
	GPIO.output(7, False)
	GPIO.output(11, True)
	GPIO.output(13, False)
	GPIO.output(15, False)
	GPIO.output(40, GPIO.HIGH)	
	time.sleep(tf)
	GPIO.cleanup()

def pivot_left(tf):
	GPIO.setup(40, GPIO.OUT)
	GPIO.output(7, True)
	GPIO.output(11, False)
	GPIO.output(13, True)
	GPIO.output(15, False)
	GPIO.output(40, GPIO.HIGH)	
	time.sleep(tf)
	GPIO.cleanup()
	
def pivot_right(tf):
	GPIO.setup(40, GPIO.OUT)
	GPIO.output(7, False)
	GPIO.output(11, True)
	GPIO.output(13, False)
	GPIO.output(15, True)
	GPIO.output(40, GPIO.HIGH)	
	time.sleep(tf)
	GPIO.cleanup()

def camera_on():
	camera = PiCamera()
	camera.start_preview(fullscreen=False, window = (100,20,640,480))
	command = tk.Tk()
	command.bind('<KeyPress>',key_input)
	command.mainloop()
	sleep(60)
	camera.stop_preview()
	camera.close()
	#os.system("raspivid -o - -t 0 -hf -w 1080 -h 720 -fps 24 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8160}' :demux=h264")

	
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
		GPIO.output(12, False)
		forward(sleep_time)
	elif key_press.lower() == 's':
		GPIO.output(12, False)
		reverse(sleep_time)
	elif key_press.lower() == 'a':
		GPIO.output(12, False)
		turn_left(sleep_time)
	elif key_press.lower() == 'd':
		GPIO.output(12, False)
		turn_right(sleep_time)		
	elif key_press.lower() == 'q':
		GPIO.output(12, False)
		pivot_left(sleep_time)
	elif key_press.lower() == 'e':
		GPIO.output(12, False)
		pivot_right(sleep_time)	
	elif key_press.lower() == 'o':
		if current_duty+increment < 13:
			init()
			GPIO.output(7, GPIO.LOW)
			GPIO.output(11, GPIO.LOW)
			GPIO.output(13, GPIO.LOW)
			GPIO.output(15, GPIO.LOW)
			GPIO.output(40, GPIO.LOW) 
			p.ChangeDutyCycle(current_duty+increment)
			time.sleep(.03)
			GPIO.cleanup()
			current_duty = current_duty + increment
		
		else:
			init()
			GPIO.output(7, GPIO.LOW)
			GPIO.output(11, GPIO.LOW)
			GPIO.output(13, GPIO.LOW)
			GPIO.output(15, GPIO.LOW)
			GPIO.output(40, GPIO.LOW)
			p.ChangeDutyCycle(13)
			time.sleep(.03)
			GPIO.cleanup()
			current_duty = current_duty
		
	elif key_press.lower() == 'p':
		if current_duty-increment > 2.5: 
			init()
			GPIO.output(7, False)
			GPIO.output(11, False)
			GPIO.output(13, False)
			GPIO.output(15, False)
			GPIO.output(40, GPIO.LOW)
			p.ChangeDutyCycle(current_duty-increment)
			time.sleep(.03)
			GPIO.cleanup()
			current_duty = current_duty - increment
		else:
			init()
			GPIO.output(7, GPIO.LOW)
			GPIO.output(11, GPIO.LOW)
			GPIO.output(13, GPIO.LOW)
			GPIO.output(15, GPIO.LOW)
			GPIO.output(40, GPIO.LOW)
			p.ChangeDutyCycle(2.5)
			time.sleep(.03)
			GPIO.cleanup()
			current_duty = current_duty	
	elif key_press.lower() == 'l':
		init()
		GPIO.output(7, GPIO.LOW)
		GPIO.output(11, GPIO.LOW)
		GPIO.output(13, GPIO.LOW)
		GPIO.output(15, GPIO.LOW)
		GPIO.output(40, GPIO.LOW) 
		p.ChangeDutyCycle(7.5)
		time.sleep(.03)
		GPIO.cleanup()
		current_duty = 7.5
	elif key_press.lower() == 'i':
		init()
		GPIO.output(7, GPIO.LOW)
		GPIO.output(11, GPIO.LOW)
		GPIO.output(13, GPIO.LOW)
		GPIO.output(15, GPIO.LOW)
		GPIO.output(40, GPIO.LOW)
		camera_on()
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
