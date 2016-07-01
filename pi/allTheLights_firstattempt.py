import RPi.GPIO as GPIO  
import time  

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  

out = {"c0":11, "c1":36, "c2":10, "c3":8, "c4":33, "c5":32, "c6":23, "c7":19 ,\
       "r0":13, "r1":37, "r2":22, "r3":18, "r4":16, "r5":15, "r6":40, "r7":38}

# set all as output
for k in out.keys():
  GPIO.setup(out[k], GPIO.OUT)

# TODO: Change this function to refer to columns rather than bytes
def set_cathodes(byte):
  GPIO.output(out["c0"], 1 if byte & 0x128 == 0x128 else 0 )
  GPIO.output(out["c1"], 1 if byte & 0x64 == 0x64 else 0 ) 
  GPIO.output(out["c2"], 1 if byte & 0x32 == 0x32 else 0 ) 
  GPIO.output(out["c3"], 1 if byte & 0x16 == 0x16 else 0 ) 
  GPIO.output(out["c4"], 1 if byte & 0x08 == 0x08 else 0 ) 
  GPIO.output(out["c5"], 1 if byte & 0x04 == 0x04 else 0 ) 
  GPIO.output(out["c6"], 1 if byte & 0x02 == 0x02 else 0 ) 
  GPIO.output(out["c7"], 1 if byte & 0x01 == 0x01 else 0 ) 

# TODO: Change this function to refer to rows rather than bytes
def set_anodes(byte):
  GPIO.output(out["r0"], 1 if byte & 0x01 == 0x01 else 0 ) 
  GPIO.output(out["r1"], 1 if byte & 0x02 == 0x02 else 0 ) 
  GPIO.output(out["r2"], 1 if byte & 0x04 == 0x04 else 0 ) 
  GPIO.output(out["r3"], 1 if byte & 0x08 == 0x08 else 0 ) 
  GPIO.output(out["r4"], 1 if byte & 0x16 == 0x16 else 0 ) 
  GPIO.output(out["r5"], 1 if byte & 0x32 == 0x32 else 0 ) 
  GPIO.output(out["r6"], 1 if byte & 0x64 == 0x64 else 0 ) 
  GPIO.output(out["r7"], 1 if byte & 0x128 == 0x128 else 0 ) 

movie = [ 
    [0b10001010,0b10001010,0b10001010,0b11111001,0b10001001,0b10001001,0b10001010,0b10001010],
    [0b10001000,0b10001000,0b10001000,0b11111000,0b10001000,0b10001000,0b10001000,0b10001000],
    [0b10001000,0b10001000,0b10001000,0b11111000,0b10001000,0b10001000,0b10001000,0b10001000],
    [0b10001000,0b10001000,0b10001000,0b11111000,0b10001000,0b10001000,0b10001000,0b10001000],
    [0b10001000,0b10001000,0b10001000,0b11111000,0b10001000,0b10001000,0b10001000,0b10001000],
    [0b10001000,0b10001000,0b10001000,0b11111000,0b10001000,0b10001000,0b10001000,0b10001000],
    [0b10001000,0b10001000,0b10001000,0b11111000,0b10001000,0b10001000,0b10001000,0b10001000]
  ]

def showBitmap(bitmap, showFor):
  frames_per_second = 50
  for n in range(0, int(showFor*frames_per_second)):
    for row in range(0,len(bitmap)): # 0 based
      anodeToSet = 1<<row
      print anodeToSet
      set_anodes( anodeToSet )
      set_cathodes( ~bitmap[row] )
      time.sleep(1.0/(len(bitmap)*frames_per_second))   

def showAnimation(movie):
  for bitmap in movie:
    showBitmap(bitmap, 1)

showAnimation(movie)
