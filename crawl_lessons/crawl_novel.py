"""
批量爬取全本小说

1.爬取目录页面，得到所有章的链接地址
·89文学网 龙王传说
http://www.89wxw.cn/0_9/

2.依次爬取每章的小说正文
1第一千八百六十八章 龙神之心
http://www.89wxw.cn/0_9/2836319.html

"""
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

def get_novel_chapters():
    root_url = "http://www.89wxw.cn/0_9/"
    r = requests.get(root_url)
    r.encoding = "gbk"
    soup = BeautifulSoup(r.text, "html.parser")

    print(soup)
    data = []
    for dd in soup.find_all("dd"):

        link = dd.find("a")
        if not link:
            continue

        data.append(("http://www.89wxw.cn/0_9/%s"%link['href'], link.get_text()))
    return data


def get_chapter_content(url):
    r = requests.get(url)
    r.encoding = "gbk"
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.find("div", id="content").get_text()


chapters = get_novel_chapters()
for chapter in chapters:
    print(chapter)
    url, title = chapter
    with open("%s.txt"%title, "w") as fout:
        fout.write(get_chapter_content(url))
