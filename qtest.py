#!/usr/bin/python
# -*- coding: utf8 -*-
# Chieh Lee Jul 2017

import urllib2
import urllib
import webbrowser
import codecs
import urlparse
from urllib2 import OpenerDirector
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint


s = open('utf8.txt').read().decode("utf-8-sig").encode("utf-8")
print s
print ' '.join(format(ord(x), '02x') for x in s)
name = s[3:]
name2 = '\xe6\x96\xb9\xe5\xa4\xa7\xe5\x90\x8c'
s2 = urllib.urlencode({'key' : s})
print s2
print s2[13:]
path = '/' + s2[13:] + '.html'

p1 = '張惠妹'
pu = urllib.quote_plus(p1)
purl = '/' + pu + '.html'



'''
url = urlparse.urlunparse(('https', 'mojim.com', purl, '', 't1', ''))
print url

req = urllib2.Request(url)
print req.get_method()
print req.get_full_url()

html = urllib2.urlopen(url)
u = html.read()
f = open('t1_example.txt', 'wb+')
f.write(u)
'''



class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        lastline = ''
        for attr in attrs:
            if attr[1].find('無事生非') >= 0:
                print attrs


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


parser = MyHTMLParser()
f = open('example.txt', 'rb').read()
print type(parser.feed(f))
aa = (1, 2)
print isinstance(aa, tuple)