from socket import *
from time import ctime
import pickle

HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

a = dict()
a["jurassic park"] = [[0 for i in range(10)] for j in range(5)]
a["avengers"] = [[0 for i in range(10)] for j in range(5)]
a["21 jump street"] = [[0 for i in range(10)] for j in range(5)]
a["the departed"] = [[0 for i in range(10)] for j in range(5)]
a["shutter island"] = [[0 for i in range(10)] for j in range(5)]

for m in a:
    q=0
    # print(m)
    for i in range(5):
        for j in range(10):
            q+=1
            a[m][i][j]=q

print(a['avengers'][3][9])
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
tcpCliSock, addr = tcpSerSock.accept()
print("Connection established to:",addr,"\n")

check = True
i = 0
while True:
    arr = [pickle.dumps(a), check]
    tcpCliSock.send(pickle.dumps(arr))
    i += 1
    # print(i)

    data = tcpCliSock.recv(BUFSIZ)
    arr = pickle.loads(data)
    if not data:
        break
    a = pickle.loads(arr[0])
    r = arr[1]
    c = arr[2]
    n = arr[3]
    s=arr[4]

    if n.lower() == "exit":
        break

    if a[n][r][c] == 'X' and r != -1:
        check = False
    elif a[n][r][c] == s and r != -1:
        a[n][r][c] = 'X'
        check = True

tcpCliSock.close()
tcpSerSock.close()

