import sys
import base64
import re

##
## Author: Paul McDowell
##
## License: MIT
##


def parseAsNum(num:str): 
    if re.search(r'[^0-1\ ]', num) == None: # binary number of some kind.
        tmpSplit = num.split(' ')
        bArray = bytearray()
        for bNum in tmpSplit: # loops through binary character array to rebuild the ascii string
            bArray.append(int(bNum, 2))
        
        num = bArray.decode('utf-8')
        print('From binary: ' + num)
    if num.startswith("0x"): # hex encoded probably
        print('From Hex: ' + bytes.fromhex(num[2:]).decode('utf-8'))
    # detects a base64 pattern, but not guaranteed to actually BE base64.
    if re.search(r'^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$',num) != None:
        try: # maybe base64 ? looping through decode/encode and decode ascii will determine if it's valid
            if base64.b64encode(base64.b64decode(num)).decode('utf-8') == num: 
                print('From B64: ' + base64.b64decode(num).decode('utf-8'))
        except Exception:
            return

if len(sys.argv) != 2:
    raise ValueError("Please provide a single string-form number or binary array to convert as the only parameter.")

parseAsNum(sys.argv[1])