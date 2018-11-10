import webbrowser
import sys

synonym_website_address = 'http://www.synonymo.fr/synonyme/'

target_word = sys.argv[1]

webbrowser.open(synonym_website_address + target_word)
