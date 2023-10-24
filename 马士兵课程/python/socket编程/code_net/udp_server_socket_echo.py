from socket import *

"""
SocketServer
"""

"""
流程：
1.创建socket
2.bind
3.一直阻塞到收到客户端数据
4.处理请求
5.sendto
6.close

"""

"""
echo服务的应用，是一种非常有用的用于调试和检测的工具，该协议接收到什么鸳鸯返回，类似于日常的：回声，及存在回显

"""

server_socket = socket(AF_INET, SOCK_DGRAM)

# 如果真是的物理小型服务器，ip地址有很多，任何本机的ip地址绑定只用‘’
host_post = ("", 8000)
server_socket.bind(host_post)

while True:
    data = server_socket.recvfrom(3 * 1024)
    origin_data = data[0].decode("UTF-8")
    print("server: ", data[0].decode("UTF-8"))
    server_socket.sendto(origin_data.encode("UTF-8"), data[1])
    if str(data[0].decode("UTF-8")) == "q":
        break
server_socket.close()
