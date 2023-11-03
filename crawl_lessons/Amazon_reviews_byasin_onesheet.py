#!/usr/bin/env python
# coding: utf-8

# In[5]:


# %load Test-fasongban.py
import math
import re
import time

import requests
import pandas as pd
from scrapy import Selector


class AmazonReviewScraper():
    headers = {
        'authority': 'www.amazon.co.jp',
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0"
    }

    def __init__(self, asin_list):
        self.asin_list = asin_list

    import re

    def extract_integer_from_string(self, s: str) -> int:
        """
        从字符串中提取数字并返回其整数部分。

        :param s: 输入的字符串
        :return: 提取出的整数或者None（如果没有找到数字）
        """
        match = re.search(r'(\d+\.\d+)', s)
        if match:
            number = float(match.group(1))
            return int(number)
        else:
            return None

    def extract_total_reviews(self, asin):
        spiderurl = f'https://www.amazon.co.jp/hz/reviews-render/ajax/reviews/get/ref=cm_cr_getr_d_paging_btm_next_1'
        post_data = {
            "sortBy": "recent",
            "reviewerType": "all_reviews",
            "pageSize": "10",
            "asin": asin,
            "pageNumber": 1,
            "reftag": "cm_cr_getr_d_paging_btm_next_1",
            "scope": "reviewsAjax1"
        }
        # res = self.get_res(spiderurl, self.headers, post_data)
        res = self.get_res(spiderurl, self.headers, post_data)
        if res:
            # print("Response content:", res)  # 打印返回的内容
            match = re.search(r'レビュー付き:(\d+)', res)
            if match:
                return int(match.group(1))
        return 0

    def get_reviews(self, asin):
        total_reviews = self.extract_total_reviews(asin)
        max_page = math.ceil(total_reviews / 10)  # calculate the num of pages
        print(max_page)
        reviews = []
        for page in range(1, max_page + 1):
            post_data = {
                "sortBy": "recent",
                "reviewerType": "all_reviews",
                "pageSize": "10",
                "asin": asin,
                "pageNumber": page,
                "reftag": f"cm_cr_getr_d_paging_btm_next_{page}",
                "scope": f"reviewsAjax{page}"
            }
            spiderurl = f'https://www.amazon.co.jp/hz/reviews-render/ajax/reviews/get/ref=cm_cr_getr_d_paging_btm_next_{page}'
            # res = self.get_res(spiderurl,self.headers, post_data)
            res = self.get_res(spiderurl, self.headers, post_data)
            if res:
                contents = res.split('&&&')
                for content in contents:
                    infos = content.split('","')
                    info = infos[-1].replace('"]', '').replace('\\n', '').replace('\\', '')
                    if 'data-hook="review"' in info:
                        sel = Selector(text=info)
                        point = sel.xpath('//span[@class="a-icon-alt"]/text()').extract_first()
                        star_count = self.extract_integer_from_string(point)
                        star_str = '\u2605' * star_count

                        amazon_account_link = sel.xpath('//a[@class="a-profile"]/@href').extract_first()
                        if amazon_account_link:
                            amazon_account_link = 'https://www.amazon.co.jp' + amazon_account_link.split('/ref=')[0]
                        else:
                            amazon_account_link = None

                        review_date = sel.xpath('//span[@data-hook="review-date"]/text()').extract_first()
                        #if '2023年8月' in review_date:  # 检查日期是否为8月份
                        data = {
                                '星の数': star_str,
                                'AmazonAccount': amazon_account_link,
                                '投稿者名': sel.xpath('//span[@class="a-profile-name"]/text()').extract_first(),
                                'ReviewDate': review_date,
                                'Amazonで購入': sel.xpath(
                                    '//span[@class="a-size-mini a-color-state a-text-bold"]/text()').extract_first(),
                                '投稿本文': sel.xpath('//span[@data-hook="review-body"]/span/text()').extract_first()
                        }
                        reviews.append(data)
        return reviews


    def get_res(self, url, headers, post_data, retries=3):
        for _ in range(retries):
            try:
                res = requests.post(url, headers=headers, data=post_data)
                if res.status_code == 200:
                    return res.content.decode('utf-8')
                else:
                    print(f'Request failed with status code: {res.status_code}')
            except Exception as e:
                if _ == retries - 1:  # last try to print error
                    print(f'Final request error after {retries} attempts: {e}')
                else:
                    print(f'Request error: {e}. Retrying...')
                time.sleep(10)  # wait for 10 secs
        return None

    def save_to_excel(self):
         ## 括号内放入输出的文件名称 ## ##
        with pd.ExcelWriter('20231031_output.xlsx') as writer: 
            for asin in self.asin_list:
                reviews = self.get_reviews(asin)
                df = pd.DataFrame(reviews)
                df.to_excel(writer, sheet_name=asin, index=False)


if __name__ == '__main__':
    ## 括号内放入读取的文件名称 ##
    raw_data = pd.read_excel("./20231031_XM.xlsx")
    asins = raw_data['ASIN'].dropna().unique().tolist()
    scraper = AmazonReviewScraper(asins)
    # print(scraper.extract_total_reviews(asins))
    scraper.save_to_excel()



# In[6]:


workbook_url = "20231031_output.xlsx"
all_dfs = pd.read_excel(workbook_url, sheet_name=None)

all_dfs_combined = pd.DataFrame()
for name, frame in all_dfs.items():
    frame['ASIN'] = name
    all_dfs_combined = all_dfs_combined.append(frame)
#all_dfs_combined.head()

#all_dfs_combined = all_dfs_combined[['ASIN', '星の数', 'AmazonAccount', '投稿者名', 'ReviewDate', 'Amazonで購入', '投稿本文', 'sheet']]
all_dfs_combined = all_dfs_combined[['ASIN', '星の数', 'AmazonAccount', '投稿者名', 'ReviewDate', 'Amazonで購入', '投稿本文']]
all_dfs_combined.head()
all_dfs_combined.to_excel("./20231031_output2.xlsx")


# In[6]:


all_dfs_combined.head()


# In[58]:




