from socket import *
import struct  # 复杂python数据结构，和C语言中数据结构转换
# file_name = input("请输入文件名：")
#
# s = socket(AF_INET, SOCK_DGRAM)  # UDP
#
# # 定义服务器的ip和端口号
# host_port = ("192.168.22.25", 69)
#
# # '!H%dsb5sb' 字符串格式，! 是字符串的开头 H 短整形  s 字符串  %d int类型参数 b 有符号的char bool
# data_package = struct.pack('!H%dsb5sb' % len(file_name), 1, file_name.encode("utf-8"), 0, 'octet'.encode("utf-8"), 0)
# s.sendto(data_package, host_port)
#
# f = open("client_" + file_name, "ab")
#
# while True:
#     # 接收的数据：1.数据包 2.error数据
#     recv_data, (server_ip, server_port) = s.recvfrom(1024)
#     server = (server_ip, server_port)
#     print(recv_data)
#     print(server)
#     operation_code, pack_num = struct.unpack('!HH', recv_data[0: 4])
#     if int(operation_code) == 5:
#         print("error message: ", recv_data[4:].decode("utf-8"))
#         exit()
#     # 保存文件内容
#     f.write(recv_data[4:])
#
#     if len(recv_data) < 516:
#         print("file received completed")
#         exit()
#
#     ack_package = struct.pack("!HH", 4, pack_num)
#     s.sendto(ack_package, server)


class TFTP_Client:
    server_host = ('192.168.22.25', 69)
    client = socket(AF_INET, SOCK_DGRAM)

    def __init__(self):
        self.f = None

    # data_package = struct.pack('!H%dsb5sb' % len(file_name), 1, file_name.encode("utf-8"), 0, 'octet'.encode("utf-8"), 0)
    # s.sendto(data_package, host_port)
    def send_to(self, file_name):
        self.f = open('client_' + file_name, 'ab')
        data_package = struct.pack('!H%dsb5sb' % len(file_name), 1,
                                   file_name.encode("utf-8"), 0, 'octet'.encode('utf-8'), 0)
        self.client.sendto(data_package, self.server_host)

    def receive(self):
        while True:
            recv, server = self.client.recvfrom(1024)
            print(recv)

            operation_code, pack_num = struct.unpack('!HH', recv[0:4])
            if int(operation_code) == 5:
                print('error')
                return

            self.f.write(recv[4:])

            if len(recv) < 516:
                print('completed')
                # exit()
                return

            ack_package = struct.pack("!HH", 4, pack_num)
            self.client.sendto(ack_package, server)


if __name__ == "__main__":
    client_ftp = TFTP_Client()
    # 循环发送
    while True:
        filename = input("please input filename: ")
        client_ftp.send_to(filename)
        client_ftp.receive()

