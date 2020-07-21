import socket

s = socket.socket()

print("Socket Created")

s.bind(('localhost', 3000))

s.listen(3)
print("Waiting for connections")

# Loop to interact with client
while True:
    c, addr = s.accept()


    c.send(bytes("Welcome {}".format(addr),'utf-8'))
    while True:
        m=c.recv(1024).decode()
        if m != "bye":
            print(m)
            msg=input("Message:")
            c.send(bytes(msg,"utf-8"))
        else:
            c.send(bytes("ok!! bye","utf-8"))
            print("Left")
            print("Waiting for connections")
            break


    c.close()
