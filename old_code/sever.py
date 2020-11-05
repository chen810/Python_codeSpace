from socket import *
severName = '127.0.0.1'
severPort = 12000
seversocket = socket(AF_INET,SOCK_DGRAM)
seversocket.bind(('',severPort))
print('all have prepared!')
while True:
    msg, clientadd = seversocket.recvfrom(2048)
    modi_msg = msg.decode().upper()
    print("{0}===>{1}".format(msg,modi_msg))
    seversocket.sendto(modi_msg.encode(),clientadd)
