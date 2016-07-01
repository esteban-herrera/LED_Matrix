import RPi.GPIO as GPIO  
import time  

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  

out = {"c0":19, "c1":23, "c2":32, "c3":33, "a0":38, "a1":40, "a2":15, "a3":16}

# set all as output
for k in out.keys():
  GPIO.setup(out[k], GPIO.OUT)

def set_cathodes(byte):
  GPIO.output(out["c3"], GPIO.HIGH if byte & 0x01 == 0x01 else GPIO.LOW ) 
  GPIO.output(out["c2"], GPIO.HIGH if byte & 0x02 == 0x02 else GPIO.LOW ) 
  GPIO.output(out["c1"], GPIO.HIGH if byte & 0x04 == 0x04 else GPIO.LOW ) 
  GPIO.output(out["c0"], GPIO.HIGH if byte & 0x08 == 0x08 else GPIO.LOW ) 

def set_anodes(byte):
  GPIO.output(out["a0"], GPIO.HIGH if byte & 0x01 == 0x01 else GPIO.LOW ) 
  GPIO.output(out["a1"], GPIO.HIGH if byte & 0x02 == 0x02 else GPIO.LOW ) 
  GPIO.output(out["a2"], GPIO.HIGH if byte & 0x04 == 0x04 else GPIO.LOW ) 
  GPIO.output(out["a3"], GPIO.HIGH if byte & 0x08 == 0x08 else GPIO.LOW ) 

movie = [ 
    [0b1001,0b1111,0b1001,0b1001],
    [0b1111,0b1001,0b1001,0b1111],
    [0b1000,0b1000,0b1000,0b1111],
    [0b1111,0b1001,0b1111,0b1001]
  ]

# given something like [0b0010, 0b1111, 0b0000, 0b1001]
def showBitmap(bitmap, showFor):
  frames_per_second = 50
  for n in range(0, int(showFor*frames_per_second)):
    for row in range(0,len(bitmap)): # 0 based
      set_anodes( 1<<row )
      set_cathodes( ~bitmap[row] )
      time.sleep(1.0/(len(bitmap)*frames_per_second))   

def showAnimation(movie):
  for bitmap in movie:
    showBitmap(bitmap, 1)

showAnimation(movie)    

#for i in range(100000):
#  showFrame([
#    0b1000, 
#    0b0100,
#    0b0010,
#    0b0001
#  ])


