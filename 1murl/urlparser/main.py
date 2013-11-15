#!/usr/bin/python
# -*- coding: cp1254 -*-

import subprocess
import os
import hbase
import alexa

if __name__ == '__main__':
    if os.path.exists('test.cron'):
        try:
                f = open('test.cron', 'w')
                cronstmt = "30 12 */15 * *  ."+os.getcwd()+"/main.py\n"
                satir = f.write(cronstmt)
                f.close()
        except:
                print "dosya editlenemedi..."
        subprocess.call("crontab test.cron", shell=True)
        # os.remove("test.cron")
        if(os.path.exists('top-1m.zip')):
            try:
                #'top-1m.zip'
                eski = os.path.getsize('top-1m.zip')
                # Dosya.setSize(eski)
                print 'eski....:  ', eski
            except:
                raise
                print 'dosya silinmis.'
    hbase = hbase.HBase()
    object1 = alexa.Alexa(eski)
    for i in range(len(object1.reversedurls)):
        #print object1.reversedurls[i]
        hbase.checkrow(object1.reversedurls[i], i + 1)
