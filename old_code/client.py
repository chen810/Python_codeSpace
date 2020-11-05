from socket import *
while True:
    severName = '127.0.0.1'
    severPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    msage = input("input the string:")
    clientSocket.sendto(msage.encode(), (severName, severPort))
    modi_msg, serveradd = clientSocket.recvfrom(2048)
    print(modi_msg.decode())
    clientSocket.close()
