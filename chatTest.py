import requests
from bs4 import BeautifulSoup
import datetime
today = datetime.date.today().strftime('%Y-%m-%d')
url = 'https://news.qq.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#找到新闻的列表
news_list = soup.find('ul', attrs={'class': 'list'})
#遍历列表，打印新闻标题及链接
for news in news_list.find_all('li'):
    date = news.find('span', attrs={'class': 'time'}).text.split(' ')[0]
    if date != today:
        continue
    title = news.find('a').text
    link = news.find('a')['href']
    print(title)
    print(link)