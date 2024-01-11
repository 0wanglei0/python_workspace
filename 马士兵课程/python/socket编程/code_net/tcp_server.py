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

# 4. 等待客户端连接,是线程阻塞的函数，会返回请求socket和客户端地址
client_socket, client_addr = server_socket.accept()
