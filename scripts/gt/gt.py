import sys
import webbrowser
import pyperclip

usage = """\
gt [destination_language] [word_or_sentence]
opens google translate in browser with the desired parameters
(press enter to exit) """

available_languages = {
    'en' : 'english',
    'fr' : 'french'
}

try:
    dest_lang = sys.argv[1]
    word = sys.argv[2]
except IndexError:
    input(usage)

try:
    lang = available_languages[dest_lang]
except KeyError:
    input('Unavailable language : {} (enter to exit) '.format(dest_lang))


if len(sys.argv)>2:
    word = ' '.join(sys.argv[2:])
else:
    word = pyperclip.paste()

webbrowser.open('https://www.google.ca/search?q=translate+to+'+lang+'='+word)
