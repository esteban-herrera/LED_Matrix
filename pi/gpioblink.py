import RPi.GPIO as GPIO  
import time  
# blinking function  
def blink(pin):  
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(.5)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(.5)  
        return  
# to use Raspberry Pi board pin numbers  
GPIO.setmode(GPIO.BOARD)  
# set up GPIO output channel  
GPIO.setup(3, GPIO.OUT)  
# blink GPIO17 50 times  
for i in range(0,50):  
        blink(3)  
GPIO.cleanup() 
