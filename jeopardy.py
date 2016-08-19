import RPi.GPIO as GPIO
import getpass
import sys
import telnetlib
import time

ip =  "192.168.0.110"

def telnet ( str ):
	tn = telnetlib.Telnet( str )
	tn.read_until("Please input username and password!")
	tn.write("admin=admin\n")
	tn.read_until("Username and password is ok!")
	return tn
	
telnet( ip )

GPIO.setmode ( GPIO.BCM )
GPIO.setup ( 4 , GPIO.IN , pull_up_down=GPIO.PUD_UP )
GPIO.setup ( 18 , GPIO.IN , pull_up_down=GPIO.PUD_UP )
GPIO.setup ( 22 , GPIO.IN , pull_up_down=GPIO.PUD_UP )
GPIO.setup ( 23 , GPIO.IN , pull_up_down=GPIO.PUD_UP )
GPIO.setup ( 25 , GPIO.IN , pull_up_down=GPIO.PUD_UP )

winner = False
button_1 = False
button_2 = False
button_3 = False
button_4 = False
while True:
	while True:
		if ((GPIO.input ( 18 ) == GPIO.LOW) & (GPIO.input ( 4 ) == GPIO.LOW) & (GPIO.input ( 22 ) == GPIO.LOW) & (GPIO.input ( 23 ) == GPIO.LOW) & (winner == False)):
			tn = telnet(ip)
			tn.write("setpower=11110000\n")
			time.sleep(.1)
			winner = False
			break
		if ((GPIO.input ( 18 ) == GPIO.LOW) & (GPIO.input ( 25 ) == GPIO.HIGH) & (winner == False) & (button_1 == False)):
			tn = telnet(ip)
			tn.write("setpower=00100000\n")
			time.sleep(.1)
			winner = True
			button_1 = True
			break
		if ((GPIO.input ( 18 ) == GPIO.HIGH)):
			button_1 = False
			

		if ((GPIO.input ( 4 ) == GPIO.LOW) & (GPIO.input ( 25 ) == GPIO.HIGH) & (winner == False) & (button_2 == False)):
			tn = telnet(ip)
			tn.write("setpower=00010000\n")
			time.sleep(.1)
			winner = True
			button_2 = True
			break
		if ((GPIO.input ( 4 ) == GPIO.HIGH)):
			button_2 = False
			
		
		if ((GPIO.input ( 22 ) == GPIO.LOW) & (GPIO.input ( 25 ) == GPIO.HIGH) & (winner == False) & (button_3 == False)):
			tn = telnet(ip)
			tn.write("setpower=01000000\n")
			time.sleep(.1)
			winner = True			
			button_3 = True
			break
		if ((GPIO.input ( 22 ) == GPIO.HIGH)):
			button_3 = False
			

		if ((GPIO.input ( 23 ) == GPIO.LOW) & (GPIO.input ( 25 ) == GPIO.HIGH) & (winner == False) & (button_4 == False)):
			tn = telnet(ip)
			tn.write("setpower=10000000\n")
			time.sleep(.1)
			winner = True			
			button_4 = True
			break
		if ((GPIO.input ( 23 ) == GPIO.HIGH)):
			button_4 = False
			

		if GPIO.input ( 25 ) == GPIO.LOW:
			tn = telnet(ip)
			tn.write("setpower=00000000\n")
			time.sleep(.1)
			winner = False
			button_1 = True
			button_2 = True
			button_3 = True
			button_4 = True
			break
