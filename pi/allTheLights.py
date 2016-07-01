import RPi.GPIO as GPIO  
import time  

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  

out = {"c0":11, "c1":36, "c2":10, "c3":8, "c4":33, "c5":32, "c6":23, "c7":19, \
       "a0":13, "a1":37, "a2":22, "a3":18, "a4":16, "a5":15, "a6":40, "a7":38}

# set all as output
for k in out.keys():
  GPIO.setup(out[k], GPIO.OUT)

# Columns
def set_cathodes(byte):
  GPIO.output(out["c7"], GPIO.HIGH if byte & 0x01 == 0x01 else GPIO.LOW )  #00000001
  GPIO.output(out["c6"], GPIO.HIGH if byte & 0x02 == 0x02 else GPIO.LOW )  #00000010
  GPIO.output(out["c5"], GPIO.HIGH if byte & 0x04 == 0x04 else GPIO.LOW )  #00000100
  GPIO.output(out["c4"], GPIO.HIGH if byte & 0x08 == 0x08 else GPIO.LOW )  #00001000
  GPIO.output(out["c3"], GPIO.HIGH if byte & 0x16 == 0x16 else GPIO.LOW )  #00010000
  GPIO.output(out["c2"], GPIO.HIGH if byte & 0x32 == 0x32 else GPIO.LOW )  #00100000
  GPIO.output(out["c1"], GPIO.HIGH if byte & 0x64 == 0x64 else GPIO.LOW )  #01000000
  GPIO.output(out["c0"], GPIO.HIGH if byte & 0x128 == 0x128 else GPIO.LOW )#10000000 

# Rows
def set_anodes(byte):
  GPIO.output(out["a0"], GPIO.HIGH if byte & 0x01 == 0x01 else GPIO.LOW )  #00000001
  GPIO.output(out["a1"], GPIO.HIGH if byte & 0x02 == 0x02 else GPIO.LOW )  #00000010
  GPIO.output(out["a2"], GPIO.HIGH if byte & 0x04 == 0x04 else GPIO.LOW )  #00000100
  GPIO.output(out["a3"], GPIO.HIGH if byte & 0x08 == 0x08 else GPIO.LOW )  #00001000
  GPIO.output(out["a4"], GPIO.HIGH if byte & 0x16 == 0x16 else GPIO.LOW )  #00010000
  GPIO.output(out["a5"], GPIO.HIGH if byte & 0x32 == 0x32 else GPIO.LOW )  #00100000
  GPIO.output(out["a6"], GPIO.HIGH if byte & 0x64 == 0x64 else GPIO.LOW )  #01000000
  GPIO.output(out["a7"], GPIO.HIGH if byte & 0x128 == 0x128 else GPIO.LOW )#10000000

movie = [ 
    [0b10000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000]
#    [0b1111,0b1001,0b1001,0b1111],
#    [0b1000,0b1000,0b1000,0b1111],
#    [0b1111,0b1001,0b1111,0b1001]
  ]

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

#showAnimation(movie)
#set_cathodes(0b11111111)
#set_anodes(0b00000000)
#GPIO.output(19,0)
#GPIO.output(38,1)
