from urllib import urlencode
from urllib2 import urlopen
import time


def send_to_server(url,post_data=None):
    if post_data:
        page=urlopen(url,urlencode(post_data))
    else:
        page=urlopen(url)
    return page.read().decode('utf8')
    
s=send_to_server(r'http://localhost:8080/cgi-bin/add_timing_data.py',{'TimingValue':time.localtime()})
print s