import RPi.GPIO as GPIO
import time 
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

while True:
	GPIO.output(3,GPIO.LOW)
	GPIO.output(5,GPIO.LOW)
	status = input("Semi-aut (0) or Discontinuity? (1)   :  ")
	
	if status == 0:
		GPIO.output(3,GPIO.HIGH)
		time.sleep(10)
	elif status == 1:
		GPIO.output(5,GPIO.HIGH)
		time.sleep(10)
	else:
		print("Pick 0 or 1")
