#!/usr/bin/python
# -*- coding: utf8 -*-
# Chieh Lee Jul 2017

import sys
import os
from mp3file import mp3file
from parse_lyric import parse_lyric

def print_mp3_index(foo):
	for x in foo.mp3s_index():
		print x

	
if __name__ == "__main__":
	if (not os.path.isdir(sys.argv[1])):
		print 'No such directory'
		exit(0)
	
	# main mp3 files object class : foo
	foo = mp3file(unicode(sys.argv[1]))
	
	if (len(foo.mp3s_index()) == 0):
		print 'No mp3 files in given directory'
		exit(0)
	# confirm mp3s in the directory
	print_mp3_index(foo)
	print 
	if (raw_input('Press Any Key to Continue or \'n\' to stop: ') == 'n'):
		exit(0)
	
	# main parse_lyric class object and passing foo
	bar = parse_lyric(foo)




