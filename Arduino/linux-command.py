import RPi.GPIO as GPIO
import time
import sys
import Tkinter as tk
from picamera import PiCamera
import os 
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)


GPIO.output(5,GPIO.LOW)
time.sleep(30)
GPIO.output(5,GPIO.HIGH)
GPIO.output(5,GPIO.LOW)
