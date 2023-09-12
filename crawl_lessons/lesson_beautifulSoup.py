# 创建BeautifulSoup对象
import requests
from bs4 import BeautifulSoup

from web_crawl.utils import url_manager

string = """
b'<!DOCTYPE html>\n<html lang="zh">\n<head>\n<meta charset="utf-8" />\n<meta http-equiv="X-UA-Compatible" content="IE=edge"/>\n<title>\xe7\xbe\x8e\xe8\xa1\x8c\xe9\xa1\xb9\xe7\x9b\xae\xe7\xae\xa1\xe7\x90\x86\xe5\xb9\xb3\xe5\x8f\xb0</title>\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<meta name="description" content="Redmine" />\n<meta name="keywords" content="issue,bug,tracker" />\n<meta name="csrf-param" content="authenticity_token" />\n<meta name="csrf-token" content="C3FImHjT/Xc/MBCI98wcCKFdsIpxNsikKVn2dQX9koS94e0toxhyfk9sT9GHMpygo7tuq2Pa1/Ybwov+OmZqzg==" />\n<link rel=\'shortcut icon\' href=\'/favicon.ico?1653026646\' />\n<link rel="stylesheet" media="all" href="/stylesheets/jquery/jquery-ui-1.12.1.css?1653026646" />\n<link rel="stylesheet" media="all" href="/stylesheets/tribute-5.1.3.css?1653026646" />\n<link rel="stylesheet" media="all" href="/themes/circle/stylesheets/application.css?1653026646" />\n<link rel="stylesheet" media="all" href="/stylesheets/responsive.css?1653026646" />\n\n<script src="/javascripts/jquery-3.5.1-ui-1.12.1-ujs-5.2.4.5.js?1653026646"></script>\n<script src="/javascripts/jquery-migrate-3.3.2.min.js?1653026646"></script>\n<script src="/javascripts/tribute-5.1.3.min.js?1653026646"></script>\n<script src="/javascripts/tablesort-5.2.1.min.js?1653026646"></script>\n<script src="/javascripts/tablesort-5.2.1.number.min.js?1653026646"></script>\n<script src="/javascripts/application.js?1653026646"></script>\n<script src="/javascripts/responsive.js?1653026646"></script>\n<script>\n//<![CDATA[\n$(window).on(\'load\', function(){ warnLeavingUnsaved(\'\xe8\x8b\xa5\xe7\xa6\xbb\xe5\xbc\x80\xe5\xbd\x93\xe5\x89\x8d\xe9\xa1\xb5\xe9\x9d\xa2\xef\xbc\x8c\xe5\x88\x99\xe8\xaf\xa5\xe9\xa1\xb5\xe9\x9d\xa2\xe5\x86\x85\xe6\x9c\xaa\xe4\xbf\x9d\xe5\xad\x98\xe7\x9a\x84\xe5\x86\x85\xe5\xae\xb9\xe5\xb0\x86\xe4\xb8\xa2\xe5\xa4\xb1\xe3\x80\x82\'); });\n//]]>\n</script>\n<script src="/themes/circle/javascripts/theme.js?1653026646"></script>\n<script>\n//<![CDATA[\nrm = window.rm || {};rm.AutoComplete = rm.AutoComplete || {};rm.AutoComplete.dataSources = \'{"issues":"/issues/auto_complete?q=","wiki_pages":"/wiki_pages/auto_complete?q="}\';\n//]]>\n</script>\n<link rel="stylesheet" media="screen" href="/plugin_assets/redmine_agile/stylesheets/redmine_agile.css?1694399425" /> <link rel="stylesheet" media="screen" href="/plugin_assets/redmine_audit_series/stylesheets/audit_series.css?1694399425" /> <link rel="stylesheet" media="screen" href="/plugin_assets/redmine_banner/stylesheets/banner.css?1694399425" /><script src="/plugin_assets/redmine_banner/javascripts/banner.js?1694399425"></script>  <link rel="stylesheet" media="screen" href="/plugin_assets/redmine_issue_templates/stylesheets/issue_templates.css?1694399425" />  <link rel="stylesheet" media="screen" href="/plugin_assets/redmine_people/stylesheets/redmine_people.css?1694399425" /> <link rel="stylesheet" media="screen" href="/plugin_assets/redmine_crm/stylesheets/money.css?1694399424" /> <link rel="stylesheet" media="screen" href="/plugin_assets/redmine_searchable_selectbox/stylesheets/select2.min.css?1694399425" /><link rel="stylesheet" media="screen" href="/plugin_assets/redmine_searchable_selectbox/stylesheets/searchable_selectbox.css?1694399425" /><script src="/plugin_assets/redmine_searchable_selectbox/javascripts/select2.full.min.js?1694399425"></script><script src="/plugin_assets/redmine_searchable_selectbox/javascripts/searchable_selectbox.js?1694399425"></script> \n<!-- page specific tags -->\n  <link rel="stylesheet" media="screen" href="/plugin_assets/redmineup_tags/stylesheets/redmine_tags.css?1694399425" />\n  <script src="/plugin_assets/redmineup_tags/javascripts/redmine_tags.js?1694399425"></script>\n  <script src="/plugin_assets/redmine_crm/javascripts/select2.js?1694399424"></script><link rel="stylesheet" media="screen" href="/plugin_assets/redmine_crm/stylesheets/select2.css?1694399424" /><script src="/plugin_assets/redmine_crm/javascripts/select2_helpers.js?1694399424"></script>\n</head>\n<body class="theme-Circle has-main-menu controller-account action-login avatars-off">\n\n<div id="wrapper">\n\n<div class="flyout-menu js-flyout-menu">\n\n\n\n        <h3>\xe9\xa1\xb9\xe7\x9b\xae</h3>\n        <span class="js-project-menu"></span>\n\n    <h3>\xe4\xb8\x80\xe8\x88\xac</h3>\n    <span class="js-general-menu"></span>\n\n    <span class="js-sidebar flyout-menu__sidebar"></span>\n\n    <h3>\xe7\xae\x80\xe4\xbb\x8b</h3>\n    <span class="js-profile-menu"></span>\n\n</div>\n\n<div id="wrapper2">\n<div id="wrapper3">\n<div id="top-menu">\n    <div id="account">\n        <ul><li><a class="login" href="/login">\xe7\x99\xbb\xe5\xbd\x95</a></li></ul>    </div>\n    \n    </div>\n\n<div id="header">\n\n    <a href="#" class="mobile-toggle-button js-flyout-menu-toggle-button"></a>\n\n\n    <h1>\xe7\xbe\x8e\xe8\xa1\x8c\xe9\xa1\xb9\xe7\x9b\xae\xe7\xae\xa1\xe7\x90\x86\xe5\xb9\xb3\xe5\x8f\xb0</h1>\n\n    <div id="main-menu" class="tabs">\n        \n        <div class="tabs-buttons" style="display:none;">\n            <button class="tab-left" onclick="moveTabLeft(this); return false;"></button>\n            <button class="tab-right" onclick="moveTabRight(this); return false;"></button>\n        </div>\n    </div>\n</div>\n\n<div id="main" class="nosidebar">\n    <div id="sidebar">text</div>\n\n    <div id="content">\n        \n        \n\n<div id="login-form">\n  <form onsubmit="return keepAnchorOnSignIn(this);" action="/login" accept-charset="UTF-8" name="form-4efcbfe7" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="ujS+xULMmFoKR2kQjman+AIkqlUbKxjG8Co7w865SJQMpBtwmQcXU3obNkn+mCdQAMJ0dAnHB5TCsUZI8SKw3g==" />\n  <input type="hidden" name="back_url" value="/selectcardinfo?utf8=%E2%9C%93&amp;code=M000761&amp;event_time%5B%5D=2023-09-01&amp;commit=%E6%9F%A5%E8%AF%A2" />\n  \n  <label for="username">\xe7\x99\xbb\xe5\xbd\x95\xe5\x90\x8d</label>\n  <input type="text" name="username" id="username" tabindex="1" />\n  \n  <label for="password">\n    \xe5\xaf\x86\xe7\xa0\x81\n    <a class="lost_password" href="/account/lost_password">\xe5\xbf\x98\xe8\xae\xb0\xe5\xaf\x86\xe7\xa0\x81</a>\n  </label>\n  <input type="password" name="password" id="password" tabindex="2" />\n  \n  \n  \n  <input type="submit" name="login" value="\xe7\x99\xbb\xe5\xbd\x95" tabindex="5" id="login-submit" />\n</form></div>\n\n\n\n<script>\n//<![CDATA[\n$(\'#username\').focus();\n//]]>\n</script>\n\n        \n        <div style="clear:both;"></div>\n    </div>\n</div>\n<div id="footer">\n    Powered by <a href="https://www.redmine.org/">Redmine</a> &copy; 2006-2021 Jean-Philippe Lang\n</div>\n</div>\n\n<div id="ajax-indicator" style="display:none;"><span>\xe8\xbd\xbd\xe5\x85\xa5\xe4\xb8\xad...</span></div>\n<div id="ajax-modal" style="display:none;"></div>\n\n</div>\n</div>\n \n<script>\n//<![CDATA[\nsetSelect2Filter(\'people\', {"format_state":"formatStateWithAvatar","min_input_length":1,"url":"/people/new/autocomplete_for_manager"});\n//]]>\n</script>\n\n  <script>\n//<![CDATA[\nsetSelect2Filter(\'issue_tags\', {"url":"http://redmine-pa.mxnavi.com/auto_completes/redmine_tags"});\n//]]>\n</script>\n\n</body>\n</html>\n'
"""


