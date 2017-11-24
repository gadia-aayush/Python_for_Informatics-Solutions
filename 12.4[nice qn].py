import urllib.request, urllib.parse, urllib.error
from urllib.request import Request #it is very necessary for https/ssl certified websites
from bs4 import BeautifulSoup
import ssl

#to fix ssl certificate error
ctx=ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode=ssl.CERT_NONE


inp=input('enter url- ')
url = Request(inp,  headers={'User-Agent': 'Chrome/51.0.2704.84'}) #imp for ssl certified websites
#find user agent of a browser by http://www.whoishostingthis.com/tools/user-agent/
html= urllib.request.urlopen(url, context=ctx).read() #first opening the file & reading the entire file in one line itself
#here writing context=ctx also necessary as ssl certificate website we are checking too
soup=BeautifulSoup(html, 'html.parser') #returns a beautiful cleaned html.....and it returns an object which is stored in soup
tags=soup('p') #returns a list
print(len(tags))

#all http wala links hi we are parsing...... (http://data.pr4e.org/romeo.txt......this is a complete URL......)
#by editing now https links bhi we can parse  (https://www.si.umich.edu..)
