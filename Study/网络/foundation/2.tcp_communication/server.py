""" robot chatting simulating """
import socket


words = {'my name': 'lx', 'sex': 'man', 'age': '23'}
host, port = '', 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print('Listening at port: ', port)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print('Received message: ', data)
    conn.sendall(words.get(data, 'Nothing').encode())
conn.close()
s.close() 