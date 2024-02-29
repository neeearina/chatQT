import socket

server_socket = socket.socket()
server_socket.bind(("localhost", 8080))
server_socket.listen(1)

while True:
    new_socket, address = server_socket.accept()
    print(" : " + new_socket.recv(1024).decode())
    while True:
        message = input("::")
        new_socket.send(bytes(message, "utf-8"))
        print(" " + new_socket.recv(1024).decode())
        new_socket.close()
