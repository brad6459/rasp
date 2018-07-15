import RPi.GPIO as GPIO
import time
import sys
import Tkinter as tk

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
	
def key_input(event):
	init()
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
	else:
		GPIO.cleanup()
		
command = tk.Tk()
command.bind('<KeyPress>',key_input)
command.mainloop()
