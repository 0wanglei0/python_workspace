# -*- coding: utf-8 -*-
import _thread as thread
import json
from datetime import datetime
from time import mktime
from wsgiref.handlers import format_date_time


cur_time = datetime.now()
date = format_date_time(mktime(cur_time.timetuple()))
# 假使生成的date和下方使用的date = Fri, 05 May 2023 10:43:39 GMT

tmp = "host: " + "spark-api.xf-yun.com" + "\n"
tmp += "date: " + date + "\n"
tmp += "GET " + "/v3.5/chat" + " HTTP/1.1"
"""上方拼接生成的tmp字符串如下
host: spark-api.xf-yun.com
date: Fri, 05 May 2023 10:43:39 GMT
GET /v3.5/chat HTTP/1.1
"""

import hmac
import hashlib
# 此处假设APISecret = MGJlZDdhM2EzZjZlODE5ZjA4Nzk1NGVm
APISecret = "MGJlZDdhM2EzZjZlODE5ZjA4Nzk1NGVm"

tmp_sha = hmac.new(APISecret.encode('utf-8'), tmp.encode('utf-8'), digestmod=hashlib.sha256).digest()
"""此时生成的tmp_sha结果如下
b'\xcf\x98\x07v\xed\xe9\xc5Ux\x0032\x93\x8e\xbb\xc0\xe5\x83C\xda\xba\x05\x0c\xd1\xdew\xccN7?\r\xa4'
"""

import base64
signature = base64.b64encode(tmp_sha).decode(encoding='utf-8')
"""此时生成的结果如下
z5gHdu3pxVV4ADMyk467wOWDQ9q6BQzR3nfMTjc/DaQ==
"""

# 假设步骤1控制台获取的APIKey=caf7552644e58d5a8a1515b95816c3bd
APIKey = "caf7552644e58d5a8a1515b95816c3bd"
authorization_origin = f"api_key='{APIKey}', algorithm='hmac-sha256', headers='host date request-line', signature='{signature}'"
"""此时生成的authorization_origin字符串如下
api_key="addd2272b6d8b7c8abdd79531420ca3b", algorithm="hmac-sha256", headers="host date request-line", signature="z5gHdu3pxVV4ADMyk467wOWDQ9q6BQzR3nfMTjc/DaQ="
"""

authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
"""此时生成的authorization如下
YXBpX2tleT0iYWRkZDIyNzJiNmQ4YjdjOGFiZGQ3OTUzMTQyMGNhM2IiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iejVnSGR1M3B4VlY0QURNeWs0Njd3T1dEUTlxNkJRelIzbmZNVGpjL0RhUT0i
"""

from urllib.parse import urlencode

v = {
		"authorization": authorization, # 上方鉴权生成的authorization
        "date": date,  # 步骤1生成的date
    	"host": "spark-api.xf-yun.com" # 请求的主机名，根据具体接口替换
}
url = "wss://spark-api.xf-yun.com/v3.5/chat?" + urlencode(v)
"""生成的最终url如下
wss://spark-api.xf-yun.com/v1.1/chat?authorization=YXBpX2tleT0iYWRkZDIyNzJiNmQ4YjdjOGFiZGQ3OTUzMTQyMGNhM2IiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iejVnSGR1M3B4VlY0QURNeWs0Njd3T1dEUTlxNkJRelIzbmZNVGpjL0RhUT0i&date=Fri%2C+05+May+2023+10%3A43%3A39+GMT&host=spark-api.xf-yun.com
"""

# 收到websocket错误的处理
def on_error(ws, error):
    print("### error:", error)


# 收到websocket关闭的处理
def on_close(ws,one,two):
    print(" ")


# 收到websocket连接建立的处理
def on_open(ws):
    thread.start_new_thread(run, (ws,))


def run(ws, *args):
    data = json.dumps(gen_params(appid=ws.appid, domain= ws.domain,question=ws.question))
    ws.send(data)


# 收到websocket消息的处理
def on_message(ws, message):
    # print(message)
    data = json.loads(message)
    code = data['header']['code']
    if code != 0:
        print(f'请求错误: {code}, {data}')
        ws.close()
    else:
        choices = data["payload"]["choices"]
        status = choices["status"]
        content = choices["text"][0]["content"]
        print(content,end ="")
        global answer
        answer += content
        # print(1)
        if status == 2:
            ws.close()


def gen_params(appid, domain,question):
    """
    通过appid和用户的提问来生成请参数
    """
    data = {
        "header": {
            "app_id": appid,
            "uid": "1234"
        },
        "parameter": {
            "chat": {
                "domain": domain,
                "temperature": 0.5,
                "max_tokens": 2048
            }
        },
        "payload": {
            "message": {
                "text": question
            }
        }
    }
    return data


import websocket  # 使用websocket_client

websocket.enableTrace(False)

ws = websocket.WebSocketApp(url, on_message=on_message, on_error=on_error, on_close=on_close, on_open=on_open)
