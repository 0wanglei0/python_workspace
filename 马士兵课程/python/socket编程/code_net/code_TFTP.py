"""
TFTP
简单文件传输协议
特点：
简单，占用资源小，适合传递小文件，适合局域网进行传输
端口号为69
基于UDP实现

客户端发送下载请求是，需要向服务器端口69发送
服务器若批准请求，则使用一个新的临时的端口进行数据传输


当服务器找到需要的文件后，会立刻打开文件，把文件中的数据通过TFTP协议发送给客户端
如果文件很大，服务器分多次发送，每次会从文件中读取512个字节的数据发送过来

如果数据包发送后没有收到会亏，则说明数据包丢失，可以尝试重发
因为发送的次数有可能会很多，为了让客户端对接收到的数据进行排序，在服务器发送512个字节数据时，多发送2个字节的数据，用来存放序号，
并且在512个字节数据的前面，序号从1开始

若文件不存在，服务器会发送一个错误信息过来，为了区分发送的是文件内容还是错误信息（即操作码），有用了2个字节表述数据包的功能，并且在序号前面
操作码    功能
1       读请求，下载
2       写请求，上传
3       表示数据包，即data
4       确认码，ACK
5       错误码

增加了块编号和操作码，发送一条数据的实际大小是516B
"""

from socket import *
import struct


def download(filename, client):
    # 创建一个新的socket，负责发送文件内部的数据包到客户端
    new_socket = socket(AF_INET, SOCK_DGRAM)
    # 文件内容数据包的计数器
    num = 1
    # 读取文件内容 rb
    try:
        f = open(filename, "rb")
    # 发生异常处理 pack包（操作码5，差错码5，差错信息， 结尾0）
    except:
        error_package = struct.pack('!HH5sb', 5, 5, 'error'.encode("utf-8"), 0)
        new_socket.sendto(error_package, client)
        exit()

    # 如果文件存在，那么把需要的文件内容切成一个个的数据包发送给客户端，每个数据包512字节
    while True:
        # 从文件内容中读取512字节
        read_data = f.read(512)  # 已经是字节数据了，不需要用pack转换了
        # 创建一个数据报,块的编号从1开始
        data_package = struct.pack('!HH', 3, num) + read_data
        new_socket.sendto(data_package, client)
        if 0 < len(read_data) < 512:  # 文件数据读完
            print("客户端 (%s, %s) 文件下载完成!" % (client[0], client[1]))
            f.close()  # 需要释放资源
            exit()  # 线程退出，但是服务不断，断当前线程
        # 服务器接收ACK数据
        recv_ack, _ = new_socket.recvfrom(1024)
        print(recv_ack)
        operator_code, ack_num = struct.unpack('!HH', recv_ack)
        print("客户端 %s confirm %d, %d" % (client, operator_code, ack_num))
        # 如果operator code或者ack num不对，下一个
        if int(operator_code) != 4 or int(ack_num) != num:
            print("client ack error, data lost")
        num += 1


def server():
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(('192.168.22.25', 69))

    while True:
        # 服务器等待客户端发送数据并接收
        recv_data, (client_ip, client_port) = s.recvfrom(1024)
        print(recv_data, client_ip, client_port)
        if struct.unpack('!b5sb', recv_data[-7::]) == (0, b'octet', 0):
            operator_code = struct.unpack('!H', recv_data[:2])
            file_name = recv_data[2:-7].decode("utf-8")

            if operator_code[0] == 1:  # 下载请求
                print("客户端要下载文件，文件名是%s" % file_name)
                download(file_name, (client_ip, client_port))


"""
1.server
创建socket
bind
等待接收消息
收到消息
解析消息

下载
创建新的socket
创建数据包格式
发送数据
接收ACK
继续发送/结束


2.client
创建socket
绑定服务端
创建数据包
发送消息
接收消息
解析消息
完成下载
"""


class Server:
    server_name = ('192.168.22.25', 69)
    client = ()

    def __init__(self):
        self.server_socket = socket(AF_INET, SOCK_DGRAM)
        self.server_socket.bind(self.server_name)

    def recv(self):
        recv_data, client = self.server_socket.recvfrom(1024)
        print(recv_data)
        operator_code = struct.unpack('!H', recv_data[0:2])
        unpack_recv_data = struct.unpack('!b5sb', recv_data[-7:])
        if operator_code[0] == 1 and unpack_recv_data == (0, b'octet', 0):
            filename = recv_data[2: -7].decode("utf-8")
            print(f"客户端{client[0]}请求下载文件{filename}")
            self.download(client, filename)

    @staticmethod
    def download(client, filename):
        download_socket = socket(AF_INET, SOCK_DGRAM)
        send_num = 1
        print(client)
        with open(filename, 'rb') as f:

            while True:
                try:
                    read_data = f.read(512)
                    send_data = struct.pack("!HH", 3, send_num) + read_data
                    download_socket.sendto(send_data, client)
                    print("server send")
                    if len(read_data) < 512:
                        print("Download completed")
                        exit()
                    recv_ack_pack, _ = download_socket.recvfrom(1024)
                    print("server send ", recv_ack_pack)

                    ack_code, ack_num = struct.unpack("!HH", recv_ack_pack[0:4])
                    if ack_code != 4 or ack_num != send_num:
                        print('received data error')
                    send_num += 1
                except Exception as e:
                    print(e)
                    send_data = struct.pack("!HH5s", 5, 5, 'error'.encode("utf-8"))
                    download_socket.sendto(send_data, client)


if __name__ == "__main__":
    s = Server()
    while True:
        s.recv()
