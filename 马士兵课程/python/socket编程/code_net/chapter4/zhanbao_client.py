# -*- coding: utf-8 -*-

"""
1.socket 粘包问题
数据之间没有明确的分界线，不能正确读取数据

单个数据包较小，接收方可能读取多个数据包
当整体数据较大，接收方读取了一个包的一部分内容
TCP协议为了效率整合数据小的包合并发送
"""

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('192.168.22.25', 8089))
client_socket.send("hello".encode("utf-8"))
client_socket.send("world".encode("utf-8"))


client_socket.close()
