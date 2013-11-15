import urllib2
import os
import zipfile
import urlisle

class Alexa:

    '''
    this class provides access to the Alexa ranking of URLs
    usage: create a new instance of this class (ranker = Alexa()) and use the getrank method
    '''
    yeni = ""
    reversedurls = []

    def __init__(self, eski):
        try:
            urls = {}
            reversedurls = []
            f = open('top-1m.zip', 'wb')
            opener = urllib2.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            file = opener.open(
                'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip').read()
            f.write(file)
            f.close()
            # unzip it
            current_dir = os.getcwd()
            zip = zipfile.ZipFile(r'top-1m.zip')
            zip.extractall(current_dir)
            # read the alexa ranking
            self.yeni = os.path.getsize('top-1m.zip')
            self.eskidosyaboyutu=eski
            print "eski....(KONTROL ONCESI)",self.eskidosyaboyutu
            print "yenia:...", self.eskidosyaboyutu
            if (self.yeni == self.eskidosyaboyutu):
                print "Dosya degismis islem yapiliyor............"
                f_csv = open('top-1m.csv')
                csv_data = f_csv.read()
                f_csv.close()
                lines = csv_data.split("\n")
                forSplit = []
                for line in lines:
                    try:
                        # print line
                        forSplit = line.split(",")
                        sira = forSplit[0]
                        urls[sira] = "http://www." + forSplit[1]
                        print urls[sira]
                        newurl = urlisle.urlislemleri().reverseUrl(urls[sira])
                        self.reversedurls.append(newurl)
                        print 'newurl==================>',newurl
                    except:
                        continue
            else:
                print 'dosya ayni'

        except:
            print 'hata'
            raise




