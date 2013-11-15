#!/usr/bin/python
from __future__ import with_statement
from urlparse import urlparse
import urllib2
import re
import urlparse
import os
import zipfile
import hashlib
import sys
import happybase
from urlparse import urlparse
import md5
import hashlib



class HBase:
    table = None

    def __init__(self):
        connection = happybase.Connection('localhost', compat='0.90')
        self.table = connection.table('webpage')

    def singleton():
        instances = {}

        def getinstance():
            if cls not in instances:
                instances[cls] = cls()
                return instances[cls]
        return getinstance

    def checkRow(self, reversedurl, i):
        row = self.table.row(reversedurl)
        if(not(row is None)):
            try:
                #self.table.put("com.agmlab.www:http/", {'f:SIRALAMA':"\'"+str(i)+"\'"})
                self.table.put(
                    reversedurl,
                    {'f:SIRALAMA': "\'" + str(i) + "\'"})
            except:
                print "hbase e yazarken hata olustu..."
                raise

        else:
            print i, ". url webpagede yok"
eski = ""


