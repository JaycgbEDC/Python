import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('127.0.0.1', 50007))
except Exception as e:
    print('Server not found or not open')
    sys.exit()
while True:
    c = input('Input the content you want to send: ')
    s.sendall(c.encode())
    data = s.recv(1024).decode()
    print('Received: ', data)
    if c.lower() == 'bye':
        break
s.close()