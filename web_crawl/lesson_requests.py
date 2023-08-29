"""
request网页下载库

requests.get/post(url, params, data, headers, timeout, verify, allow_redirects,cookies)

url: 目标网页url
params:字典形式，设置url后面的参数，比如?id=123&name=wang
data:字典或者字符串，一般用于post方法提交数据
headers:设置user-agent等请求头
timeout:超时时间，单位是秒
verify:True/false,是否进行HTTPS证书验证，默认是，需要自己设置证书地址
allow_redirects:True、FALSE是否让requests做重定向处理，默认True
cookies:附带本地的Cookies数据

r = requests.get/post(url)
查看状态码
r.status_code
查看当前编码及变更编码
r.encoding
查看返回的网页内容
r.text
查看返回的HTTP的headers
r.headers
查看实际访问的URL
r.url
以字节的方式返回内容，比如下载图片
r.content
服务端要写入本地的Cookies数据
r.cookies
"""