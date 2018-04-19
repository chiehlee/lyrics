import os

l =  os.listdir('D:\Downloads\\22')
for x in l:
	s = x[4:]
	of = 'D:\Downloads\\22' + '\\' + x
	nf = 'D:\Downloads\\22' + '\\Vol_' + s
	print of
	print nf
	os.rename(of, nf)