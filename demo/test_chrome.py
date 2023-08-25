import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree

# 'Cookie': '_redmine_session=RmlHYW03ZXo3MGt0dWpEUjdEVkxUVk50YUxUb0RXT21qT05MNzN3eDFQck1yNElkSzAzWVFheGlOK3A3OGhrRVVYMzdXcGplMzU1cHJjd0tSRmpJa3VHT2R3RzRiVWZWaFJycGVIUnpvV2NxWjRvWWhmRS9FL2lpcVFFUjUvYWhsbW9WVVc1U3lXM0JxV1Y3NDBmeGpXVW9oWkNPcVN2dVJRSjcvMlpaZTRpTFYrQnJqNE50RWJCd2htcmpwWnprcnA1WUxmbG53QVVqZ1hLdWVrblAySkFCbUJFeU5lRG1qdTZSTlFKSGpoL2NzWnhaSmxFeFY4Skc4T294VGNyNGRlUS9ZV1dWTE9JMXJ2ZFJyQ2VVU0lQbUVXN1cvay9ncmovVGFCNi9xZEVwMkQ5VnhXWk42MllkUm9VMWMwaHctLVRZS0p6VytJUWQxQkt1TG5LVUd0aEE9PQ%3D%3D--667c38daec557cd0cd0cae9ba170c96cc77eef91',

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding': "gzip, deflate",
'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

def test_url():
    url = "http://redmine-pa.mxnavi.com/login?username=wangleic&password=Xiaoting521&login=%E7%99%BB%E5%BD%95"
    response = requests.post(url, headers = headers)
    print(response)
    cookies = requests.utils.dict_from_cookiejar(response.cookies)
    print(cookies)


