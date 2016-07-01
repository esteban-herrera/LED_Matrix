#!/usr/bin/python
import sys
import copy
from LED_Matrix_Display import *
from alphabet import *

# A string containing chars [A-Za-z]
stringToScroll = sys.argv[1]
# For best results a float between 0 and 1, 
howFast = float(sys.argv[2])
# The width of a letter bitmap, with this alphabet 6
howWide = int(sys.argv[3])
Display().setup()

def scrollString(string):
  string = string.lower()
  index = 0

  letter_bitmap = [0,0,0,0,0,0,0,0]
  #iterates through the string one char at a time
  while True:
    letter = string[index]
    # add the next letter to the first byte of each row
    for row in range(0,8):
      letter_bitmap[row] = letter_bitmap[row] ^ alpha[letter][row]

    for shift in range(0,howWide): # shift letter across view
      for i in range(0,len(letter_bitmap)):
        letter_bitmap[i] = letter_bitmap[i]<<1
      showBitmap(letter_bitmap, howFast)

    index+=1
    if index >= len(string):
      break

# display the second byte of bitmap 
# given 0xXXXXSSXX I want 0x000000SS
# done by masking with 0x0000FF00 and shifting 8 right
def showBitmap(bitmap, showFor):
    frames_per_second = 50
    for n in range(0, int(showFor*frames_per_second)):
      for row in range(0,len(bitmap)):
        Display.set_anodes( 1<<row )
        Display.set_cathodes( (bitmap[row] & 0xFF00)>>8 )
        time.sleep(1.0/(len(bitmap)*frames_per_second))

scrollString(stringToScroll)

