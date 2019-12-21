import socket
import time

PORT = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), PORT))
s.listen(100)

while True:
    clientsocket, address = s.accept()
    print(f"live connection from {address}")
    clientsocket.close()
	
