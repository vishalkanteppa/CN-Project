
from socket import *
from time import ctime
import pickle

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

a = [[0 for i in range(10)] for j in range(5)] 

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
tcpCliSock, addr = tcpSerSock.accept()

check=True
while True:

    arr=[pickle.dumps(a),check]
    tcpCliSock.send(pickle.dumps(arr))

    data=tcpCliSock.recv(BUFSIZ)
    arr=pickle.loads(data)
    if not data:
        break
    a=pickle.loads(arr[0])
    r=arr[1]
    c=arr[2]

    if a[r][c]==1:
        check=False
    else:
        a[r][c]=1
        check=True

tcpCliSock.close()
tcpSerSock.close()
