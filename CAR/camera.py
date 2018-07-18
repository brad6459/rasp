import RPi.GPIO as GPIO
import time
import sys
import Tkinter as tk
	
def left(current_duty,increment,servo):
	if current_duty+increment < 13: 
		init()
		p.ChangeDutyCycle(current_duty+increment)
		time.sleep(.03)
		GPIO.cleanup()
		current_duty = current_duty + increment
		print("%d ") %(current_duty)
	else:
		init()
		p.ChangeDutyCycle(13)
		time.sleep(.03)
		GPIO.cleanup()
		current_duty = current_duty
	return current_duty
	
		
def right(current_duty,increment,servo):
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
	return current_duty
	
	
def key_input(event):
	servo = 12
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(servo,GPIO.OUT)
	increment = .5
	
	print 'Key:', event.keysym
	key_press = event.keysym
	sleep_time = 0.03
	
	if key_press.lower() == 'r':
		print("key %d") %(current_duty)
		left(current_duty,increment,servo)
	elif key_press.lower() == 't':
		right(current_duty,increment,servo)
	else:
		GPIO.cleanup()

def init():
	servo = 12
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(servo,GPIO.OUT)
	p=GPIO.PWM(servo,50)# 50hz frequency

servo = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo,GPIO.OUT)
p=GPIO.PWM(servo,50)# 50hz frequency
p.start(7.5)
current_duty = 7.5		
command = tk.Tk()
command.bind('<KeyPress>',key_input)
command.mainloop()
