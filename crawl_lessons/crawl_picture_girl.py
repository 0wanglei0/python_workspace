"""
爬取图片，并下载
url:https://pic.netbian.com/4kmeinv/

1.爬取网页的request

2.解析网页 beautifulSoup

"""
import os.path

import requests
from bs4 import BeautifulSoup


#获取网页源代码
def get_html(url):
    resp = requests.get(url)
    resp.encoding = "gbk"
    print(resp.status_code)

    return resp.text


#解析网页
def pull_img(html):
    soup = BeautifulSoup(html, "html.parser")
    images = soup.find_all("img")
    for img in images:
        print(img["src"])
        src = img["src"]
        if "/uploads/" not in src:
            continue
        src = f"https://pic.netbian.com/{src}"
        print(src)

        if not os.path.exists("girl_pictures"):
            os.mkdir("girl_pictures")
        filename = os.path.basename(src)
        with open(f"girl_pictures/{filename}", "wb") as p_file:
            resp_img = requests.get(src)
            p_file.write(resp_img.content)


if __name__ == "__main__":
    urls = ["https://pic.netbian.com/4kmeinv/"] + [
        f"https://pic.netbian.com/4kmeinv/index_{i}.html"
        for i in range(2, 11)
    ]
    for url in urls:
        print("Crawling")
        html = get_html(url)
        pull_img(html)
