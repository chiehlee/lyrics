#!/usr/bin/python
# -*- coding: utf8 -*-
# Chieh Lee Jul 2017

import mp3file
import os
import sys
import urllib2
import urllib
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3 as id3
from mutagen.id3 import ID3
import re




m = mp3file.mp3file(unicode('MP3'))
#print m.mp3s_directory()

n = ID3('MP3\\07.mp3', translate=False)
'''
print n['TPE1']
keep = n.getall('TPE1')
print keep
print type(keep)
print type(id3.TPE1(text=u'new'))
print n.setall('TPE1', [id3.TPE1(text='new'.encode('utf8'))])
print n.pprint().encode('utf8')
'''

#n.add(id3.USLT(lang='eng', text=u'測試'))



k = mp3file.mp3file(unicode('C:\Users\leejaypiqq\Dropbox\Project\lyrics\lyric'))
p = mp3file.mp3file(unicode('MP3\\test2'))
pp = ID3(u'MP3\\test2\\07.mp3')
pp.delall('TIT2')
pp.save()

tv = ID3(p.mp3s_directory()[0].decode('utf8'))
print p.build_mtp()


print len((1,2,3,4))
