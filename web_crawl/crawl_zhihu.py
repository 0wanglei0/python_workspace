# -*- coding: utf-8 -*-

import requests

try:
    import cookielib

except:
    import http.cookiejar as cookielib
import re
import time
import os.path

try:
    from PIL import Image
except:
    pass
from bs4 import BeautifulSoup

# 构造 Request headers
# 从配置表获取
# agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3294.6 Safari/537.36'
#
# headers = {
#
#     "Host": "www.zhihu.com",
#
#     "Referer": "https://www.zhihu.com/",
#
#     'User-Agent': agent
#
# }

cookie_file = 'cookie.txt'
header = {
    'Host': 'www.zhihu.com',
    'Referer': 'http://www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
# 使用登录cookie信息

session = requests.session()

session.cookies = cookielib.LWPCookieJar(filename=cookie_file)

try:

    session.cookies.load(ignore_discard=True)

except:

    print("Cookie 未能加载")


def get_xsrf():
    '''_xsrf 是一个动态变化的参数'''

    index_url = 'https://www.zhihu.com'

    # 获取登录时需要用到的_xsrf

    index_page = session.get(index_url, headers=header)

    # html = index_page.cookies

    # pattern = r'name="_xsrf" value="(.*?)"'
    #
    # # 这里的_xsrf 返回的是一个list
    #
    # _xsrf = re.findall(pattern, html)
    xsrf = index_page.request._cookies.get("_xsrf")
    return xsrf


# 获取验证码

def get_captcha():
    t = str(int(time.time() * 1000))

    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"

    r = session.get(captcha_url, headers=header)

    with open('captcha.jpg', 'wb') as f:

        f.write(r.content)

        f.close()

    # 用pillow 的 Image 显示验证码

    # 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入

    try:

        im = Image.open('captcha.jpg')

        im.show()

        im.close()

    except:

        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))

    captcha = input("please input the captcha\n>")

    return captcha


def isLogin():
    # 通过查看用户个人信息来判断是否已经登录

    url = "https://www.zhihu.com/settings/profile"

    login_code = session.get(url, headers=header, allow_redirects=False).status_code
    print(login_code)
    if login_code == 200:

        return True

    else:

        return False


def login(secret, account):
    # 通过输入的用户名判断是否是手机号

    if re.match(r"^1\d{10}$", account):

        print("手机号登录 \n")

        post_url = 'https://www.zhihu.com/login/phone_num'

        postdata = {
            '_xsrf': get_xsrf(),

            'password': secret,

            'remember_me': 'true',

            'phone_num': account,

        }

    else:

        if "@" in account:

            print("邮箱登录 \n")

        else:

            print("你的账号输入有问题，请重新登录")

            return 0

        post_url = 'https://www.zhihu.com/login/email'

        postdata = {

            '_xsrf': get_xsrf(),

            'password': secret,

            'remember_me': 'true',

            'email': account,

        }

    try:

        # 不需要验证码直接登录成功

        login_page = session.post(post_url, data=postdata, headers=header)

        login_code = login_page.text

        print(login_page.status_code)

        print(login_code)

    except:

        # 需要输入验证码后才能登录成功

        postdata["captcha"] = get_captcha()

        login_page = session.post(post_url, data=postdata, headers=header)

        login_code = eval(login_page.text)

        print(login_code['msg'])
    cookie_path = cookie_file
    session.cookies.save(cookie_path)


# try:
#
#     input = raw_input
#
# except:
#
#     pass


##将主页面的用户提问print到shell上

def getpage(url2):
    mainpage = session.get(url2, headers=header)

    soup = BeautifulSoup(mainpage.text, 'html.parser')
    print(soup)

    tags = soup.find_all("a", class_="question_link")

    print(tags)

    for tag in tags:
        print(tag.string)


def get_login_cookie(url):
    '''
    获取保存cookie
    :param url:
    :return:
    '''

    if not os.path.exists(cookie_file):
        account = input('请输入你的用户名\n>  ')
        secret = input("请输入你的密码\n>  ")
        user_name = account
        passwd = secret
        login(passwd, user_name)
    try:
        cookie_jar = cookielib.LWPCookieJar(cookie_file)
        cookie_jar.load(ignore_discard=True, ignore_expires=True)
        print('Load cookie succeeded')
    except cookielib.LoadError:
        return None
    else:
        cookie_d = {}
        for cookie in cookie_jar:
            domain = cookie.domain
            if url.find(domain) > 0:
                cookie_d[cookie.name] = cookie.value
        return cookie_d


if __name__ == '__main__':

    if isLogin():

        print('您已经登录')

        url2 = 'https://www.zhihu.com'

        getpage(url2)

    else:

        account = '15041264842'

        secret = 'wls999@999'

        login(secret, account)

        print('您已经登录')

        url2 = 'https://www.zhihu.com'

        getpage(url2)