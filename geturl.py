#!/usr/bin/python
import urllib
import lxml.html
import os 
connection = urllib.urlopen('http://www.agmlab.com')
if(os.path.isfile('somefile.txt')):
        os.remove('somefile.txt')                                   

dom =  lxml.html.fromstring(connection.read())
f=open('somefile.txt', 'a')
for link in dom.xpath('//a/@href'): 
	f.write(link+"\n")
