import socket
url=input('enter the url: ')
hostname=url.split('/')[2]
try:
    mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket create
    mysock.connect((hostname, 80)) #socket connect
    cmd='GET '+url+' HTTP/1.0\r\n\r\n' #make sure to put \r\n\r\n...as for telnet genrallt for new line \r\n is used....and by it only correct o/p coming up
    print (cmd)
    mysock.send(cmd.encode()) #now requesting the host for data thru socket....
    print('connected')
    data=mysock.recv(512) #socket se data receive....and atmost 512 bytes ka data receive..you can put anything here
    print(len(data))
    if len(data)>3000:
        exit()
    else:
        print(data.decode())    
    mysock.close() #it is very important to close the socket after using it....
  
except:
    print('Re-enter the correct URL')
    
    


#http://data.pr4e.org/romeo.txt......this is a complete URL......
