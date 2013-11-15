#!/usr/bin/python
import hashlib
# bastaki ve sondaki elemanlar sabit oldugundan ya index olarak 0 alindi
# yada son eleman
class Test:
    def __init__():
        print 'test calisti'
    def reverseUrlTest(self, url):
        o = urlparse(url)
        #sema=o.scheme ;protocol
        netloc = o.netloc
        hostname = o.hostname
        path = o.path
        port = o.port
        if((port is None or port == "") and (path is None or path == "")):
            print "patern===>com.blogspot.msertacturkel.www:http/  || com.msertacturkel.www:http/"
            parseurl = []
            tmp = []
            reversedurl = ""
            parseurl = url.split('.')
            parseurl.reverse()
            protocolwithwww = parseurl[len(parseurl) - 1]
            tmp = protocolwithwww.split(':')
            tmp[1] = tmp[1][2:]
            tmp[0] = ":" + tmp[0] + "/"
            # http de olsa https de olsa bu sekilde birlesmis
            protocolwithwww = tmp[1][::] + '.' + tmp[0][::]
            parseurl[len(parseurl) - 1] = protocolwithwww
            if(parseurl[0][-1] == "/"):
                parseurl[0][-1] == ""
            for i in range(len(parseurl)):
                if(i < 3):
                    reversedurl += parseurl[i] + '.'
                else:
                    reversedurl += tmp[1][::] + tmp[0][::] + "/"
            reversedurl = reversedurl[:-1]
            print "path veya port girilmemis url== ", reversedurl
            return reversedurl
        elif(not(path is None) and not(path is "") and not (path is "/")):
            print "patern====>com.deneme:http/dosya"
            path = path[1:]
            parseurl = []
            tmp = []
            path = ""
            fileseperator = []
            reversedurl = ""
            parseurl = url.split('.')
            parseurl.reverse()
            protocolwithwww = parseurl[len(parseurl) - 1]
            tmp = protocolwithwww.split(':')
            # http de olsa https de olsa bu sekilde birlesmis
            protocolwithwww = tmp[1][::] + ':' + tmp[0][:] + '/'
            protocolwithwww = protocolwithwww[2:]
            parseurl[len(parseurl) - 1] = protocolwithwww
            fileseperator = parseurl[0].split("/")
            path = fileseperator[1]
            if(parseurl[0][-1] == "/"):
                parseurl[0][-1] == ""
            for i in range(len(parseurl)):
                if(i == 0):
                    reversedurl += fileseperator[0] + '.'
                else:
                    reversedurl += parseurl[i] + '.'
            reversedurl = reversedurl[:-1] + path
            print "pathi girilmis url==", reversedurl
            return reversedurl
        elif(not(port is None) and not(port is "")):
            #['com:8040', 'asd', 'http://www']
            print "pattern===>com.asd.www:https:8040/"
            parseurl = []
            tmp = []
            portseperator = []
            port = ""
            reversedurl = ""
            parseurl = url.split('.')
            parseurl.reverse()
            portseperator = parseurl[0].split(":")
            port = portseperator[1]
            protocolwithwww = parseurl[len(parseurl) - 1]
            tmp = protocolwithwww.split(':')
            tmp[1] = tmp[1][2:]
            # http de olsa https de olsa bu sekilde birlesmis
            protocolwithwww = tmp[1][::] + ':' + tmp[0][:] + ':' + port + '/'
            parseurl[len(parseurl) - 1] = protocolwithwww
            if(parseurl[0][-1] == "/"):
                parseurl[0][-1] == ""
            for i in range(len(parseurl)):
                if(i == 0):
                    reversedurl += portseperator[0] + '.'
                else:
                    reversedurl += parseurl[i] + '.'
            reversedurl = reversedurl[:-1]
            print "port numarasi olan url: ", reversedurl
            return reversedurl
        else:
            return "gecersiz url"
