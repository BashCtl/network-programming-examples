import socket

s = socket.socket()
print('Socket succesfully created')
port = 55442
s.bind(('', port))
print(f'socket binded to port:{port}')
s.listen(5)
print('Socket is listening')

while True:
    conn, addr = s.accept()
    print(f'Got connection from {addr}')
    message = ('Thank you for connecting')
    conn.send(message.encode())
    conn.close()
