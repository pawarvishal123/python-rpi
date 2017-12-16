import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()
print(mode)
#GPIO.cleanup()
print("Start")
Forward1=38
Backward1=37
Forward2=36
Backward2=35
sleeptime=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward1, GPIO.OUT)
GPIO.setup(Backward1, GPIO.OUT)
GPIO.setup(Forward2, GPIO.OUT)
GPIO.setup(Backward2, GPIO.OUT)
def forward(x):
    GPIO.output(Forward1, GPIO.HIGH)
    GPIO.output(Forward2, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Forward1, GPIO.LOW)
    GPIO.output(Forward2, GPIO.LOW)

def reverse(x):
    GPIO.output(Backward1, GPIO.HIGH)
    GPIO.output(Backward2, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(Backward1, GPIO.LOW)
    GPIO.output(Backward2, GPIO.LOW)

#try:
#while (1):
print("try forward")
forward(sleeptime)
print("try reverse")
reverse(sleeptime)
#except:
#    print("Some error")#
GPIO.cleanup()
