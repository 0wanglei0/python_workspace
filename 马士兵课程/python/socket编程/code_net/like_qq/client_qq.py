# -*- coding: utf-8 -*-
from socket import *
import _thread as thread

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(("192.168.22.25", 8088))

# def run(ws, *args):
#     accept_data = client_socket.recv(1024)
#     ws.send(data)

while True:
    send_data = input("ask:")
    if send_data == 'q':
        break
    client_socket.send(send_data.encode("utf-8"))

    # thread.start_new_thread(run, (ws,))

    accept_data = client_socket.recv(1024)
    print(accept_data.decode("utf-8"))
    if len(accept_data) == 0:
        break

client_socket.close()



