#!/usr/bin/python
from urlparse import urlparse
import urllib2
import happybase
import whois
from time import gmtime, strftime
from collections import Counter


infowhois = {}
unreversedurl = ""
whoislist = []
reversedurl = []


class HBase:
    table = None

    def __init__(self):
        try:
            connection = happybase.Connection('localhost', compat='0.90')
            self.table = connection.table('externalpage')
        except:
            print 'baglanti saglanamadi'
            raise
        try:
            scanner = self.table.scan()
            for row_key, data in scanner:
                try:
                    row = self.table.row(row_key)
                    # row--->{'mtdt:expiration_date': '2020-03-30 00:00:00',
                    # 'mtdt:_name_': 'www.example.com', 'mtdt:name':
                    # 'facebook.com'}

                    unreversedurl = self.unreverse(self, row_key)
                    if not(row is None):
                        if "mtdt:expiration_date" in row and row['mtdt:expiration_date'] < strftime("%Y-%m-%d %H:%M:%S", gmtime()):
                            print "whois e expried_data in suresi doldugu icin gidiliyor...."
                            u = urlparse(unreversedurl)
                            whoislist.append(u.hostname)
                            reversedurl.append(row_key)
                            # self.setWhoisinfo(row_key)

                        elif ("mtdt:expiration_date" in row) is False:
                            print "mtdt:expiration_date yok veya exprieddate suresi dolmamis"
                            u = urlparse(unreversedurl)
                            whoislist.append(u.hostname)
                            # self.setWhoisinfo(row_key)
                            reversedurl.append(row_key)

                        else:
                            print "else..............."
                            continue

                    else:
                        print "rowun valuesu null geldi"
                        u = urlparse(unreversedurl)
                        whoislist.append(u.hostname)
                        reversedurl.append(row_key)

                        # self.setWhoisinfo(reversedurl)

                except:
                    print "row alinirken hata olustu..."
        except:
            print 'rowkeyler listleye eklenemedi..'

    @staticmethod
    def reverseUrl(self, url):
        part = []
        reversedurl = ""
        o = urlparse(url)
        hostname = str(o.hostname)
        part = hostname.split('.')
        if len(part) > 0:
            for i in range(len(part) - 1, 0, -1):
                reversedurl += part[i] + '.'
            reversedurl += part[0] + ':' + o.scheme + '/'
        else:
            return hostname
        return reversedurl

    @staticmethod
    def unreverse(self, rvsdurl):
        buf = ""
        self.pathbegin = rvsdurl.find("/")
        if self.pathbegin is -1:
            self.pathbegin = len(rvsdurl)
        self.sub = rvsdurl[0:self.pathbegin]
        self.splits = self.sub.split(":")
        if len(self.splits) is 2:
            buf += self.splits[1]
            buf += "://"
            self.reverse = self.splits[0]
            dotsplits = self.reverse.split(".")
            if len(dotsplits) > 0:
                for i in range(len(dotsplits) - 1, 0, -1):
                    buf += dotsplits[i]
                    buf += "."
                buf += dotsplits[0]
            else:
                buf += self.splits[0]
        if len(self.splits) is 3:
            buf += ":"
            buf += self.splits[2]
        buf += rvsdurl[self.pathbegin:]
        return str(buf)

    def setWhoisinfo(self, url):
        print "setwhoisinfo"
        for i in range(len(infowhois)):
            self.table.put(
                url,
                {'mtdt:' + str(infowhois.keys()[i]): str(infowhois.values()[i])})


class Whois:

    def __init__(self, url_):
        print "WHOIS: ", url_
        domain = whois.query(url_)
        infowhois["name"] = domain.name
        infowhois["expiration_date"] = domain.expiration_date
        infowhois["last_updated"] = domain.last_updated
        infowhois["registrar"] = domain.registrar
        infowhois["creation_date"] = domain.creation_date
        infowhois["name_servers"] = domain.name_servers
        infowhois["creation_date"] = domain.creation_date

if __name__ == '__main__':
    	hbase = HBase()
   	whoislist = [k for k, v in Counter(whoislist).iteritems() if v == 1]
  	for i in range(len(whoislist)):
            Whois(whoislist[i])
            hbase.setWhoisinfo(reversedurl[i])



