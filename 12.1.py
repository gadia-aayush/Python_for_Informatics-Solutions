import socket
url=input('enter the url: ')
hostname=url.split('/')[2]
try:
    mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((hostname, 80))
    print('connected')

except:
    print('Re-enter the correct URL')


#http://www.py4inf.com/code/romeo.txt......this is a complete URL......
