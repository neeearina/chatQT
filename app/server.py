import select
import socket

server_socket = socket.socket()
server_socket.bind(("localhost", 8080))
server_socket.listen(1)
server_socket.settimeout(1)
client_sockets = []

while True:
    try:
        new_socket, address = server_socket.accept()
    except OSError:
        pass
    else:
        client_sockets.append(new_socket)
    finally:
        for client_socket in client_sockets:
            cl_r, _, _ = select.select(client_sockets,
                                       client_sockets,
                                       client_sockets, 0)
            if client_socket in cl_r:
                for client_socket2 in client_sockets:
                    client_socket2.send(client_socket.recv(1024))
