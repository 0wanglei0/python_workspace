import socket
from socket import *  # 可以省略部分调用中的socket.
import cv2
import numpy as np

"""
1.客户端无限发送
2.客户端如果发送一个标志位，则退出客户端
3.服务器端收到什么就返回什么
"""


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
server_address = ("192.168.22.25", 8000)

# 读取图片
image = cv2.imread('1698160724065.jpg', cv2.IMREAD_COLOR)
# cv2.imshow("Received Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # 将图片转换为字节流
# image_bytes = cv2.imencode('.jpg', image)[1].tobytes()
# 将图片转换为字节流
_, buffer = cv2.imencode('.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 85])
image_bytes = buffer.tobytes()

# 保存图片
# cv2.imwrite('received_image.jpg', image)
# cv2.imshow("Received Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""
3.准备数据，字符串使用utf-8编码，把数据转成字节数组bytes，否则无法通过协议传输
"""
while True:
    datas = input("请输入内容：").encode("utf-8")
    print(datas)

    if "1" == str(datas.decode("UTF-8")):
        client_socket.sendto(image_bytes, server_address)
        continue

    """
    4.发送数据，sendto(数据, 接收目标)
    """
    client_socket.sendto(datas, server_address)
    data = client_socket.recvfrom(1024)
    print("返回的数据是：", str(data[0].decode("UTF-8")))
    if str(data[0].decode("UTF-8")) == "q":
        break

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

