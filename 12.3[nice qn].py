import urllib.request,  urllib.parse,  urllib.error
url=input('enter url- ')
fhand= urllib.request.urlopen(url) #first opening the file
f_data=fhand.read() #reading the entire file in one variable
f_decoded=f_data.decode()
print(len(f_decoded))
if len(f_decoded)<=3000:
    print(f_decoded)
else:
    exit()

#http://data.pr4e.org/romeo.txt......this is a complete URL......
