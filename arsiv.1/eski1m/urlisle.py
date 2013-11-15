import urlparse
class urlislemleri:
    def reverseUrl(self, url):
        """

        @rtype : object
        """
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
