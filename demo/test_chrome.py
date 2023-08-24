import os

from selenium import webdriver

print(0)
# print("C:/Program Files/Google/Chrome/Application/chromedriver.exe".replace("/", "\\"))
# os.system("chromedriver.exe")
browser = webdriver.Chrome()
# print(1)

browser.get("http://redmine-pa.mxnavi.com/workreports?utf8=%E2%9C%93&report_state=3&time_begin%5B%5D=2023-08-01&time_end%5B%5D=2023-08-25&commit=%E6%9F%A5%E8%AF%A2")
