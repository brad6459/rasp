#________________________INSTRUCTIONS___________________________________
#FOR LED:
	#In order to have led incorporated to the game, connect pins 
	#23(RIGHT ANSWER) and 12 (WRONG ANSWER)
#FOR LCD:
	# Connect LCD as such:
	#top wire: ground
	#wire2: 5V
	#wire3: SDA1
	#bottom wire: SCL1
#_______________________________________________________________________	
	
#Import libraries 
from gpiozero import LED
import time
import random
import math 
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime
 
 
def setup():
	#Select default play to 1 (YES)
	global play
	play = 1 
	return play

def game(play):
	while play == 1: #Will continue the game until play again is selected
		
		#########################SET UP LCD#############################
		PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
		PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
		
		# Create PCF8574 GPIO adapter.
		mcp = PCF8574_GPIO(PCF8574_address)
		
		# Create LCD, passing in MCP GPIO adapter.
		lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7],
		GPIO=mcp)
		
		#turn on LCD backlight 
		mcp.output(3,1)
		lcd.begin(16,2) #set lcd lines and columns
		lcd.setCursor(0,0) #set cursor position
		
		lcd.message('Let\'s Play, \n Math Time!')
		
		for i in range(16):
			lcd.scrollDisplayRight()
			time.sleep(.1)
		for i in range(16):
			lcd.DisplayLeft()
			time.sleep(.1)
		################################################################	
		
		#Allow user to pick a category
		selection = 1.11
		while selection <0 or selection >3 or selection == 1.11:
		#print 'Select one: \n 1) Addition \n 2) Subtraction \n 3) Multiplication'
			lcd.clear()
			lcd.setCursor(0,0)
			lcd.message('1.Add 2.Subtract \n 3.Multiply :')
			selection = input("Which one do you want to play? Pick a number between 1-3:")
			lcd.message('{}'.format(selection))	
			time.sleep(1)
							
		#Allow the user to pick a difficulty 
		#print 'Select a difficulty: 1) EASY 2) MEDIUM 3) HARD'
		difficulty = 1.11
		while difficulty < 0 or difficulty > 3 or difficulty == 1.11:
			lcd.clear()
			lcd.setCursor(0,0)
			lcd.message('Difficulty:')
			difficulty = input("Difficulty Desired: ") 
			lcd.message('{}'.format(difficulty))
			time.sleep(1)
		#Allow the user to select the number of questions they wanna answer
		lcd.clear()
		lcd.setCursor(0,0)
		lcd.message('Questions \n Desired:')
		num_questions = input("How many questions do you want? :")
		lcd.message('{}'.format(num_questions))	
		time.sleep(1)
			
		#Select the range based on difficulty
		if difficulty  == 1:
			num_range = 10
		elif difficulty == 2:
			num_range = 15
		else: 
			num_range = 100


		counter = 0 #Counter of questions starts at 0
		right_tally = 0 #Questions answered correctly
		
		#-------------------ADDITION------------------------------------#
		
		if  selection == 1:

				while counter < num_questions:
					num1 = random.randint(0,num_range)
					num2 = random.randint(0,num_range)
					#print("%d + %d = ") %(num1,num2)
					lcd.clear()
					lcd.setCursor(0,0)
					lcd.message("{} + {} =".format(num1,num2))
					answer = num1 + num2
					user_answer = input("Your Answer:")
					lcd.message("{}".format(user_answer))
					if answer == user_answer:
						led = LED(23)
						led.on()
						time.sleep(1)
						led.off()
						right_tally= right_tally + 1
					else:
						led = LED(12)
						led.on()
						time.sleep(1)
						led.off()
						
					del led
					counter = counter + 1
						 
					

		#-------------------SUBTRACTION---------------------------------#		
		elif selection ==2:
				while counter < num_questions:
					num1 = random.randint(0,num_range)
					num2 = random.randint(0,num_range)
					#print("%d - %d = ") %(num1,num2)
					lcd.clear()
					lcd.setCursor(0,0)
					lcd.message("{} - {} =".format(num1,num2))
					answer = num1 - num2
					user_answer = input("Your Answer:")
					lcd.message("{}".format(user_answer))
					
					if answer == user_answer:
						led = LED(23)
						led.on()
						time.sleep(1)
						led.off()
						right_tally = right_tally + 1
						
					else:
						led = LED(12)
						led.on()
						time.sleep(1)
						led.off()
						
					del led
					counter = counter + 1
								
		#----------------------Multiplication------------------------------#	
		elif selection ==3:
			while counter < num_questions:
					num1 = random.randint(0,num_range)
					num2 = random.randint(0,num_range)
					#print("%d * %d = ") %(num1,num2)
					lcd.clear()
					lcd.setCursor(0,0)
					lcd.message("{} * {} =".format(num1,num2))
					answer = num1 * num2
					user_answer = input("Your Answer:")
					lcd.message("{}".format(user_answer))
					if answer == user_answer:
						led = LED(23)
						led.on()
						time.sleep(1)
						led.off()
						right_tally = right_tally + 1
					else:
						led = LED(12)
						led.on()
						time.sleep(1)
						led.off()
						
					del led
					counter = counter + 1
		
		#TELL THE USER  HOW THEY DID
		print("You answered %d/%d questions correctly\n") %(right_tally,num_questions)
		lcd.clear()
		lcd.setCursor(0,0)
		lcd.message("Result: {}/{}".format(right_tally,num_questions))
		time.sleep(3)
		#ASK THE USER IF THEY WANNA PLAY AGAIN
		#print 'Do you want to keep playing?. TYPE 1 for yes or anything else for no'
		lcd.clear()
		lcd.setCursor(0,0)
		lcd.message('Play Again? \n 1.YES 2.NO  :')
		play = input("Choice:")
		
		if play == 1:
			lcd.clear()
			lcd.setCursor(0,0)
			lcd.message('Playing \n Again!')
			time.sleep(1)
			#print "\nLet's play again"
		else:
			#print "\nGood game. Play again Next time!"
			lcd.clear()
			lcd.setCursor(0,0)
			lcd.message("Play Again \n Next Time!")
			time.sleep(1)
			destroy()
	return 
			
# FUNCTION WILL STOP THE PROGRAM WHEN CALLED FOR
def destroy():
	PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
	PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
	# Create PCF8574 GPIO adapter.
	mcp = PCF8574_GPIO(PCF8574_address)
	# Create LCD, passing in MCP GPIO adapter.
	lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
	lcd.clear() #Clear the LCD when game is exited


# STARTS HERE
if __name__ == '__main__':
	setup()
	
	try:
		#Start the game
		game(play)
	
	except KeyboardInterrupt:
	    destroy()

