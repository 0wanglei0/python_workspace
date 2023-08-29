class UrlManager():
    """
    url管理器
    """

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None or len(url) == 0:
            return
        elif url in self.new_urls or url in self.old_urls:
            return
        else:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            if url in self.new_urls or url in self.old_urls:
                continue
            else:
                self.new_urls.add(url)

    def get_url(self):
        if self.has_new_url():
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None

    def has_new_url(self):
        return len(self.new_urls) > 0


if __name__ == "__main__":
    url = "https://www.baidu.com"
    url1 = "https://www.google.com"
    url2 = "https://www.baidu.com"

    urlManager = UrlManager()
    urlManager.add_new_url(url)
    urlManager.add_new_url(url1)
    urlManager.add_new_url(url2)
    print(urlManager.get_url())
