import RPi.GPIO as GPIO  
import time  

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  

out = {"c0":11, "c1":36, "c2":10, "c3":8, "c4":33, "c5":32, "c6":23, "c7":19, \
       "a0":13, "a1":37, "a2":22, "a3":18, "a4":16, "a5":15, "a6":40, "a7":38}

# set all as output
for k in out.keys():
  GPIO.setup(out[k], GPIO.OUT)

# for cathodes/columns set to 0 to turn on
def set_cathodes(byte):
# GPIO.output(out["c0"], GPIO.HIGH if byte & 0x01 == 0x01 else GPIO.LOW ) 
  GPIO.output(out["c0"], 0 if byte & 128 == 128 else 1) # col 0 
  GPIO.output(out["c1"], 0 if byte & 064 == 064 else 1) # col 1
  GPIO.output(out["c2"], 0 if byte & 032 == 032 else 1) # col 2
  GPIO.output(out["c3"], 0 if byte & 016 == 016 else 1) # col 3
  GPIO.output(out["c4"], 0 if byte & 008 == 008 else 1) # col 4
  GPIO.output(out["c5"], 0 if byte & 004 == 004 else 1) # col 5
  GPIO.output(out["c6"], 0 if byte & 002 == 002 else 1) # col 6
  GPIO.output(out["c7"], 0 if byte & 001 == 001 else 1) # col 7

# for anodes/rows set to 1 to turn on
def set_anodes():
# GPIO.output(out["a0"], GPIO.HIGH if byte & 0x01 == 0x01 else GPIO.LOW ) 
  GPIO.output(out["a0"], 1 if byte & 001 == 001 else 0) # row 0
  GPIO.output(out["a1"], 1 if byte & 002 == 002 else 0) # row 1
  GPIO.output(out["a2"], 1 if byte & 004 == 004 else 0) # row 2
  GPIO.output(out["a3"], 1 if byte & 008 == 008 else 0) # row 3
  GPIO.output(out["a4"], 1 if byte & 016 == 016 else 0) # row 4
  GPIO.output(out["a5"], 1 if byte & 032 == 032 else 0) # row 5
  GPIO.output(out["a6"], 1 if byte & 064 == 064 else 0) # row 6
  GPIO.output(out["a7"], 1 if byte & 128 == 128 else 0) # row 7

def showBitmap(bitmap, showFor)
  frames_per_second = 50
  for n in range(0, int(showFor*frames_per_second)):
    for row in range(0,len(bitmap)):
      set_anodes( 1<<row )
      set_cathodes( ~bitmap[row] )
      time.sleep(1.0/(len(bitmap)*frames_per_second))

def showAnimation(movie)
  for bitmap in movie:
    showBitmap(bitmap, 1)

showAnimation(movie)
