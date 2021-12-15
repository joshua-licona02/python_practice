import socket

HEADER =64
PORT =5050
FORMAT ='utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(message):
    msg =message.encode(FORMAT)
    message_length =len(msg)
    send_length = str(message_length).encode(FORMAT)
    send_length+= b' ' *(HEADER-len(send_length))
    client.send(send_length)
    client.send(msg)
    print(client.recv(2048).decode(FORMAT))

send("Hello!")
input()
send("Hello world!")
input()
send("Hello Joshua!")

send(DISCONNECT_MESSAGE)