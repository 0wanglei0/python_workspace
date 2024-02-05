# -*- coding: utf-8 -*-
from socket import *
import SparkApi

# 以下密钥信息从控制台获取
appid = "0d0149a2"  # 填写控制台中获取的 APPID 信息
api_secret = "MGJlZDdhM2EzZjZlODE5ZjA4Nzk1NGVm"  # 填写控制台中获取的 APISecret 信息
api_key = "caf7552644e58d5a8a1515b95816c3bd"  # 填写控制台中获取的 APIKey 信息

# 用于配置大模型版本，默认“general/generalv2”
domain = "generalv3.5"  # v1.5版本
# domain = "generalv2"    # v2.0版本
# 云端环境的服务地址
Spark_url = "ws://spark-api.xf-yun.com/v3.5/chat"  # v1.5环境的地址
# Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址


text = []


# length = 0

def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text


def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length


def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text


if __name__ == '__main__':
    text.clear()
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', 8088))

    server_socket.listen(5)
    client_list = []
    while True:
        client_socket, host = server_socket.accept()
        print("client_socket: ", client_socket, "host:", host)
        client_list.append(client_socket)
        while True:
            data = client_socket.recv(1024)

            if len(data) == 0:
                print("客户端拒绝继续聊天")
                break

            print(data.decode("utf-8"))

            print(data.decode("utf-8"))

            send_data = input("answer: ")
            client_socket.send(send_data.encode("utf-8"))

            # question = checklen(getText("user", data.decode("utf-8")))
            # SparkApi.answer = ""
            # print("星火:", end="")
            # SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
            # getText("assistant", SparkApi.answer)
            #
            # # send_data = input("answer: ")
            # client_socket.send(SparkApi.answer.encode("utf-8"))

        client_socket.close()
        client_list.remove(client_socket)
        if len(client_list) == 0:
            break

    server_socket.close()
    print("结束运行")

