import socket
from socket import *  # 可以省略部分调用中的socket.


# 创建socket，2种，TCP和UDP
# socket.AF_INET  网络通信
# socket.AF_UNIX  本机通信，不常用，相同方式可使用队列或同步消息，互斥锁等实现
# socket.SOCK_STREAM  主要用于TCP协议  socket.SOCKET_DGRAM  用于UDP协议
tcp_socket = socket(AF_INET, SOCK_STREAM)  # tcp socket
print(tcp_socket)

print("start")
"""
1.创建一个UDP协议的socket， 然后发送一条数据到网络上的另一个进程
"""
client_socket = socket(AF_INET, SOCK_DGRAM)

"""
2.定义一个接收消息的目标，(目标ip, 目标port)
"""
server_address = ("127.0.0.1", 8080)

"""
3.准备数据，字符串使用utf-8编码，把数据转成字节数组bytes，否则无法通过协议传输
"""
datas = input("请输入内容：").encode("utf-8")

"""
4.发送数据，sendto(数据, 接收目标)
"""
client_socket.sendto(datas, server_address)

"""
5.关闭socket，释放资源
"""
client_socket.close()
print("over")


"""
UDP是不可靠的，无连接的协议，不能保证成功接收和发送,通讯不需要连接，可以实现广播发送，传输数据大小限制64KB，数据可能会以不同顺序达到接收方

一般用于多点通信和实时的数据业务，比如：语音广播，视频，QQ，TFTP简单文件传送，SNMP 简单网络管理协议
RIP 路由信息协议，如报告股票市场，航空信息等，DNS 域名解释，主要是速度流畅，不卡顿
"""

"""
SocketServer
"""