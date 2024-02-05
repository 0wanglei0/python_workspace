# -*- coding: utf-8 -*-

from socket import *

# 1.创建server socket,TCP 就要使用SOCK_STREAM了
server_socket = socket(AF_INET, SOCK_STREAM)

# 2.绑定IP和端口，ip设置为‘’可以接受所有ip
host_post = ('', 8088)
server_socket.bind(host_post)

# 3.服务器的socket监听,监听5个客户端
# listen 让服务器端处于被动状态，就可以接受客户端的连接请求，不需要主动调用接口获取请求
server_socket.listen(5)
while True:
    # 4. 等待客户端连接,是线程阻塞的函数，会返回请求socket和客户端地址
    client_socket, client_addr = server_socket.accept()
    print(client_socket)
    # 5.服务器接收客户端消息,recv一半用于TCP协议的接收数据，recvfrom用于UDP，data是字节数据
    data = client_socket.recv(1024)
    print("server received data is ", data.decode("utf-8"))

    # 6.服务器端发送消息给客户端,tcp直接用send，udp一般用sendto
    client_socket.send("Thank you!".encode("utf-8"))

    # 7.关闭套接字
    if len(data) == 0:
        print(client_socket, " close")
        client_socket.close()  # client_socket关闭，意味着当前客户端的服务已经完成

# server_socket.close()  # 整个服务器全部关闭

