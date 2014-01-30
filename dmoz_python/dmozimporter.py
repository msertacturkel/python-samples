#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import urllib
import shutil
import subprocess

url=[]
dir_name="dmoz"
working_dir=os.getcwd()

def dataGetir():
    if not os.path.exists("%s/%s/url.txt" %(working_dir,dir_name)):
        shutil.copy("%s/url.txt" %working_dir,"%s/%s/" %(working_dir,dir_name))

    os.chdir("%s/%s/" %(working_dir,dir_name))
    with open('url.txt') as fp:
        for line in fp:
            parcala=line.split(";")
            cron=parcala[0]
            url_=parcala[1]
            jarName=parcala[2]
            url.append(url_)
    
            cronCalistir(cron)
            runJar(jarName)    

    for i in range(len(url)):
        print "indirelen url: ",url[i]
	os.system('wget %s' %url[i])
    print "url sayisi: ",len(url)

def dataTemizle():
    os.chdir("%s/%s/" %(working_dir,dir_name))
    os.system("rm -rf *")
    os.chdir("/%s" %working_dir)

def cronCalistir(cron):
     os.chdir("/%s" %working_dir)
     if os.path.exists('%s/test.cron' %working_dir):
        try:
            f = open('test.cron', 'w')
            dizin=os.getcwd()
            cronstmt = "%s %s/dmozimporter.py\n" %(cron,dizin)
            f.write(cronstmt)
            f.close()
            print ".......cron editlendi"
        except:
            print ".......dosya editlenemedi..."
     subprocess.call("crontab test.cron", shell=True)
     os.chdir("%s/%s/" %(working_dir,dir_name))


def runJar(jarName):
    subprocess.call(['java', '-jar', '%s' %jarName])

if __name__ == '__main__':
    print "******************************************************************************************************************************************"
    print "dmozimporter.py ile ayni dizinde url.txt adinda bir dosyaya cron stringi;indirilecekurl;calistirilacak jar formatında satir girilmelidir. "
    print "******************************************************************************************************************************************"
    if not os.path.exists("%s/%s/" %(working_dir,dir_name)):
	try:
            os.mkdir(dir_name)
        except:
            pass
    dataTemizle()
    dataGetir()
	
