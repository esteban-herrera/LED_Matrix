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

delay=1.0/1

frames = [ 
    [0b0001,0b0000,0b0000,0b0000],
    [0b0010,0b0000,0b0000,0b0000],
    [0b0100,0b0000,0b0000,0b0000],
    [0b1000,0b0000,0b0000,0b0000],
    [0b0000,0b0100,0b0000,0b0000],
    [0b0000,0b0000,0b0010,0b0000],
    [0b0000,0b0000,0b0000,0b1000],
    [0b0000,0b0000,0b0000,0b0100],
    [0b0000,0b0000,0b0000,0b0010],
    [0b0000,0b0000,0b0000,0b0001],
    [0b0000,0b0000,0b0100,0b0000],
    [0b0000,0b0010,0b0000,0b0000]
  ]

def readFrames(frameSet):
  for frame in frameSet:
    for n in range(4):
      set_cathodes(0)
      nibble = frame[n]
      set_anodes(nibble)
  time.sleep(delay)

# given something like [0b0010, 0b1111, 0b0000, 0b1001]
def showFrame(frame):
  for row in range(0,len(frame)): # 0 based
    print row

def turnOnLight(row, column):
  rowMask = 0b1<<(row-1)
  set_anodes(rowMask)
  colMask = ~(0b1<<(column-1))
  set_cathodes(colMask)

def drawPoint(row, col):
  turnOnLight(row, col)
  time.sleep(0.1)

def drawBowtie():
  drawPoint(1,1)
  drawPoint(2,1)
  drawPoint(3,1)
  drawPoint(4,1)
  drawPoint(3,2)
  drawPoint(2,3)
  drawPoint(1,4)
  drawPoint(2,4)
  drawPoint(3,4)
  drawPoint(4,4)
  drawPoint(3,3)
  drawPoint(2,2)
  
for a in range(10000):
  drawBowtie()
