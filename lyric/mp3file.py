#!/usr/bin/python
# -*- coding: utf8 -*-
# Chieh Lee Jul 2017

import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3

'''
APIC=cover front,  (image/jpeg, 3995131 bytes)
TALB=My Love
TIT2=無事生非
TPE1=田馥甄
TRCK=7/10
USLT=[unrepresentable data]
'''

class mp3file:
	
	# constructor given a directory
	def __init__(self, directory):
		self.directory = directory
		build = []

	# return only list on only mp3 files in the directory
	def mp3s_index(self):
		files = os.listdir(self.directory)
		mp3s = []
		for x in files:
			if (x[-4:] == '.mp3'):
				mp3s.append(x.encode('utf8'))
		return mp3s

	def mp3s_directory(self):
		mp3s = []
		for x in self.mp3s_index():
			s = self.directory + '\\' + x.decode('utf8')
			mp3s.append(s.encode('utf8'))
		return mp3s


	# abstract function for getting tag of a mp3 folder
	# will convert any tag from unicode to utf-8
	def get_tag_value(self, tag):
		output = []
		if self.mp3s_directory() != []:
			for x in self.mp3s_directory():
				filename = x.decode('utf8')
				mp3 = ID3(filename)
				output.append(mp3[tag].text[0].encode('utf-8'))
			return list(set(output))
		else:
			raise Exception ('tag %s retuns none' % tag)

	
	# build the info tuples (TPE1, TALB, TIT2, USLT='')
	# aka (artist, album, title, lyric='')
	def build_mtp(self):
		try:
			mp3dir = self.mp3s_directory()
			output = []
			if mp3dir != []:
				for x in mp3dir:
					filename = x.decode('utf8')
					mp3 = ID3(filename)
					artist = mp3['TPE1'].text[0].encode('utf8')
					album  = mp3['TALB'].text[0].encode('utf8')
					title =  mp3['TIT2'].text[0].encode('utf8')
					lyric = ''.encode('utf8')
					'''
					if 'USLT::eng' in mp3.keys():
						lyric = mp3['USLT::eng'].text.encode('utf8')
					elif 'USLT::XXX' in mp3.keys():
						lyric = mp3['USLT::XXX'].text.encode('utf8')
					elif 'USLT::zho' in mp3.keys():
						lyric = mp3['USLT::zho'].text.encode('utf8')
					else:
						lyric = ''
					'''
					output.append((artist, album, title, lyric))
			else:
				raise Exception ('0 mp3 files in the directory')
			self.build = output
			return output
		except KeyError as k:
			return  'Did not find key %s: %s' % (k, filename.encode('utf8'))


	# return album name in utf-8
	def get_album(self):
		return self.get_tag_value('TALB')

	# return artist in utf-8
	def get_artist(self):
		return self.get_tag_value('TPE1')


	# insert lyrics from the given dictionary
	def insert_lyrics(self):
		pass