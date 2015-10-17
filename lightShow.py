#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

#pinList = [2, 3, 4, 17, 27, 22, 10, 9]
# init list with pin numbers

R1=10
R2=2
R3=3
R4=4
R5=25
R6=22
R7=17
R8=18
pinList = [R1,R2,R3,R4,R5,R6,R7,R8]

SleepTimeL = .1

def allOff():
	for i in pinList: 
		print 'turning off: ' + str(i)
		GPIO.setup(i, GPIO.OUT) 
		GPIO.output(i, GPIO.HIGH)
		
def allOn():
	for i in pinList: 
		print 'turning on: ' + str(i) 
		GPIO.output(i, GPIO.OUT)		
	
def getInput():
    inpt = raw_input(":")
    return inpt

def leftToright():
	for r in range(0, len(pinList)):
		print "relay: " + str(r+1)
		GPIO.output(pinList[r], GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(pinList[r], GPIO.HIGH)
	return
	
def rightToLeft():
	for rt in range(len(pinList)-1, 0, -1):
		print "relay: " + str(rt+1)
		GPIO.output(pinList[rt], GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(pinList[rt], GPIO.HIGH)
	return
	
def blink():
	for delay in range(4):
		allOff();
		time.sleep(1)
		allOn()
		time.sleep(.5)
	return

allOff()

# main loop

try:
	leftToright()
	rightToLeft()
	blink()
	time.sleep(3)
	print "Good bye!"
	time.sleep(4)
	GPIO.cleanup()

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/oaf_zQcrg7g