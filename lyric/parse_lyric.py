# Chieh Lee @ Nov 2016

import urllib2
import urllib
import urlparse
import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
from mp3file import mp3file
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
#ojim_Parser import Mojim_Parser

'''
search query for mojim.com:
	?t1 = artist
	?t2 = album
	?t3 = title
	?t4 = lyrics
'''

artist = ''
album = ''

class parse_lyric:

	# constructor pass a mp3file class
	def __init__(self, mp3f):
		self.mp3f = mp3f
	
	# nested class for parsing mojim html tags
	class Mojim_Parser(HTMLParser):

		def handle_starttag(self, tag, attrs):
			global artist
			global album
			lastline = ''
			output = []
			print artist
			for attr in attrs:
				if (attr[1].find(artist) >= 0 or \
					attr[1].find(album) >= 0):
					output.append((attr[1], lastline))
					print lastline
					print attr[1]
				lastline = attr[1]

	
	def search_by_artist(self):
		global artist
		artist = self.mp3f.get_artist()
		name = urllib.urlencode({'key' : artist})[4:]
		print name
		path = '/' + name + '.html'
		url = urlparse.urlunparse(('https', 'mojim.com', path, '', 't1', ''))
		req = urllib2.Request(url)
		html = urllib2.urlopen(req).read()
		parser = self.Mojim_Parser()
		parser.feed(html)


path = "C:\\Users\\leejaypiqq\\Desktop\\future"
f = mp3file(path)
p = parse_lyric(f)
p.search_by_artist()
