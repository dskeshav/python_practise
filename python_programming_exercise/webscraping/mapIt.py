#! python3 
#mapIt.py - launches a map in the browser using an address from the commmadline or clipboard 

import sys
import webbrowser

import pyperclip
# pyperclip module copies the content from the clipboard
if len(sys.argv)>1:
    #Getting address from the command prompt
    address=" ".join(sys.argv[1:])
else :
    #Getting address from the clip board.
    address=pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/'+address)