def auto_login():
    # print(1)

    # today = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    # print(today)
    # first_day_of_month = time.strftime("%Y-%m", time.localtime(time.time()))
    # first_day_of_month = first_day_of_month + "-1"
    # print(first_day_of_month)
    # url = "http://redmine-pa.mxnavi.com/workreports?utf8=%E2%9C%93&report_state=3&time_begin%5B%5D=" + str(first_day_of_month) + "&time_end%5B%5D="+ today + "&commit=%E6%9F%A5%E8%AF%A2"
    # browser.get(url)
    #
    # username = browser.find_element(By.ID, "username")
    # password = browser.find_element(By.ID, "password")
    # login_button = browser.find_element(By.NAME, "login")
    # print(username)
    # print(password)
    # if username:
    #     # username.send_keys(input("用户名:"))
    #     username.send_keys("wangleic")
    #     # password.send_keys(input("密码:"))
    #     password.send_keys("Xiaoting521")
    #     login_button.click()
    #
    # time.sleep(5)
    #
    # # work_report_btn = browser.find_element(By.CLASS_NAME, "workreport-audit")
    # # work_report_btn.click()
    #
    # print(browser.get_cookies())
    # cookie = browser.get_cookies()[0].get("value")
    # headers["Cookie"] = "_redmine_session=" + cookie
    # response = requests.get(url, headers=headers)
    # soup = BeautifulSoup(response.content, 'html.parser')
    response = """<html><div class="data-table" style="margin-top: 10px ;">
         <table id="workreport-table" style="margin-top: 1px;width: 100%;">
          <thead>
           <tr>
            <th align="center" width="8%">
             时间
            </th>
            <th align="center" width="6%">
             分类一名称
            </th>
            <th align="center" width="9%">
             分类二名称
            </th>
            <th align="center" width="9%">
             分类三名称
            </th>
            <th align="center" width="8%">
             分类四名称
            </th>
            <th align="center" width="8%">
             活动名称
            </th>
            <th align="center" width="5%">
             工作时间
            </th>
            <th align="center" width="6%">
             工作时间合计
            </th>
            <th align="center" width="6%">
             在岗时间X.XX小时
            </th>
            <th align="center" width="17%">
             工作内容
            </th>
            <th align="center" width="6%">
             注释
            </th>
            <th align="center" width="6%">
             异常原因
            </th>
            <th align="center" width="6%">
             审核标识
            </th>
           </tr>
          </thead>
          <tbody>
           <tr>
            <td align="center" rowspan="1">
             2023-08-01
            </td>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             11.4
            </td>
            <td align="center" rowspan="1">
             11.4
            </td>
            <td align="center" rowspan="1">
             <input disabled="true" id="2023-08-01" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-01">
               11.41
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-01')" style="background: navajowhite" type="button" value="报销操作"/>
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/13252" target="_blank">
              【Audio】外部问题调研&amp;确认
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             通过审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="2">
             2023-08-02
            </td>
            <td align="center">
             请假
            </td>
            <td align="center">
             串休假
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             1.0
            </td>
            <td align="center" rowspan="2">
             8.1
            </td>
            <td align="center" rowspan="2">
             <input disabled="true" id="2023-08-02" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-02">
               8.1
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-02')" type="button" value="报销操作"/>
            </td>
            <td align="center">
             加班串休
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             通过审核
            </td>
           </tr>
           <tr>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             8.1
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/29818" target="_blank">
              【3B4A】【二部】【QQ音乐】勾选我已阅读并知晓该风险，迁移到其他应用再迁移回QQ音乐，我已阅读并知晓该风险先显示为勾选状态，再显示为取消勾选状态
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             通过审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="1">
             2023-08-03
            </td>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             8.0
            </td>
            <td align="center" rowspan="1">
             8.0
            </td>
            <td align="center" rowspan="1">
             <input disabled="true" id="2023-08-03" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-03">
               8.03
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-03')" type="button" value="报销操作"/>
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/29818" target="_blank">
              【3B4A】【二部】【QQ音乐】勾选我已阅读并知晓该风险，迁移到其他应用再迁移回QQ音乐，我已阅读并知晓该风险先显示为勾选状态，再显示为取消勾选状态
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             通过审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="1">
             2023-08-04
            </td>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             9.18
            </td>
            <td align="center" rowspan="1">
             9.18
            </td>
            <td align="center" rowspan="1">
             <input disabled="true" id="2023-08-04" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-04">
               9.18
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-04')" type="button" value="报销操作"/>
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/12682" target="_blank">
              【T31A】【二部】【QQ音乐】未登录情况下 进入QQ音乐，没有直接显示二维码登录页面
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             通过审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="1">
             2023-08-07
            </td>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             8.0
            </td>
            <td align="center" rowspan="1">
             8.0
            </td>
            <td align="center" rowspan="1">
             <input disabled="true" id="2023-08-07" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-07">
               8.03
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-07')" type="button" value="报销操作"/>
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/12682" target="_blank">
              【T31A】【二部】【QQ音乐】未登录情况下 进入QQ音乐，没有直接显示二维码登录页面
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             通过审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="1">
             2023-08-08
            </td>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             8.15
            </td>
            <td align="center" rowspan="1">
             8.15
            </td>
            <td align="center" rowspan="1">
             <input disabled="true" id="2023-08-08" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-08">
               8.15
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-08')" type="button" value="报销操作"/>
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/12682" target="_blank">
              【T31A】【二部】【QQ音乐】未登录情况下 进入QQ音乐，没有直接显示二维码登录页面
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             通过审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="1">
             2023-08-09
            </td>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             11.0
            </td>
            <td align="center" rowspan="1">
             11.0
            </td>
            <td align="center" rowspan="1">
             <input disabled="true" id="2023-08-09" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-09">
               11.05
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-09')" style="background: navajowhite" type="button" value="报销操作"/>
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/13252" target="_blank">
              【Audio】外部问题调研&amp;确认
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             未审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="1">
             2023-08-10
            </td>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             8.3
            </td>
            <td align="center" rowspan="1">
             8.3
            </td>
            <td align="center" rowspan="1">
             <input disabled="true" id="2023-08-10" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-10">
               8.33
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-10')" type="button" value="报销操作"/>
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/13252" target="_blank">
              【Audio】外部问题调研&amp;确认
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             未审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="3">
             2023-08-11
            </td>
            <td align="center">
             请假
            </td>
            <td align="center">
             事假
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             1.0
            </td>
            <td align="center" rowspan="3">
             7.5
            </td>
            <td align="center" rowspan="3">
             <input disabled="true" id="2023-08-11" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-11">
               4.55
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-11')" type="button" value="报销操作"/>
            </td>
            <td align="center">
             迟到请假
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             通过审核
            </td>
           </tr>
           <tr>
            <td align="center">
             OT共通项目
            </td>
            <td align="center">
             OT050001.技术中心
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             3.0
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/7516" target="_blank">
              公司活动（党建活动/技术日活动/总裁办活动）
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             通过审核
            </td>
           </tr>
           <tr>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             4.5
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/13252" target="_blank">
              【Audio】外部问题调研&amp;确认
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             未审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="1">
             2023-08-14
            </td>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             12.0
            </td>
            <td align="center" rowspan="1">
             12.0
            </td>
            <td align="center" rowspan="1">
             <input disabled="true" id="2023-08-14" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-14">
               12.06
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-14')" style="background: navajowhite" type="button" value="报销操作"/>
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/13252" target="_blank">
              【Audio】外部问题调研&amp;确认
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             未审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="2">
             2023-08-15
            </td>
            <td align="center">
             请假
            </td>
            <td align="center">
             串休假
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             1.0
            </td>
            <td align="center" rowspan="2">
             8.2
            </td>
            <td align="center" rowspan="2">
             <input disabled="true" id="2023-08-15" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-15">
               8.25
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-15')" type="button" value="报销操作"/>
            </td>
            <td align="center">
             加班串休
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             通过审核
            </td>
           </tr>
           <tr>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             8.2
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/13252" target="_blank">
              【Audio】外部问题调研&amp;确认
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             未审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="1">
             2023-08-16
            </td>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             8.3
            </td>
            <td align="center" rowspan="1">
             8.3
            </td>
            <td align="center" rowspan="1">
             <input disabled="true" id="2023-08-16" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-16">
               8.36
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-16')" type="button" value="报销操作"/>
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/13252" target="_blank">
              【Audio】外部问题调研&amp;确认
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             未审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="2">
             2023-08-17
            </td>
            <td align="center">
             请假
            </td>
            <td align="center">
             事假
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             1.0
            </td>
            <td align="center" rowspan="2">
             7.6
            </td>
            <td align="center" rowspan="2">
             <input disabled="true" id="2023-08-17" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-17">
               7.66
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-17')" type="button" value="报销操作"/>
            </td>
            <td align="center">
             迟到
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             通过审核
            </td>
           </tr>
           <tr>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             7.6
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/13252" target="_blank">
              【Audio】外部问题调研&amp;确认
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             未审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="1">
             2023-08-18
            </td>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             8.0
            </td>
            <td align="center" rowspan="1">
             8.0
            </td>
            <td align="center" rowspan="1">
             <input disabled="true" id="2023-08-18" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-18">
               8.05
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-18')" type="button" value="报销操作"/>
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/13252" target="_blank">
              【Audio】外部问题调研&amp;确认
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             未审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="1">
             2023-08-19
            </td>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             2.0
            </td>
            <td align="center" rowspan="1">
             2.0
            </td>
            <td align="center" rowspan="1">
             <input disabled="true" id="2023-08-19" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-19">
               2.01
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-19')" type="button" value="报销操作"/>
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/13252" target="_blank">
              【Audio】外部问题调研&amp;确认
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             未审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="1">
             2023-08-21
            </td>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             9.1
            </td>
            <td align="center" rowspan="1">
             9.1
            </td>
            <td align="center" rowspan="1">
             <input disabled="true" id="2023-08-21" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-21">
               9.13
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-21')" type="button" value="报销操作"/>
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/13252" target="_blank">
              【Audio】外部问题调研&amp;确认
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             未审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="2">
             2023-08-22
            </td>
            <td align="center">
             请假
            </td>
            <td align="center">
             事假
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             1.0
            </td>
            <td align="center" rowspan="2">
             9.16
            </td>
            <td align="center" rowspan="2">
             <input disabled="true" id="2023-08-22" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-22">
               9.16
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-22')" type="button" value="报销操作"/>
            </td>
            <td align="center">
             迟到了
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             通过审核
            </td>
           </tr>
           <tr>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             9.16
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/13252" target="_blank">
              【Audio】外部问题调研&amp;确认
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             未审核
            </td>
           </tr>
           <tr>
            <td align="center" rowspan="1">
             2023-08-23
            </td>
            <td align="center">
             100.本田技研（中国）
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目
            </td>
            <td align="center">
             CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)
            </td>
            <td align="center">
            </td>
            <td align="center">
             redmine登录日报
            </td>
            <td align="center">
             8.0
            </td>
            <td align="center" rowspan="1">
             8.0
            </td>
            <td align="center" rowspan="1">
             <input disabled="true" id="2023-08-23" size="10" style="color: red;text-align: center" type="text" value=""/>
             <br/>
             <b>
              <a href="/selectcardinfo?code=M000761&amp;event_time=2023-08-23">
               8.05
              </a>
             </b>
             <br/>
             <br/>
             <input onclick="addReimbursement('2023-08-23')" type="button" value="报销操作"/>
            </td>
            <td align="center">
             <a href="http://redmine-pa.mxnavi.com/issues/13252" target="_blank">
              【Audio】外部问题调研&amp;确认
             </a>
            </td>
            <td align="center">
            </td>
            <td align="center">
            </td>
            <td align="center">
             未审核
            </td>
           </tr>
          </tbody>
         </table>
        </div></html>"""

    soup = BeautifulSoup(response, 'html.parser')
    tables = soup.find_all('tr')

    table_dic = {}
    table_headers = []
    table_values = []
    # 遍历每个table标签
    for table in tables:
        # 查找当前table下的所有子元素
        table_header = []
        table_value = []
        children = table.find_all("th", recursive=False)
        for child in children:
            text = child.getText().replace("\n", "").replace(" ", "")
            if child.getText() == "":
                continue
            table_header.append(text)
        # print(table_header)
        td_children = table.find_all("td", recursive=False)
        for td_child in td_children:
            td_text = td_child.getText().replace("\n", "").replace(" ", "")
            table_value.append(td_text)
        # print(table_value)
        if table_header:
            table_headers.append(table_header)
        if table_value:
            table_values.append(table_value)
    table_dic["header"] = table_headers[0]
    table_dic["values"] = table_values
    print(table_dic)


# browser = webdriver.Chrome()
auto_login()
# browser.quit()

# test_url()