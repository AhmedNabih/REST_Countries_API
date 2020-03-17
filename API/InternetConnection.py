import urllib
import urllib.request


class Connection:
    def CheckInternetConnection(host = 'http://google.com'):
        try:
            urllib.request.urlopen(host)  # Python 3.x
            return True
        except:
            return False
