#!/usr/bin/python
import happybase

class HBase:
    table = None
    def __init__(self):
        try:
            connection = happybase.Connection('localhost', compat='0.90')
            self.table = connection.table('webpage')
        except:
            print 'baglanti saglanamadi'
            raise
        scanner = self.table.scan()
        f = open('ol1.txt','w')
	try:
            for row_key, data in scanner:
                row = self.table.row(row_key)
                result = [(key, value) for key, value in row.iteritems() if key.startswith("ol")]
		print result
		#f.write(result+"\n") # python will convert \n to os.linesep
        except:
	    print "satir okunamadi"
		#f.write(result[i]) # python will convert \n to os.linesep

if __name__ == '__main__':
    hbase = HBase()



