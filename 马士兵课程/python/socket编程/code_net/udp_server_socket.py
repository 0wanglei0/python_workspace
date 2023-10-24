from socket import *

import cv2
import numpy as np

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

server_socket = socket(AF_INET, SOCK_DGRAM)

host_post = ("192.168.22.25", 8000)
server_socket.bind(host_post)


# 接收图片
image_bytes, client_address = server_socket.recvfrom(64 * 1024)
# print(image_bytes)
# 将字节流转换为图片
# 将字节流转换为图像
image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
# print(image)
# 保存图片
cv2.imwrite('received_image.jpg', image)
cv2.imshow("Received Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# data = server_socket.recvfrom(1024)
# print("server: ", str(data[0].decode("UTF-8")))
server_socket.sendto("image received".encode("UTF-8"), client_address)

server_socket.close()


