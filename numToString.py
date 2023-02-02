import sys
import base64
import re

def parseAsNum(num:str): 
    if re.search(r'[^0-1\ ]', num) == None: # binary
        tmpSplit = num.split(' ')
        bArray = bytearray()
        for bNum in tmpSplit:
            bArray.append(int(bNum, 2))
        
        num = bArray.decode('utf-8')
        print('From binary: ' + num)
    if num.startswith("0x"): # hex encoded probably
        print('From Hex: ' + bytes.fromhex(num[2:]).decode('utf-8'))
    
    if re.search(r'^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$',num) != None:
        try:
            if base64.b64encode(base64.b64decode(num)).decode('utf-8') == num: 
                # maybe base64 ?
                print('From B64: ' + base64.b64decode(num).decode('utf-8'))
        except Exception:
            return
    else:
        print('Post processed guess: ' + num)

if len(sys.argv) < 2:
    raise ValueError("Please provide the number to convert as a parameter.")

parseAsNum(sys.argv[1])