soup = BeautifulSoup(
    string,  # 文档字符串
    'html.parser',  # html解析器
    # from_encoding="utf-8"  # html编码，相同则可省略
)

# 搜索节点  find_all find

"""
find_all(name, attrs, string)

"""

print(soup.find_all('meta', content="IE=edge"))

# string需要完全匹配
print(soup.find_all("div", id="footer"))
link = soup.find_all("a")
for item in link:
    print(item['href'], item.get_text())
print(soup.find_all("a", href="https://www.redmine.org/"))

import re

pattern = r'^http://www.crazyant.net/\d+.html$'

print(re.match(pattern, "http://www.baidu.com"))


root_url = "http://www.crazyant.net"

urls = url_manager.UrlManager()
urls.add_new_url(root_url)

fout = open("crawl_all_pages.txt", "w", encoding="utf-8")
while urls.has_new_url():
    curr_url = urls.get_url()
    r = requests.get(curr_url, timeout=3)
    if r.status_code != 200:
        print("error")
        continue
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.title.string

    fout.write("%s\t%s\n" % (curr_url, title))
    print("success: %s, %s, %d "% (curr_url, title, len(urls.new_urls)))

    links = soup.find_all("a")
    for link in links:
        # href = link['href']  # 如果href为空会抛出异常
        href = link.get('href')
        if href is None:
            continue
        pattern = r'^http://www.crazyant.net/\d+.html$'
        if re.match(pattern, href):
            urls.add_new_url(href)

fout.close()