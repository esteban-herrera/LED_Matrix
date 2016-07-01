import RPi.GPIO as GPIO  
import time  

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  

out = {"c0":19, "c1":23, "c2":32, "c3":33, "a0":38, "a1":40, "a2":15, "a3":16}

# set all as output
for k in out.keys():
  GPIO.setup(out[k], GPIO.OUT)

def set_cathodes(byte):
  GPIO.output(out["c0"], GPIO.HIGH if byte & 0x01 == 0x01 else GPIO.LOW ) 
  GPIO.output(out["c1"], GPIO.HIGH if byte & 0x02 == 0x02 else GPIO.LOW ) 
  GPIO.output(out["c2"], GPIO.HIGH if byte & 0x04 == 0x04 else GPIO.LOW ) 
  GPIO.output(out["c3"], GPIO.HIGH if byte & 0x08 == 0x08 else GPIO.LOW ) 

def set_anodes(byte):
  GPIO.output(out["a0"], GPIO.HIGH if byte & 0x01 == 0x01 else GPIO.LOW ) 
  GPIO.output(out["a1"], GPIO.HIGH if byte & 0x02 == 0x02 else GPIO.LOW ) 
  GPIO.output(out["a2"], GPIO.HIGH if byte & 0x04 == 0x04 else GPIO.LOW ) 
  GPIO.output(out["a3"], GPIO.HIGH if byte & 0x08 == 0x08 else GPIO.LOW ) 

#set_cathodes(0x00)
#set_anodes(0x0f)
#time.sleep(1)

delay=0.0001
for c in range(0,100000):
  set_cathodes(0b11111110)
  set_anodes(0b00000001)
  time.sleep(delay)
  set_cathodes(0b11111101)
  set_anodes(0b00000010)
  time.sleep(delay)
  set_cathodes(0b11111011)
  set_anodes(0b00000100)
  time.sleep(delay)
  set_cathodes(0b11110111)
  set_anodes(0b00001000)
  time.sleep(delay)

  set_cathodes(0b11111110)
  set_anodes(0b00001000)
  time.sleep(delay)
  set_cathodes(0b1111101)
  set_anodes(0b00000100)
  time.sleep(delay)
  set_cathodes(0b11111011)
  set_anodes(0b00000010)
  time.sleep(delay)
  set_cathodes(0b11110111)
  set_anodes(0b00000001)
  time.sleep(delay)

