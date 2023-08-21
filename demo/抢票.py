import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

print(0)

browser = webdriver.Chrome()
print(1)
browser.get("https://www.jd.com/")
time.sleep(3)
print(2)

browser.find_element(By.LINK_TEXT, "你好，请登录").click()
print("please scan the QR")
time.sleep(8)
print(3)

browser.get("https://cart.jd.com/cart_index")
time.sleep(5)
print(4)

while True:
    if browser.find_element(By.CLASS_NAME, "jdcheckbox"):
        browser.find_element(By.CLASS_NAME, "jdcheckbox").click()
        break

while True:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    print(now)
    if now >= '2023-08-21 14:15:00':
        while True:
            try:
                if browser.find_element(By.LINK_TEXT, "去结算"):
                    browser.find_element(By.LINK_TEXT, "去结算").click()
                    speaker.Speak(f"成功拉")
                    break
            except:
                pass
