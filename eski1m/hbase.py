#!/usr/bin/python

from __future__ import with_statement
from urlparse import urlparse
import re


import sys
import happybase
from urlparse import urlparse
import md5
import hashlib



class HBase:
    table = None

    def __init__(self):
        """

        @rtype : object
        """
        connection = happybase.Connection('localhost', compat='0.90')
        self.table = connection.table('webpage')

    @staticmethod
    def singleton():
        instances = {}

        def getinstance():
            if cls not in instances:
                instances[cls] = cls()
                return instances[cls]
        return getinstance

    def checkrow(self, reversedurl, i):
        """

        @param reversedurl:
        @param i:
        @raise:
        """
        row = self.table.row(reversedurl)
        if not(row is None):
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



