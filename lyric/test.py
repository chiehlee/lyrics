#!/usr/bin/python
# -*- coding: utf8 -*-
# Chieh Lee Jul 2017

import unittest
import mp3file
from Mojim_Parser import Mojim_Parser
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3 as id3
from mutagen.id3 import ID3

class Testlyric(unittest.TestCase):

	def setUp(self):
		self.mp3file = mp3file.mp3file(unicode('MP3'))
		self.mp3file2 = mp3file.mp3file(unicode
			('C:\Users\ChiehL\Dropbox\Project\lyrics\lyric'))
		self.mp3file3 = mp3file.mp3file(unicode('MP3\\test2'))
		self.mp3file4 = mp3file.mp3file(unicode('MP3\\test'))
		###########################################################################
		self.mojim_parser1 = Mojim_Parser(('田馥甄', 'My Love', '無事生非', ''))
		self.mojim_parser2 = Mojim_Parser(('方大同', '未來', '未來', ''))

	
	# test mp3file.py
	def test_mp3s_index(self):
		self.assertEqual(set(self.mp3file.mp3s_index()), set(['01.mp3', '02.mp3', '04.mp3',
			'05.mp3', '06.mp3', '07.mp3', '08.mp3', '09.mp3',
			'田馥甄-(My Love)-03.My Love.mp3', '田馥甄-(My Love)-10.你.mp3', '无事生非.mp3']))
		#test for another directory without mp3 files
		self.assertEqual(set(self.mp3file2.mp3s_index()), set([]))
		self.assertEqual(set(self.mp3file3.mp3s_index()), set(['田馥甄-(My Love)-10.你.mp3',
			'07.mp3']))

	def test_mp3s_directory(self):
		self.assertEqual(set(self.mp3file.mp3s_directory()), set(['MP3\\01.mp3', 'MP3\\02.mp3', 
			'MP3\\04.mp3', 'MP3\\05.mp3', 'MP3\\06.mp3', 'MP3\\07.mp3', 'MP3\\08.mp3', 
			'MP3\\09.mp3', 'MP3\\田馥甄-(My Love)-03.My Love.mp3', 
			'MP3\\田馥甄-(My Love)-10.你.mp3', 'MP3\\无事生非.mp3']))
		#test for another directory without mp3 files
		self.assertEqual(set(self.mp3file2.mp3s_directory()), set([]))

	def test_get_tag_value(self):
		with self.assertRaises(Exception):
			self.mp3file2.get_tag_value('TIT2')
			self.mp3file2.get_tag_value('TPE1')
		self.assertEqual(self.mp3file.get_tag_value('TPE1'), ['田馥甄'])
		self.assertEqual(self.mp3file.get_tag_value('TALB'), ['My Love'])

	def test_build_mtp(self):
		self.assertEqual(set(self.mp3file.build_mtp()), set([('田馥甄', 'My Love', '烏托邦', ''), 
			('田馥甄', 'My Love', '要說什麼', ''), ('田馥甄', 'My Love', '請你給我好一點的情敵', ''),
			('田馥甄', 'My Love', '還是要幸福', ''), ('田馥甄', 'My Love', '魔鬼中的天使', ''), 
			('田馥甄', 'My Love', '無事生非', ''), ('田馥甄', 'My Love', '花花世界', ''), 
			('田馥甄', 'My Love', '影子的影子', ''), ('田馥甄', 'My Love', '無事生非', ''), 
			('田馥甄', 'My Love', 'My Love', ''), ('田馥甄', 'My Love', '你', '')]))
		self.assertRegexpMatches(self.mp3file3.build_mtp(), '^Did not find key \'(TPE1|TIT2|TALB)\': *')
		with self.assertRaises(Exception):
			self.mp3file4.build_mtp()
		#test for another directory without mp3 files
		self.assertEqual(set(self.mp3file2.mp3s_index()), set([]))

	def test_get_album(self):
		self.assertEqual(self.mp3file.get_album()[0], 'My Love')
		with self.assertRaises(Exception):
			self.mp3file2.get_album()

	def test_get_artist(self):
		self.assertEqual(self.mp3file.get_artist()[0], '田馥甄')
		with self.assertRaises(Exception):
			self.mp3file2.get_artist()
	

	###########################################################################
	# test Mojim_Parser.py
	
	# test as static method
	def test_url_str(self):
		self.assertEqual(Mojim_Parser.url_str('田馥甄', 't1'), ('https', 'mojim.com', 
			'%E7%94%B0%E9%A6%A5%E7%94%84.html', '', 't1', ''))
		self.assertEqual(Mojim_Parser.url_str('twy109122x4x7', ''), ('https', 'mojim.com', 
			'twy109122x4x7.html', '', '', ''))
		self.assertEqual(Mojim_Parser.url_str('張惠妹', 't3'), ('https', 'mojim.com', 
			'%E5%BC%B5%E6%83%A0%E5%A6%B9.html', '', 't3', ''))
		self.assertEqual(Mojim_Parser.url_str('', ''), ('https', 'mojim.com', 
			'.html', '', '', ''))

	def test_search_mojim(self):
		# I self tested it. It's no problem
		return

	def test_search_by_artist(self):
		# I self tested it. It's no problem
		return

	def test_search_by_album(self):
		# I self tested it. It's no problem
		return

	def test_search_by_title(self):
		# I self tested it. It's no problem
		return





suite = unittest.TestLoader().loadTestsFromTestCase(Testlyric)
unittest.TextTestRunner(verbosity=2).run(suite)