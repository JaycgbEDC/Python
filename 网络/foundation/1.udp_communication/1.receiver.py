import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # IPV4, udp
s.bind(('', 5000))  # bind sokcet with ip and port
while True:
    data, addr = s.recvfrom(1024)  # 1024 means bufsize, return data(bytes) and addr(ip, port)
    print('received message: {0} from {1} on {2}'.format(data.decode(), addr[1], addr[0]))
    if data.decode().lower() == 'bye':
        break
s.close()