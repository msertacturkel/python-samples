#!/usr/bin/python

from __future__ import with_statement
import happybase
from collections import Counter

class HBase:
    table = None
    reversedurls=[]
    def __init__(self):
        """

        @rtype : object
        """
        connection = happybase.Connection('localhost', compat='0.90')
        self.table = connection.table('webpage')

	scanner = self.table.scan()
        for row_key, data in scanner:
                    row = self.table.row(row_key)
		    if not(row is None):
		    	self.reversedurls.append(row_key)
	self.reversedurls = [k for k, v in Counter(self.reversedurls).iteritems() if v == 1]

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
        if not(reversedurl in self.reversedurls):
            try:
		#print "url yaziliyor"
		self.reversedurls.append(reversedurl)
		self.table.put(
                     reversedurl,
                     {'f:SIRALAMA': "\'" + str(i) + "\'"})
                #self.table.put("com.agmlab.www:http/", {'f:SIRALAMA':"\'"+str(i)+"\'"})
            except:
                print "hbase e yazarken hata olustu..."
                raise
        else:
	    #print "else......"
            pass
