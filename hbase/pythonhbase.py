#!/usr/bin/python
import happybase
import sys
#import os
import subprocess

total = len(sys.argv)
cmdargs = sys.argv
urls=[]
dosyadanGelenUrller=[]
sayac=0
fark=[]
try:
    connection = happybase.Connection('localhost', compat='0.90')
    table = connection.table('webpage')
   # os.system("eject")
except:
    print 'baglanti saglanamadi'
    raise
try:
    scanner = table.scan()
    for row_key, data in scanner:
        try:
            row = table.row(row_key)
	    if len(cmdargs)==1 and sayac==0:
	    	print "secenekler: ",row.keys()
		sayac=sayac+1
	    else:
	    	urls.append(row.get(cmdargs[1]))
        except:
            print "KULLANIM: ./pythonhappybase.py kolonfamily:kolonadi karsilastirilacak_dosya_adi"
    print "Veritabaninda varolan URL sayisi: ",len(urls)
except:
        print 'tablo okunamadi..'
if len(cmdargs)==3:
	fp = open(cmdargs[2])
	while 1:
    		line = fp.readline()
    		if not line:
        		break
		dosyadanGelenUrller.append(line[:-1])
                print line[:-1]

fark=list(set(dosyadanGelenUrller) - set(urls))
g=open("fark.txt","w")
g.write("Veritabaninda varolan URL sayisi: %d :\n" %len(urls))
for i in range(len(fark)):
	g.write(fark[i])
g.close()

subprocess.call("vi fark.txt", shell=True)

		
