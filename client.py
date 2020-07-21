import socket

c= socket.socket()

c.connect(("localhost",3000))

# Loop to interact with server
while True:
    m = c.recv(1024).decode()
    if m != "bye":
        if m == "ok!! bye":
            break
        else:
            print(m)
            msg=input("Type your message:")
            c.send(bytes(msg, "utf-8"))

    else:
        c.send(bytes("ok!!bye","utf8"))
        print("bye")
        break

c.close()


