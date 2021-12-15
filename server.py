import socket
import threading #can be used so clients arent waiting for other clients to use the server#

HEADER =64
PORT =5050
SERVER = socket.gethostbyname(socket.gethostname())      #SERVER ="192.168.56.1"    #Can change to public IP address to work through internet
ADDR = (SERVER, PORT)
FORMAT ='utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #socket type for TCP
server.bind(ADDR)

def handle_client(conn, addr):
    #global message
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        message_length = conn.recv(HEADER).decode(FORMAT)
        if message_length:
             message_length =int(message_length)
             message = conn.recv(message_length).decode(FORMAT)
             if message == DISCONNECT_MESSAGE:
                     connected = False  # or break

             print(f"[{addr}] {message}")
             conn.send("Message received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()            #connection, address    #conn is a socket object
        thread = threading.Thread(target = handle_client, args =(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")


print("[STARTING] server is starting...")
start()
