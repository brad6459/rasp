from gpiozero import LED
import time
K = input("Sleep for: ")
led = LED(18)

while True: 
	led.toggle()
	time.sleep(K)
	led.toggle()
	time.sleep(K)