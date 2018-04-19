#!/usr/bin/python
# -*- coding: utf8 -*-
# Chieh Lee Jul 2017

import urllib2
import urllib
import urlparse
import os
import codecs
from mutagen.id3 import ID3
from mp3file import mp3file
from HTMLParser import HTMLParser
import re

'''
search query for mojim.com:
	?t1 = artist
	?t2 = album
	?t3 = title
	?t4 = lyrics
'''
# example html file
t1_example = open('t1_example.txt', 'rb')
t2_exampl3 = open('t2_example.txt', 'rb')
t3_example = open('t3_example.txt', 'rb')
lyricpage_example = open('lyricpage_example.txt', 'rb')
temp = open('temp.txt', 'wb+')

artist = ''
album = ''


# unparse mojim.com url with given path and query
def url_str(p, q):
	#(scheme='https', netloc='mojim.com', path=p, paprams='', query=q)
	p = urllib.quote(p) + '.html'
	return ('https', 'mojim.com', p, '', q, '')

def get_mojim_response(path):
	url = 'https://mojim.com/%s' % urllib.quote(path)
	mojim_response = urllib2.urlopen(url)
	return mojim_response.read().decode('utf-8')

# class handle information of 1 mp3 file at time
class Mojim_Parser:

	# constructor pass a mp3file class
	def __init__(self, mp3_tuple):
		# mp3_tuple will be the 3-tuple object that is built by mp3file.py
		self.mp3_tuple = mp3_tuple
		if (not isinstance(self.mp3_tuple, tuple)) or (len(self.mp3_tuple) != 4):
			raise Exception('Mojim_Parser.py: Wrong MP3 file build')
	
	# abstract method for searching attribute on mojim.com
	# ! this method will create a connection to mojim.com !
	def search_mojim(self, p, q):
		url = urlparse.urlunparse(url_str(p, q))
		html_result = urllib2.urlopen(url)
		return html_result

	# search by artist
	# ! this method will create a connection to mojim.com !
	def search_by_artist(self):
		return self.search_mojim(self.mp3_tuple[0], 't1')

	# search by title
	# ! this method will create a connection to mojim.com !
	def search_by_album(self):
		return self.search_mojim(self.mp3_tuple[1], 't2')

	# search by title
	# ! this method will create a connection to mojim.com !
	def search_by_title(self):
		return self.search_mojim(self.mp3_tuple[2], 't3')

	# return the lyric of this mp3_tuple
	def return_lyric(self):
		return

# subclass of HTMLParser for parsing searched page by artist
class Search_Artist_Parser(HTMLParser):
	
	# constructor pass a mp3file class
	# param q    : query
	# param mp3_tuple : mp3 tuple
	def __init__(self, q, mp3_tuple):
		HTMLParser.__init__(self)
		# mp3_tuple will be the 3-tuple object that is built by mp3file.py
		self.q = q
		self.mp3_tuple = mp3_tuple
		self.output = []

	def html_searcher(self, attrs, tuple_attritube, search_pattern='.*'):
		if attrs[0][0] == 'href' and \
			re.match(search_pattern, attrs[0][1]) and \
			attrs[1][0] == 'title' and \
			attrs[1][1].find(tuple_attritube) >= 0:
			self.output.append((attrs[1][1], attrs[0][1]))

	def handle_starttag(self, tag, attrs):
		# q == 1, search by artist, q == 10, page after search by artist which looks the album further return list of (name, url)
		# example tag <a  href="/twh100090.htm" title="阿妹 歌詞" >
		if self.q == 1 and self.output != False and tag == 'a' and len(attrs) == 2:
			self.html_searcher(attrs, self.mp3_tuple[0])
		elif self.q == 10 and self.output != False and tag == 'a' and len(attrs) == 2:
			self.html_searcher(attrs, self.mp3_tuple[1], search_pattern=r'^/[a-zA-Z]*[0-9]*[x][0-9]{1,4}[.]htm$')
		elif self.q == 100 and self.output != False and tag == 'a' and len(attrs) == 2:
			self.html_searcher(attrs, self.mp3_tuple[2])
		elif self.q == 2:
			pass
		else:
			pass

	def handle_data(self, data):
		# q == 1, search by artist
		if self.q == 1:
			if (data.find('沒有符合的') >= 0) and (data.find(self.mp3_tuple[0]) >= 0):
				self.output = False
		elif self.q == 1:
			pass
		else:
			pass
	
	'''	
    def handle_endtag(self, tag):
        print "End tag  :", tag

    def handle_data(self, data):
        print "Data     :", data

    def handle_comment(self, data):
        print "Comment  :", data

    def handle_decl(self, data):
        print "Decl     :", data
	'''


p = Mojim_Parser(('阿妹', '偷故事的人', '連名帶姓', ''))
print url_str(p.mp3_tuple[0], 't1')
#temp.write(p.search_by_artist().read())
#t1_example.write(p.search_by_artist().read())
m = Search_Artist_Parser(1, p.mp3_tuple) 
m.feed(t1_example.read())
print m.output

m = Search_Artist_Parser(10, p.mp3_tuple)
with open('artist_page.txt', 'r') as artist_page:
	m.feed(artist_page.read())
print m.q
for item in m.output:
	print item[0]
	print item[1]

m = Search_Artist_Parser(100, p.mp3_tuple)
with open('q100.txt', 'r') as q100:
	m.feed(q100.read())
if not m.output:
	print '沒有符合的'
else:
	for x in m.output:
		print x[0]
		print x[1]
