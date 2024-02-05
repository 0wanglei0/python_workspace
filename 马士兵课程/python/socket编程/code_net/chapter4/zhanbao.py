# -*- coding: utf-8 -*-

"""
1.socket 粘包问题
数据之间没有明确的分界线，不能正确读取数据

单个数据包较小，接收方可能读取多个数据包
当整体数据较大，接收方读取了一个包的一部分内容
TCP协议为了效率整合数据小的包合并发送
"""

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('', 8089))
server_socket.listen(5)
new_socket, client_addr = server_socket.accept()
data1 = new_socket.recv(1024)
print(data1)
data2 = new_socket.recv(1024)
print(data2)

new_socket.close()
server_socket.close()