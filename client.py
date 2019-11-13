from socket import *
import pickle

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:

    data = tcpCliSock.recv(BUFSIZ)
    arr=pickle.loads(data)
    a=pickle.loads(arr[0])
    check=arr[1]

    if check==True:
        for i in a:
            for j in i:
                print(j,end='    ')
            print()
        print()
    else:
        print("Seat already taken. Please try again.\n")  
    
    s=input('> Enter seat you wish to sit in: ')
    if not s:
        break
    seat=int(s)

    row=int(seat/10)
    col=(seat%10)-1
    
    a=pickle.dumps(a)
    arr=[a,row,col]
    # print(arr)
    tcpCliSock.send(pickle.dumps(arr))
    
    # print(pickle.load(data))
    # print(pickle.loads(data))

tcpCliSock.close()
