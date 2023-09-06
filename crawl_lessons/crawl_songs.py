import requests
from bs4 import BeautifulSoup
import os
import re
import wget
import crawl_lessons.crawl_movies as cm

# ..\python_workspace\Scripts\pyinstaller.exe - F.\crawl_songs.py - p.\crawl_movies.py
class AppSongs(cm.App):
    def __init__(self):
        super().__init__()
        self.title = "获取歌曲"

    def video_play(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': "gzip, deflate, br",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            'Cookies':"""wyy_uid=a1bc5976-1ed6-47a9-83e4-4efc317851f3; __bid_n=18634c7ae62313b34f4207; FPTOKEN=tpl6cWy1pJOYZYcPMRGvvWRC/w9nv9tSwir8hfER5fWHF1CBRIR5mmbIDnZRHxAhTIZKy5VRI2yqV9VO8Rla1fXYFiLxqhHe1wZQv9z8/Rt4oyPNAgbjx61d2LGnneMkqC4Wfc3jA50scSJX7E7fWDP7pONY8ZsGquU2Br96xsqqzE+q89qcZkGqlEGVIoKAyZOooskOij8mdh18W5VXEeQIwpZ9RJsxQ8NoyP+xNYRlKUP1TEc+3E8xxl/EMyaPuw3Vxs0m1L065mq7UGFS8WBTHno5lrcutIPLCQf4HM4aDe04tbsANNytF1yFxAf+eWJcBiXR/HkgcKnB7RZEkgUJNZp4QuAMUigVwtWnM29ytzz7PYiygq3rfkDv5gD77yqbHmFQhNhYOW9eK8xRpg==|ey2u1uPN0uNH8PoNjW/EKMC4SlIJtHxhUIPw4TapfOQ=|10|e25664e0f68c7b18489d7e522fb9e382; NTES_P_UTID=xS6CbRk0OorRHF5l71oVq0ZP2wzrZKDj|1678668991; P_INFO=wang_lei_hcc@163.com|1678668991|0|mail163|00&99|null&null&null#lin&210100#10#0#0|&0||wang_lei_hcc@163.com; _iuqxldmzr_=32; _ntes_nnid=d328f1ebf5f9b57c1d443ba8269d7abf,1678669003429; _ntes_nuid=d328f1ebf5f9b57c1d443ba8269d7abf; WM_TID=sumAF%2FbJt1JBEQVQARfVeKfAP8ALsYpg; NMTID=00OXCbRA-Gg_-apokoqmzUnrCM62NsAAAGKT9_nhA; WM_NI=NnvCsAoTPuHjTZvBg8RYckjMTBMZVd%2FQYxKi0emI9%2BLtM9Mt1T3WCvaXw%2FvWkB2A37y95Ymhl4nGuYq3OK7qa4Y%2BazCSkMb5q7Uwy6W5B63TqXDXgf9FO2j8%2FJeuRNA8SDc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee92f14bbb9f8e89ef53ace78ea6d85e879b8a82c873958dba96d45eb186afd0ee2af0fea7c3b92a8eb2baa4f24bad8ca096cb629886baa3e6349287ad8ce947989e83bbd570ed8f9799ca63f4bba3aabc2190ac83dad080f38cfdb8c27ea388b9d0f55da99efea2b23dbbe7fbbaf064b0eca2a8f853b3ed81acb67ba3ec97cce472818da5aee13fb3e99b98fc3e95eb8ed7b260b3888cb9e66efb9a81d3e934ed96ab96d14683e89da5e237e2a3; ntes_utid=tid._.lhLmAPhkpE5EAwVQVBPEiGS%252F7QA6UmDS._.0; sDeviceId=YD-O%2FWCDXnjHdFEVkBFBFLQiCT76EBqVmTN; JSESSIONID-WYYY=dQ%5CPoZ65b1AHHJFIhv5erP27tb%2FnxQwIBrD6qstJB3%5ClR4KEkFv7lWYeD8%2Bf8YbK8YgC3AI5wJAE8SG8u%2F9iVxebF4xTkZcfN8BFOgSsJgwmX5ABbqsfN74%2BQuQWdyWGSEJcC67ypvG2%5ClRAlNlj6Oa9FOzMMv%2BJSsbSXi8gP8ik2d0T%3A1693560759857"""
        }

        # 网易云音乐VIP歌曲列表页面
        url = 'https://music.163.com/discover/top/v3'

        # 发送HTTP请求获取页面内容
        response = requests.get(url, headers=headers)

        # 使用BeautifulSoup解析HTML页面
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
        # 查找VIP歌曲列表的HTML元素
        vip_songs = soup.find('div', class_='top-songs').find_all('div', class_='song-item')

        # 创建下载目录
        download_dir = 'VIP_Songs'
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        # 遍历VIP歌曲列表并下载歌曲
        for song in vip_songs:
            song_info = song.find('a', class_='song-name').text  # 获取歌名
            song_url = song.find('a', class_='song-name')['href']  # 获取歌曲链接
            song_id = re.findall(r'id=(.*?)&', song_url)[0]  # 从链接中提取歌曲ID
            download_path = os.path.join(download_dir, f'{song_id}_{song_info}')  # 构建下载路径
            response = requests.get(song_url)  # 发送HTTP请求获取歌曲详情页内容
            soup = BeautifulSoup(response.text, 'html.parser')
            download_url = soup.find('a', class_='Song-download').get('href')  # 获取下载链接
            wget.download(download_url, out=download_path)  # 使用wget下载歌曲

if __name__ == "__main__":
    app = AppSongs()
    app.loop()