import RPi.GPIO as GPIO  
import time  

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)  

GPIO.setup(15, GPIO.OUT)  
GPIO.setup(16, GPIO.OUT)  
GPIO.setup(18, GPIO.OUT)  
GPIO.setup(22, GPIO.OUT)  

for i in range(0,50):
  GPIO.output(15,GPIO.HIGH) # BROWN  
  GPIO.output(16,GPIO.LOW) # RED
  GPIO.output(18,GPIO.LOW)  # ORANGE
  GPIO.output(22,GPIO.HIGH)  # YELLOW
  time.sleep(.1)
  GPIO.output(15,GPIO.HIGH) # BROWN  
  GPIO.output(16,GPIO.LOW) # RED
  GPIO.output(18,GPIO.HIGH)  # ORANGE
  GPIO.output(22,GPIO.LOW)  # YELLOW
  time.sleep(.1)
  GPIO.output(15,GPIO.LOW) # BROWN  
  GPIO.output(16,GPIO.HIGH) # RED
  GPIO.output(18,GPIO.HIGH)  # ORANGE
  GPIO.output(22,GPIO.LOW)  # YELLOW
  time.sleep(.1)
  GPIO.output(15,GPIO.LOW) # BROWN  
  GPIO.output(16,GPIO.HIGH) # RED
  GPIO.output(18,GPIO.LOW)  # ORANGE
  GPIO.output(22,GPIO.HIGH)  # YELLOW
  time.sleep(.1)
