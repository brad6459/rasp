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

GPIO.output(3,GPIO.LOW)
time.sleep(5)
GPIO.output(3,GPIO.HIGH)
