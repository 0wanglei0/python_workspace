# -*- coding: utf-8 -*-
from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)

# 客户端发送连接的请求（不是传输数据的请求）

# 目标服务器的ip和端口号
server_host = ('192.168.22.25', 8088)

client_socket.connect(server_host)

while True:
    send_data = input("请输入：")
    if send_data == "q":
        break

    client_socket.send(send_data.encode("utf-8"))

    # 接收服务器返回的数据
    recv_data = client_socket.recv(1024).decode("utf-8")
    print("客户端接收数据：", recv_data)


# close后服务器端不会阻塞，接收的数据长度是0，服务器端可以根据接收数据长度判断是否关闭连接了
client_socket.close()
