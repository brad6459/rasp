from gpiozero import LED
import time
import random
import math 

a = 1
counter = 0
K = input("Time to alternate:")
while (a == 1): 

	led = LED(23)
	led.on()
	time.sleep(K)
	led.off()
	del led

	led = LED(18)
	led.on()
	time.sleep(K)
	led.off()
	del led
	
	led = LED(22)
	led.on()
	time.sleep(K)
	led.off()
	del led
	
		
	led = LED(17)
	led.on()
	time.sleep(K)
	led.off()
	del led
		
	led = LED(6)
	led.on()
	time.sleep(K)
	led.off()
	del led
	
	led = LED(19)
	led.on()
	time.sleep(K)
	led.off()
	del led
	
	led = LED(12)
	led.on()
	time.sleep(K)
	led.off()
	del led
	
	led = LED(21)
	led.on()
	time.sleep(K)
	led.off()
	del led
	
	
	led = LED(16)
	led.on()
	time.sleep(K)
	led.off()
	del led
	
	K = K - .1
	if K > 0: 
		K = K 
	else:
		K = .01
			
	
