from socket import *
import pickle
from getpass import getpass

HOST = "127.0.0.1"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

user = dict()

print("TIMINGS\n")
print("1. Jurassic Park- 10:15")
print("2. Avengers- 12")
print("3. The Departed- 14:30")
print("4. Shutter Island- 16:00")
print("5. 21 Jump Street- 19:00\n")

movie = [
    "jurassic park",
    "avengers",
    "the departed",
    "shutter island",
    "21 jump street",
]

print("Please login to continue.")
uname = input("Username: ")
print("This is not an existing username. Please sign up.")
uname = input("Username: ")
pswd = getpass("Password: ")
print()
user[uname] = pswd
login = True


def rec():
    data = tcpCliSock.recv(BUFSIZ)
    arr = pickle.loads(data)
    a = pickle.loads(arr[0])
    check = arr[1]
    return (a, check)


def sen(s, a, name):

    seat = int(s)
    if seat > 50:
        print("Please enter a valid seat number.\n")
        return 0

    if seat != -1:
        row = int(seat / 10)
        col = (seat % 10) - 1
    else:
        row = -1
        col = -1
    a = pickle.dumps(a)
    arr = [a, row, col, name]
    # print(arr)
    tcpCliSock.send(pickle.dumps(arr))
    return 1

t=1
decide = -1
a, check = rec()
name = "avengers"
while True:
    if login:
        decide *= -1

        name = "avengers"
        sen(-1, a, name)
        a, check = rec()

        if t==1:
            print('Type "logout" to logout and "exit" to exit.\n')
            t=0

        if decide == 1:
            name = input("Enter movie name. \n")

            if name.lower() == "logout":
                login = False
                continue
            elif name.lower() == "exit":
                sen(-1, a, name)
                break

            if name.lower() not in movie:
                print(
                    "Sorry that movie does not seem to be playing today. Please select one from the list.\n"
                )
                continue

            if check == True:
                for i in a[name]:
                    for j in i:
                        print(j, end="    ")
                    print()
                print()
            s = input("Enter seat you wish to sit in. ")

            flag = sen(s, a, name)
            if flag:
                a, check = rec()
            if check == True and flag:
                print("Booking done succesfully!\n")

            while check == False:
                print(
                    "Sorry that does not seem to be a valid seat. Please try again.\n"
                )
                s = input("Enter seat you wish to sit in. ")
                flag = sen(s, a, name)
                if flag:
                    a, check = rec()
                if check == True and flag:
                    print("Booking done succesfully!\n")

        elif decide == -1:
            while name.lower() not in movie:
                print(
                    "Sorry that movie does not seem to be playing today. Please select one from the list."
                )
                name = input("Enter MMovie name. \n")

    elif not login:
        print("You seem to be signed out. Please login to continue.")
        while not login:
            uname = input("Username: ")
            if uname not in user:
                print("User does not exist. Please sign up.")
                uname = input("Username: ")
                pswd = getpass("Paswword: ")
                user[uname] = pswd
                login = True
            elif uname in user:
                pswd = getpass("Paswword: ")
                if user[uname] == pswd:
                    print("Login Successful!")
                    login = True
                    continue
                else:
                    print("User already exists. \n")
            else:
                pswd = getpass("Password: ")
                if user[uname] == pswd:
                    print("Login Successful!\n")
                    login = True
                    continue
                else:
                    print("Incorrect Password.")

tcpCliSock.close()
