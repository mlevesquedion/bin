import sys
import webbrowser
import pyperclip

if len(sys.argv)>1:
    search = ' '.join(sys.argv[1:])
else:
    search = pyperclip.paste()

webbrowser.open('https://www.google.ca/search?q='+search)
