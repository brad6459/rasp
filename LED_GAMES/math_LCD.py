## INSTRUCTIONS
	#In order to have led incorporated to the game, connect pins 
	#23(RIGHT ANSWER) and 12 (RIGHT ANSWER)

#Import libraries that we need
from gpiozero import LED
import time
import random
import math 
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime
 
#Select default play to 1 (YES)
play = 1 
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
mcp = PCF8574_GPIO(PCF8574_address)

# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

while play == 1:
	#Create LCD
	lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db = [4,5,6,7], GPIO=mcp)
	#turn on LCD backlight 
	mcp.output(3,1)
	lcd.begin(16,2) #set lcd lines and columns
	lcd.setCursor(0,0) #set cursor position
	
	lcd.message('Let\'s play!')
	for i in range(16):
		lcd.scrollDisplayRight()
		time.sleep(.1)
	for i in range(16):
		lcd.DisplayLeft()
		time.sleep(.1)
		
	
	#Allow user to pick a category 
	print 'Select one: \n 1) Addition \n 2) Subtraction \n 3) Multiplication'
	selection = 1.11
	while selection <0 or selection > 4 or selection == 1.11:
		selection = input("Which one do you want to play? Pick a number between 1-3:")
	
	#Allow the user to pick a difficulty 
	print 'Select a difficulty: 1) EASY 2) MEDIUM 3) HARD'
	difficulty = 1.11
	while difficulty < 0 or difficulty > 4 or difficulty == 1.11:
		difficulty = input("Difficulty Desired: ") 
	
	#Allow the user to select the number of questions they wanna answer
	num_questions = input("How many questions do you want? :")
		
		
	#Select the range based on difficulty
	if difficulty  == 1:
		num_range = 5
	elif difficulty == 2:
		num_range = 10
	else: 
		num_range = 20


	counter = 0 #Counter of questions starts at 0
	right_tally = 0 #Questions answered correctly
	
	#-------------------ADDITION------------------------------------#
	
	if  selection == 1:

			while counter < num_questions:
				num1 = random.randint(0,num_range)
				num2 = random.randint(0,num_range)
				print("%d + %d = ") %(num1,num2)
				lcd.clear()
				lcd.setCursor(0,0)
				lcd.message("{} + {} =".format(num1,num2))
				answer = num1 + num2
				user_answer = input("Your Answer:")
				if answer == user_answer:
#					led = LED(23)
#					led.on()
#					time.sleep(1)
#					led.off()
					right_tally= right_tally + 1
#				else:
#					led = LED(12)
#					led.on()
#					time.sleep(1)
#					led.off()
					
#				del led
				counter = counter + 1
					 
				

	#-------------------SUBTRACTION---------------------------------#		
	elif selection ==2:
			while counter < num_questions:
				num1 = random.randint(0,num_range)
				num2 = random.randint(0,num_range)
				print("%d - %d = ") %(num1,num2)
				answer = num1 - num2
				user_answer = input("Your Answer:")
				if answer == user_answer:
#					led = LED(23)
#					led.on()
#					time.sleep(1)
#					led.off()
					right_tally = right_tally + 1
					
#				else:
#					led = LED(12)
#					led.on()
#					time.sleep(1)
#					led.off()
					
#				del led
				counter = counter + 1
							
	#----------------------Multiplication------------------------------#	
	elif selection ==3:
		while counter < num_questions:
				num1 = random.randint(0,num_range)
				num2 = random.randint(0,num_range)
				print("%d * %d = ") %(num1,num2)
				answer = num1 * num2
				user_answer = input("Your Answer:")
				if answer == user_answer:
#					led = LED(23)
#					led.on()
#					time.sleep(1)
#					led.off()
					right_tally = right_tally + 1
#				else:
#					led = LED(12)
#					led.on()
#					time.sleep(1)
#					led.off()
					
#				del led
				counter = counter + 1
	
	#TELL THE USER  HOW THEY DID
	print("You answered %d/%d questions correctly\n") %(right_tally,num_questions)
	
	#ASK THE USER IF THEY WANNA PLAY AGAIN
	print 'Do you want to keep playing?. TYPE 1 for yes or anything else for no'
	play = input("Choice:")
	
	if play == 1:
		print "\nLet's play again"
	else:
		print "\nGood game. Play again Next time!"
		

	
