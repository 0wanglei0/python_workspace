# -*- coding: utf-8 -*-
import sys
import datetime
import time
import traceback

from bs4 import BeautifulSoup
from lxml import etree

from selenium.webdriver.common.by import By
import requests

import module_weekdays as weekdays
import prettytable as ptb

from log_print import Log
import argparse
import module_browser as m_browser
import module_write_file as m_write
import utils

""" ..\python_workspace\Scripts\pyinstaller.exe -F .\work_report.py --add-binary "chromedriver.exe;." --add-binary "chromedriver_116.exe;." --add-binary "chromedriver_115.exe;." """

"""
获取指定日期的工时
http://redmine-pa.mxnavi.com/issues/13252/time_entries/autocomplete_for_time?q=2023-12-03
"""


def find_work_time(response_with_code, workday):
    # print(response_with_code.content)
    # content = b'<!DOCTYPE html>\n<html lang="zh">\n<head>\n<meta charset="utf-8" />\n<meta http-equiv="X-UA-Compatible" content="IE=edge"/>\n<title>\xe7\xbe\x8e\xe8\xa1\x8c\xe9\xa1\xb9\xe7\x9b\xae\xe7\xae\xa1\xe7\x90\x86\xe5\xb9\xb3\xe5\x8f\xb0</title>\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<meta name="description" content="Redmine" />\n<meta name="keywords" content="issue,bug,tracker" />\n<meta name="csrf-param" content="authenticity_token" />\n<meta name="csrf-token" content="yKjqmUY3UqpFtppYBpTbBfiKCm3GjVz8Un2S7FSKkjrOAAlSzBWNw3eN/8fy2rg3H71Ffd1N7vLX08IABrQVKA==" />\n<link rel=\'shortcut icon\' href=\'/favicon.ico?1653026646\' />\n<link rel="stylesheet" media="all" href="/stylesheets/jquery/jquery-ui-1.12.1.css?1653026646" />\n<link rel="stylesheet" media="all" href="/stylesheets/tribute-5.1.3.css?1653026646" />\n<link rel="stylesheet" media="all" href="/themes/circle/stylesheets/application.css?1653026646" />\n<link rel="stylesheet" media="all" href="/stylesheets/responsive.css?1653026646" />\n\n<script src="/javascripts/jquery-3.5.1-ui-1.12.1-ujs-5.2.4.5.js?1653026646"></script>\n<script src="/javascripts/jquery-migrate-3.3.2.min.js?1653026646"></script>\n<script src="/javascripts/tribute-5.1.3.min.js?1653026646"></script>\n<script src="/javascripts/tablesort-5.2.1.min.js?1653026646"></script>\n<script src="/javascripts/tablesort-5.2.1.number.min.js?1653026646"></script>\n<script src="/javascripts/application.js?1653026646"></script>\n<script src="/javascripts/responsive.js?1653026646"></script>\n<script>\n//<![CDATA[\n$(window).on(\'load\', function(){ warnLeavingUnsaved(\'\xe8\x8b\xa5\xe7\xa6\xbb\xe5\xbc\x80\xe5\xbd\x93\xe5\x89\x8d\xe9\xa1\xb5\xe9\x9d\xa2\xef\xbc\x8c\xe5\x88\x99\xe8\xaf\xa5\xe9\xa1\xb5\xe9\x9d\xa2\xe5\x86\x85\xe6\x9c\xaa\xe4\xbf\x9d\xe5\xad\x98\xe7\x9a\x84\xe5\x86\x85\xe5\xae\xb9\xe5\xb0\x86\xe4\xb8\xa2\xe5\xa4\xb1\xe3\x80\x82\'); });\n//]]>\n</script>\n<script src="/themes/circle/javascripts/theme.js?1653026646"></script>\n<script>\n//<![CDATA[\nrm = window.rm || {};rm.AutoComplete = rm.AutoComplete || {};rm.AutoComplete.dataSources = \'{"issues":"/issues/auto_complete?q=","wiki_pages":"/wiki_pages/auto_complete?q="}\';\n//]]>\n</script>\n<link rel="stylesheet" media="screen" href="/plugin_assets/redmine_agile/stylesheets/redmine_agile.css?1701779526" /> <link rel="stylesheet" media="screen" href="/plugin_assets/redmine_audit_series/stylesheets/audit_series.css?1701779526" /> <link rel="stylesheet" media="screen" href="/plugin_assets/redmine_banner/stylesheets/banner.css?1701779526" /><script src="/plugin_assets/redmine_banner/javascripts/banner.js?1701779526"></script> <script src="/plugin_assets/redmine_checklists/javascripts/checklists.js?1701779526"></script><link rel="stylesheet" media="screen" href="/plugin_assets/redmine_checklists/stylesheets/checklists.css?1701779526" /> <link rel="stylesheet" media="screen" href="/plugin_assets/redmine_issue_badge/stylesheets/style.css?1701779526" /> <link rel="stylesheet" media="screen" href="/plugin_assets/redmine_issue_templates/stylesheets/issue_templates.css?1701779526" />  <link rel="stylesheet" media="screen" href="/plugin_assets/redmine_people/stylesheets/redmine_people.css?1701779526" /> <link rel="stylesheet" media="screen" href="/plugin_assets/redmine_crm/stylesheets/money.css?1701779524" /> <link rel="stylesheet" media="screen" href="/plugin_assets/redmine_searchable_selectbox/stylesheets/select2.min.css?1701779526" /><link rel="stylesheet" media="screen" href="/plugin_assets/redmine_searchable_selectbox/stylesheets/searchable_selectbox.css?1701779526" /><script src="/plugin_assets/redmine_searchable_selectbox/javascripts/select2.full.min.js?1701779526"></script><script src="/plugin_assets/redmine_searchable_selectbox/javascripts/searchable_selectbox.js?1701779526"></script> \n<!-- page specific tags -->\n\n<style type="text/css">\n  .from-table\n  {\n    overflow-y: visible;\n  }\n  .from-table,.data-table\n  {\n    clear:left;\n  }\n\n  .from-table table td,.data-table table td\n  {\n    background: #F8FCF8;\n    border:1px #c0c0c0 solid;\n    text-align: center;\n    padding:5px 3px;\n    word-break: break-all;\n\n  }\n\n  .from-table table th,.data-table table th{\n    font-size: 11px;\n  }\n\n  .from-table table th,.data-table table th\n  {\n    background: #cbd9d9;\n    border:1px #c0c0c0 solid;\n    text-align: center;\n    padding:5px 3px;\n    word-break: break-all;\n  }\n  .from-table table,.data-table table\n  {\n    border-collapse: collapse;\n    border:1px solid #c0c0c0\n  }\n  .test{\n    color: red;\n  }\n\n</style>\n<script>\n//<![CDATA[\nvar datepickerOptions={dateFormat: \'yy-mm-dd\', firstDay: 0, showOn: \'button\', buttonImageOnly: true, buttonImage: \'/images/calendar.png?1653026646\', showButtonPanel: true, showWeek: true, showOtherMonths: true, selectOtherMonths: true, changeMonth: true, changeYear: true, beforeShow: beforeShowDatePicker};\n//]]>\n</script><script src="/javascripts/i18n/datepicker-zh-CN.js?1653026646"></script>  <link rel="stylesheet" media="screen" href="/plugin_assets/redmineup_tags/stylesheets/redmine_tags.css?1701779526" />\n  <script src="/plugin_assets/redmineup_tags/javascripts/redmine_tags.js?1701779526"></script>\n  <script src="/plugin_assets/redmine_crm/javascripts/select2.js?1701779524"></script><link rel="stylesheet" media="screen" href="/plugin_assets/redmine_crm/stylesheets/select2.css?1701779524" /><script src="/plugin_assets/redmine_crm/javascripts/select2_helpers.js?1701779524"></script>\n</head>\n<body class="theme-Circle has-main-menu controller-cardinfos action-selectcardinfo avatars-off">\n\n<div id="wrapper">\n\n<div class="flyout-menu js-flyout-menu">\n\n        <div class="flyout-menu__search">\n            <form action="/search" accept-charset="UTF-8" name="form-e60284c4" method="get"><input name="utf8" type="hidden" value="&#x2713;" />\n            \n            <label class="search-magnifier search-magnifier--flyout" for="flyout-search">&#9906;</label>\n            <input type="text" name="q" id="flyout-search" class="small js-search-input" placeholder="\xe6\x90\x9c\xe7\xb4\xa2" />\n</form>        </div>\n\n        <div class="flyout-menu__avatar flyout-menu__avatar--no-avatar">\n            <a href="/people/1541">wangleic</a>\n        </div>\n\n        <h3>\xe9\xa1\xb9\xe7\x9b\xae</h3>\n        <span class="js-project-menu"></span>\n\n    <h3>\xe4\xb8\x80\xe8\x88\xac</h3>\n    <span class="js-general-menu"></span>\n\n    <span class="js-sidebar flyout-menu__sidebar"></span>\n\n    <h3>\xe7\xae\x80\xe4\xbb\x8b</h3>\n    <span class="js-profile-menu"></span>\n\n</div>\n\n<div id="wrapper2">\n<div id="wrapper3">\n<div id="top-menu">\n    <div id="account">\n        <ul><li><a class="my-account" href="/my/account">\xe6\x88\x91\xe7\x9a\x84\xe5\xb8\x90\xe5\x8f\xb7</a></li><li><a class="logout" rel="nofollow" data-method="post" href="/logout">\xe9\x80\x80\xe5\x87\xba</a></li></ul>    </div>\n    <div id="loggedas">\xe7\x99\xbb\xe5\xbd\x95\xe4\xb8\xba <a href="/people/1541">wangleic</a></div>\n    <ul><li><a class="home" href="/">\xe4\xb8\xbb\xe9\xa1\xb5</a></li><li><a class="my-page" href="/my/page">\xe6\x88\x91\xe7\x9a\x84\xe5\xb7\xa5\xe4\xbd\x9c\xe5\x8f\xb0</a></li><li><a class="projects" href="/projects">\xe9\xa1\xb9\xe7\x9b\xae</a></li><li><a class="help" href="https://www.redmine.org/guide">\xe5\xb8\xae\xe5\x8a\xa9</a></li></ul></div>\n\n<div id="header">\n\n    <a href="#" class="mobile-toggle-button js-flyout-menu-toggle-button"></a>\n\n    <div id="quick-search">\n        <form action="/search" accept-charset="UTF-8" name="form-e6943a68" method="get"><input name="utf8" type="hidden" value="&#x2713;" />\n        <input type="hidden" name="scope" />\n        \n        <label for=\'q\'>\n          <a accesskey="4" href="/search">\xe6\x90\x9c\xe7\xb4\xa2</a>:\n        </label>\n        <input type="text" name="q" id="q" size="20" class="small" accesskey="f" data-auto-complete="true" />\n</form>        <div id="project-jump" class="drdn"><span class="drdn-trigger">\xe9\x80\x89\xe6\x8b\xa9\xe4\xb8\x80\xe4\xb8\xaa\xe9\xa1\xb9\xe7\x9b\xae...</span><div class="drdn-content"><div class="quick-search"><input type="text" name="q" id="projects-quick-search" value="" class="autocomplete" data-automcomplete-url="/projects/autocomplete.js?jump=cardinfos" autocomplete="off" /></div><div class="drdn-items projects selection"><strong>\xe6\x9c\x80\xe8\xbf\x91\xe4\xbd\xbf\xe7\x94\xa8</strong><a title="CP100004.Honda_\xe6\xb5\xb7\xe7\xba\xb3\xe6\x96\xb0\xe6\x80\x9d_TSU3.0\xe7\xbb\xb4\xe6\x8a\xa4\xe9\xa1\xb9\xe7\x9b\xae+04.\xe9\x87\x8f\xe4\xba\xa7\xe5\x90\x8e\xe7\xbb\xb4\xe6\x8a\xa4(TSU)" href="/projects/cp100004-honda-tsu3-0-04-tsu?jump=cardinfos"><span style="padding-left:0px;">CP100004.Honda_\xe6\xb5\xb7\xe7\xba\xb3\xe6\x96\xb0\xe6\x80\x9d_TSU3.0\xe7\xbb\xb4\xe6\x8a\xa4\xe9\xa1\xb9\xe7\x9b\xae+04.\xe9\x87\x8f\xe4\xba\xa7\xe5\x90\x8e\xe7\xbb\xb4\xe6\x8a\xa4(TSU)</span></a><a title="CP100001.Honda_HMCT_CONNECT4.5_EV\xe5\x8a\x9f\xe8\x83\xbd\xe8\xbf\x9b\xe5\x8c\x96Demo+04.HondaAPP\xe5\x8a\x9f\xe8\x83\xbd\xe5\xbc\x80\xe5\x8f\x91" href="/projects/cp100001-honda-04-hondaapp?jump=cardinfos"><span style="padding-left:0px;">CP100001.Honda_HMCT_CONNECT4.5_EV\xe5\x8a\x9f\xe8\x83\xbd\xe8\xbf\x9b\xe5\x8c\x96Demo+04.HondaAPP\xe5\x8a\x9f\xe8\x83\xbd\xe5\xbc\x80\xe5\x8f\x91</span></a><a title="CP100003.Honda_\xe4\xb8\x89\xe8\x8f\xb1\xe7\x94\xb5\xe6\x9c\xba_TSU3.0-OTA-TSU_\xe5\x8a\x9f\xe8\x83\xbd\xe8\xbf\x9b\xe5\x8c\x96_2023+(CR)01.OTA(202306)" href="/projects/cp100003-honda-ota-tsu-2023-cr-01-ota-202306?jump=cardinfos"><span style="padding-left:0px;">CP100003.Honda_\xe4\xb8\x89\xe8\x8f\xb1\xe7\x94\xb5\xe6\x9c\xba_TSU3.0-OTA-TSU_\xe5\x8a\x9f\xe8\x83\xbd\xe8\xbf\x9b\xe5\x8c\x96_2023+(CR)01.OTA(202306)</span></a><strong>\xe6\x89\x80\xe6\x9c\x89\xe7\x9a\x84\xe9\xa1\xb9\xe7\x9b\xae</strong><a title="CP100003.Honda_\xe4\xb8\x89\xe8\x8f\xb1\xe7\x94\xb5\xe6\x9c\xba_TSU3.0-OTA-TSU_\xe5\x8a\x9f\xe8\x83\xbd\xe8\xbf\x9b\xe5\x8c\x96_2023+(CR)01.OTA(202306)" href="/projects/cp100003-honda-ota-tsu-2023-cr-01-ota-202306?jump=cardinfos"><span style="padding-left:0px;">CP100003.Honda_\xe4\xb8\x89\xe8\x8f\xb1\xe7\x94\xb5\xe6\x9c\xba_TSU3.0-OTA-TSU_\xe5\x8a\x9f\xe8\x83\xbd\xe8\xbf\x9b\xe5\x8c\x96_2023+(CR)01.OTA(202306)</span></a><a title="CP100003.Honda_\xe4\xb8\x89\xe8\x8f\xb1\xe7\x94\xb5\xe6\x9c\xba_TSU3.0-OTA-TSU_\xe5\x8a\x9f\xe8\x83\xbd\xe8\xbf\x9b\xe5\x8c\x96_2023+(CR)02.OTA(202312)" href="/projects/cp100003-honda-2023-cr-02-ota-202312?jump=cardinfos"><span style="padding-left:0px;">CP100003.Honda_\xe4\xb8\x89\xe8\x8f\xb1\xe7\x94\xb5\xe6\x9c\xba_TSU3.0-OTA-TSU_\xe5\x8a\x9f\xe8\x83\xbd\xe8\xbf\x9b\xe5\x8c\x96_2023+(CR)02.OTA(202312)</span></a><a title="CP100004.Honda_\xe6\xb5\xb7\xe7\xba\xb3\xe6\x96\xb0\xe6\x80\x9d_TSU3.0\xe7\xbb\xb4\xe6\x8a\xa4\xe9\xa1\xb9\xe7\x9b\xae+04.\xe9\x87\x8f\xe4\xba\xa7\xe5\x90\x8e\xe7\xbb\xb4\xe6\x8a\xa4(TSU)" href="/projects/cp100004-honda-tsu3-0-04-tsu?jump=cardinfos"><span style="padding-left:0px;">CP100004.Honda_\xe6\xb5\xb7\xe7\xba\xb3\xe6\x96\xb0\xe6\x80\x9d_TSU3.0\xe7\xbb\xb4\xe6\x8a\xa4\xe9\xa1\xb9\xe7\x9b\xae+04.\xe9\x87\x8f\xe4\xba\xa7\xe5\x90\x8e\xe7\xbb\xb4\xe6\x8a\xa4(TSU)</span></a><a title="CP100005.Honda_CabinControl4.0_\xe9\x98\xbf\xe5\xb0\x94\xe6\xb4\xbe_\xe9\x87\x8f\xe4\xba\xa7\xe5\x90\x8e\xe7\xbb\xb4\xe6\x8a\xa4" href="/projects/cp100005-honda-cabincontrol4-0?jump=cardinfos"><span style="padding-left:0px;">CP100005.Honda_CabinControl4.0_\xe9\x98\xbf\xe5\xb0\x94\xe6\xb4\xbe_\xe9\x87\x8f\xe4\xba\xa7\xe5\x90\x8e\xe7\xbb\xb4\xe6\x8a\xa4</span></a><a title="CP100006.Honda_CabinControl4.0_\xe6\xb5\xb7\xe7\xba\xb3\xe6\x96\xb0\xe6\x80\x9d_\xe9\x87\x8f\xe4\xba\xa7\xe5\x90\x8e\xe7\xbb\xb4\xe6\x8a\xa4" href="/projects/cp100006-honda_cabincontrol4-0?jump=cardinfos"><span style="padding-left:0px;">CP100006.Honda_CabinControl4.0_\xe6\xb5\xb7\xe7\xba\xb3\xe6\x96\xb0\xe6\x80\x9d_\xe9\x87\x8f\xe4\xba\xa7\xe5\x90\x8e\xe7\xbb\xb4\xe6\x8a\xa4</span></a><a title="OT050001.\xe6\x8a\x80\xe6\x9c\xaf\xe4\xb8\xad\xe5\xbf\x83" href="/projects/ot050001?jump=cardinfos"><span style="padding-left:0px;">OT050001.\xe6\x8a\x80\xe6\x9c\xaf\xe4\xb8\xad\xe5\xbf\x83</span></a><a title="\xe7\xbc\xba\xe9\x99\xb7\xe9\xa2\x84\xe9\x98\xb2\xe5\x88\x86\xe6\x9e\x90\xe7\xb3\xbb\xe7\xbb\x9f" href="/projects/bugyyfx?jump=cardinfos"><span style="padding-left:0px;">\xe7\xbc\xba\xe9\x99\xb7\xe9\xa2\x84\xe9\x98\xb2\xe5\x88\x86\xe6\x9e\x90\xe7\xb3\xbb\xe7\xbb\x9f</span></a></div><div class="drdn-items all-projects selection"><a href="/projects?jump=cardinfos">\xe6\x89\x80\xe6\x9c\x89\xe7\x9a\x84\xe9\xa1\xb9\xe7\x9b\xae</a></div></div></div>\n    </div>\n\n    <h1>\xe7\xbe\x8e\xe8\xa1\x8c\xe9\xa1\xb9\xe7\x9b\xae\xe7\xae\xa1\xe7\x90\x86\xe5\xb9\xb3\xe5\x8f\xb0</h1>\n\n    <div id="main-menu" class="tabs">\n        <ul><li><a class="mx-cardinfo" href="/cardinfos">\xe6\x89\x93\xe5\x8d\xa1\xe8\xae\xb0\xe5\xbd\x95\xe7\x9b\xb8\xe5\x85\xb3</a></li><li><a class="workreport-audit" href="/workreports">\xe6\x97\xa5\xe6\x8a\xa5\xe7\x9b\xb8\xe5\x85\xb3</a></li></ul>\n        <div class="tabs-buttons" style="display:none;">\n            <button class="tab-left" onclick="moveTabLeft(this); return false;"></button>\n            <button class="tab-right" onclick="moveTabRight(this); return false;"></button>\n        </div>\n    </div>\n</div>\n\n<div id="main" class="nosidebar">\n    <div id="sidebar">\n        \n        \n    </div>\n\n    <div id="content">\n        \n        <fieldset>\n  <fieldset>\n  <legend><h3 style="margin-top: 10px;">\xe5\x9c\xa8\xe5\xb2\x97\xe5\xb7\xa5\xe6\x97\xb6\xe7\xbb\x9f\xe8\xae\xa1\xe8\xa7\x84\xe5\x88\x99</h3></legend>\n  <div class="from-table">\n    <pre class="test" style="margin-top: 10px;">  *1.\xe4\xb8\x8a\xe5\x8d\x88\xe4\xbb\x8e8\xef\xbc\x9a30\xe5\xbc\x80\xe5\xa7\x8b\xe8\xae\xa1\xe7\xae\x97\xe5\x9c\xa8\xe5\xb2\x97\xe5\xb7\xa5\xe6\x97\xb6\xef\xbc\x8c\xe4\xb8\xad\xe5\x8d\x88\xe5\x8d\x88\xe4\xbc\x91\xe6\x97\xb6\xe9\x97\xb4\xef\xbc\x8812\xef\xbc\x9a00\xef\xbd\x9e13\xef\xbc\x9a00\xef\xbc\x89\xe4\xb8\x8d\xe4\xbd\x9c\xe4\xb8\xba\xe5\x9c\xa8\xe5\xb2\x97\xe5\xb7\xa5\xe6\x97\xb6\xef\xbc\x8c\xe8\xae\xa1\xe7\xae\x97\xe6\x97\xb6\xe4\xbc\x9a\xe8\x87\xaa\xe5\x8a\xa8\xe6\x89\xa3\xe9\x99\xa4</pre>\n    <pre class="test" style="margin-top: 10px;">  *2.\xe5\x9c\xa8\xe5\xb2\x97\xe6\x9c\x9f\xe9\x97\xb4\xef\xbc\x8c\xe7\xa6\xbb\xe5\xbc\x80\xe5\x85\xac\xe5\x8f\xb8\xe7\x9a\x84\xe5\xb7\xa5\xe6\x97\xb6\xef\xbc\x8c\xe4\xb8\x8d\xe4\xbd\x9c\xe4\xb8\xba\xe5\x9c\xa8\xe5\xb2\x97\xe5\xb7\xa5\xe6\x97\xb6\xef\xbc\x8c\xe8\xae\xa1\xe7\xae\x97\xe6\x97\xb6\xe4\xbc\x9a\xe8\x87\xaa\xe5\x8a\xa8\xe6\x89\xa3\xe9\x99\xa4</pre>\n  </div>\n</fieldset>\n\n<!-- \xe6\x9f\xa5\xe8\xaf\xa2 -->\n<form id="cardinfo_list_form" action="/selectcardinfo" accept-charset="UTF-8" name="cardinfo_list_form-80e094c7" method="get"><input name="utf8" type="hidden" value="&#x2713;" />\n  <fieldset>\n    <legend><h3 style="margin-top: 10px;">\xe6\x89\x93\xe5\x8d\xa1\xe8\xae\xb0\xe5\xbd\x95\xe6\x9f\xa5\xe8\xaf\xa2</h3></legend>\n    <div class="from-table">\n      <table style="margin-top: 1px;width: 100%;">\n        <tr>\n          <td align="center">\n            \xe6\x9f\xa5\xe8\xaf\xa2\xe6\x97\xb6\xe9\x97\xb4 :\n            <input type="hidden" name="code" value="M000761" />\n            <input value="2023-12-01" size="15" type="date" name="event_time[]" id="event_time_" />\n            <script>\n//<![CDATA[\n$(function() { $(\'#event_time\').addClass(\'date\').datepickerFallback(datepickerOptions); });\n//]]>\n</script>\n            <input type="submit" name="commit" value="\xe6\x9f\xa5\xe8\xaf\xa2" data-disable-with="\xe6\x9f\xa5\xe8\xaf\xa2" />\n          </td>\n        </tr>\n      </table>\n    </div>\n  </fieldset>\n</form>\n<fieldset>\n  <legend><h3 style="margin-top: 10px;">\xe6\x89\x93\xe5\x8d\xa1\xe8\xae\xb0\xe5\xbd\x95\xe5\x88\x97\xe8\xa1\xa8\xe8\xaf\xa6\xe7\xbb\x86,\xe6\x80\xbb\xe5\xb7\xa5\xe6\x97\xb6\xef\xbc\x9a  8.41</h3> </legend>\n  <div class="data-table" >\n    <table  id="workreport-table"  style="margin-top: 1px;width: 100%;" >\n      <thead>\n      <tr>\n        <th width="20%" align ="center"> \xe5\x91\x98\xe5\xb7\xa5\xe5\xa7\x93\xe5\x90\x8d</th>\n        <th width="60%" align ="center"> \xe6\x89\x93\xe5\x8d\xa1\xe8\xae\xb0\xe5\xbd\x95</th>\n        <th width="20%" align ="center"> \xe8\xbf\x9b\xe5\x87\xba</th>\n      </tr>\n      </thead>\n      <tbody>\n          <tr>\n            <td align="center"  valign="middle">\n              \xe7\x8e\x8b\xe7\xa3\x8aC\n            </td>\n            <td align="center"  valign="middle">\n              2023-12-01 08:57:27\n            </td>\n             <td align="center"  valign="middle">\n               \xe8\xbf\x9b\xe9\x97\xa8\n            </td>\n          </tr>\n          <tr>\n            <td align="center"  valign="middle">\n              \xe7\x8e\x8b\xe7\xa3\x8aC\n            </td>\n            <td align="center"  valign="middle">\n              2023-12-01 12:21:39\n            </td>\n             <td align="center"  valign="middle">\n               \xe5\x87\xba\xe9\x97\xa8\n            </td>\n          </tr>\n          <tr>\n            <td align="center"  valign="middle">\n              \xe7\x8e\x8b\xe7\xa3\x8aC\n            </td>\n            <td align="center"  valign="middle">\n              2023-12-01 14:15:11\n            </td>\n             <td align="center"  valign="middle">\n               \xe8\xbf\x9b\xe9\x97\xa8\n            </td>\n          </tr>\n          <tr>\n            <td align="center"  valign="middle">\n              \xe7\x8e\x8b\xe7\xa3\x8aC\n            </td>\n            <td align="center"  valign="middle">\n              2023-12-01 15:32:56\n            </td>\n             <td align="center"  valign="middle">\n               \xe5\x87\xba\xe9\x97\xa8\n            </td>\n          </tr>\n          <tr>\n            <td align="center"  valign="middle">\n              \xe7\x8e\x8b\xe7\xa3\x8aC\n            </td>\n            <td align="center"  valign="middle">\n              2023-12-01 15:36:32\n            </td>\n             <td align="center"  valign="middle">\n               \xe8\xbf\x9b\xe9\x97\xa8\n            </td>\n          </tr>\n          <tr>\n            <td align="center"  valign="middle">\n              \xe7\x8e\x8b\xe7\xa3\x8aC\n            </td>\n            <td align="center"  valign="middle">\n              2023-12-01 19:41:27\n            </td>\n             <td align="center"  valign="middle">\n               \xe5\x87\xba\xe9\x97\xa8\n            </td>\n          </tr>\n          <tr>\n            <td colspan="2"  align ="right">\n              \xe5\x9c\xa8\xe5\xb2\x97\xe6\x97\xb6\xe9\x97\xb4\xef\xbc\x9a(H\xe5\xb0\x8f\xe6\x97\xb6\xef\xbc\x9aM\xe5\x88\x86\xe9\x92\x9f)\n            </td>\n            <td  colspan="1" align="left"  valign="middle">\n              8.41\n            </td>\n          </tr>\n      </tbody>\n    </table>\n  </div>\n</fieldset>\n\n</fieldset>\n        \n        <div style="clear:both;"></div>\n    </div>\n</div>\n<div id="footer">\n    Powered by <a href="https://www.redmine.org/">Redmine</a> &copy; 2006-2021 Jean-Philippe Lang\n</div>\n</div>\n\n<div id="ajax-indicator" style="display:none;"><span>\xe8\xbd\xbd\xe5\x85\xa5\xe4\xb8\xad...</span></div>\n<div id="ajax-modal" style="display:none;"></div>\n\n</div>\n</div>\n<div class="banner_area global_banner">\n<div class="banner banner_info" id="banner_content">\n  <ol>\n\t<li>\xe6\x97\xa5\xe6\x8a\xa5\xe5\xbc\xba\xe5\x88\xb6\xe5\xae\xa1\xe6\xa0\xb8\xe7\x9a\x84\xe6\x96\xb9\xe5\xbc\x8f\xe8\xbf\x9b\xe8\xa1\x8c\xe4\xba\x86\xe6\x94\xb9\xe5\x96\x84\xef\xbc\x8c\xe5\x8f\xaf\xe4\xbb\xa5\xe6\x89\xb9\xe9\x87\x8f\xe5\xa4\x84\xe7\x90\x86\xe4\xba\x86\xe3\x80\x82\xe5\xa4\xa7\xe5\xae\xb6\xe5\x9c\xa8\xe5\xbc\xba\xe5\xae\xa1\xe6\x97\xb6\xe5\x92\x8c\xe5\xae\xa1\xe6\xa0\xb8\xe4\xb8\x8d\xe9\x80\x9a\xe8\xbf\x87\xe7\x9a\x84\xe6\x97\xb6\xe5\x80\x99\xef\xbc\x8c\xe8\xaf\xb7\xe6\x8a\x8a\xe5\x8e\x9f\xe5\x9b\xa0\xe5\xa1\xab\xe5\x86\x99\xe4\xb8\x80\xe4\xb8\x8b\xe3\x80\x82</li>\n\t\t<li>\xe8\x81\x8c\xe8\x83\xbd\xe7\xbb\x84\xe9\x95\xbf\xe5\x8f\xaf\xe4\xbb\xa5\xe5\xbe\x88\xe6\x96\xb9\xe4\xbe\xbf\xe5\x9c\xb0\xe6\x9f\xa5\xe7\x9c\x8b\xe7\xbb\x84\xe5\x91\x98\xe7\x9a\x84\xe6\x97\xa5\xe6\x8a\xa5\xe4\xba\x86\xe3\x80\x82</li>\n\t\t<li>\xe9\xa3\x9e\xe4\xb9\xa6\xe6\x89\x93\xe9\x80\x9a\xef\xbc\x9a\xe9\xa1\xb9\xe7\x9b\xae\xe5\xbc\x80\xe5\x90\xaf\xe9\xa3\x9e\xe4\xb9\xa6\xe6\xb6\x88\xe6\x81\xaf\xe9\x80\x9a\xe7\x9f\xa5\xe5\x8a\x9f\xe8\x83\xbd\xe5\x90\x8e\xef\xbc\x8c\xe9\x97\xae\xe9\xa2\x98\xe7\x9a\x84\xe5\x88\x9b\xe5\xbb\xba\xe5\x92\x8c\xe6\x9b\xb4\xe6\x96\xb0\xe4\xbc\x9a\xe9\x80\x9a\xe8\xbf\x87\xe9\xa3\x9e\xe4\xb9\xa6\xe6\x9c\xba\xe5\x99\xa8\xe4\xba\xba\xe5\xbf\xab\xe9\x80\x9f\xe9\x80\x9a\xe7\x9f\xa5\xe7\x9b\xb8\xe5\x85\xb3\xe5\xaf\xb9\xe5\xba\x94\xe8\x80\x85</li>\n\t</ol>\n</div>\n  <div class="banner_edit">\n    \n<a class="icon banner-icon-off" title="\xe5\x85\xb3\xe9\x97\xadBanner\xe6\xa8\xaa\xe5\xb9\x85\xe4\xbf\xa1\xe6\x81\xaf\xe3\x80\x82" data-remote="true" href="/banner/off?moderate=yes">\xe5\x85\xb3\xe9\x97\xad</a>\n  </div>\n\n</div>\n\n<script type="text/javascript">\n  $(document).ready(function () {\n    displayTopBanner();\n  });\n\n  $(window).resize(function () {\n    console.log("resize");\n    displayTopBanner();\n  });\n</script>\n\n \n<script>\n//<![CDATA[\nsetSelect2Filter(\'people\', {"format_state":"formatStateWithAvatar","min_input_length":1,"url":"/people/new/autocomplete_for_manager"});\n//]]>\n</script>\n\n  <script>\n//<![CDATA[\nsetSelect2Filter(\'issue_tags\', {"url":"http://redmine-pa.mxnavi.com/auto_completes/redmine_tags"});\n//]]>\n</script>\n\n</body>\n</html>\n'

    # resp_html = etree.HTML(content)
    resp_html = etree.HTML(response_with_code.content)
    # print(resp_html)
    resp_list = resp_html.xpath("//table[@id='workreport-table']/tbody")
    # print(resp_list)
    # print("in")
    # for tr in resp_list[0].xpath("//tr")[2::]:
    #     if len(tr) == 2:
    #         continue
    #     clock_time = str(tr.xpath("./td/text()")[1]).replace("\n", "").strip().split(" ")[1]
    #     log.d("clock_time:", clock_time)
    #     clock_in[workday] = clock_time
    #     break
    # print(clock_in)
    current_tr = resp_list[0].xpath("//tr")
    work_total_time = str(current_tr[-1].xpath("./td/text()")[-1]).replace("\n", "").replace(" ", "")
    if len(current_tr) <= 3:
        log.info("无打卡记录")
        if weekdays.is_workday(workday):
            log.info("工作日未打卡视为请假")
            clock_in[workday] = "-"
            clock_go_home[workday] = "-"
            delay_map[workday] = 0
            vacations_map[workday] = "今天请假了，记得请假哦"
    else:
        go_home_time = "-"
        vacations_map[workday] = ""
        log.d("len(current_tr)", len(current_tr))
        if len(current_tr) > 4:
            go_home_time = str(current_tr[-2].xpath("./td/text()")[1]).replace("\n", "").strip()
        clock_time = str(current_tr[2].xpath("./td/text()")[1]).replace("\n", "").strip().split(" ")[1]
        clock_in[workday] = clock_time
        clock_go_home[workday] = go_home_time
        log.d("go_home_time", go_home_time)
        log.d("clock_time", clock_time)
        log.d("work_total_time", work_total_time)
    return work_total_time


def get_time_at_company(input_month):
    log.info_out("统计在岗时间")
    response = requests.get("https://redmine-pa.mxnavi.com/cardinfos", headers=m_browser.headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    hidden_code = soup.find(name="input", attrs={"name": "code"})["value"]
    # print("hidden_code", hidden_code)
    # print(soup)
    work_days = weekdays.get_days_until_today_with_month(input_month)
    log.d("work_days", work_days)
    work_time_by_days = {}
    for workday in work_days:
        url = f"https://redmine-pa.mxnavi.com/selectcardinfo?utf8=%E2%9C%93&code={hidden_code}" \
              f"&event_time%5B%5D={workday}&commit=%E6%9F%A5%E8%AF%A2"
        log.d("usl is ", url)
        response_with_code = requests.get(url, headers=m_browser.headers)

        worktime = find_work_time(response_with_code, workday)
        work_time_by_days[workday] = worktime
        time.sleep(0.2)
    calculate_leave_time()
    calculate_vacation()
    log.info(f"delay : {delay_map}")
    log.info(f"vacations : {vacations_map}")
    log.d("work_time_by_days", work_time_by_days)
    return work_time_by_days


def get_work_time(url):
    # print(browser.get_cookies())
    log.info_out("统计已登记日报")
    response = requests.get(url, headers=m_browser.headers)
    soup = BeautifulSoup(response.content, 'html.parser')

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
    if table_headers == [] or table_values == []:
        return
    table_dic["header"] = table_headers[0]
    table_dic["values"] = table_values
    return table_dic


def total_time_to_file(table_dic, input_month):
    log.info_out("统计时间制成表格")
    # print(table_dic)
    print_lst = [
        str("日期" + "\t" + "请假类型" + "\t" + "请假时间" + "\t" + "工时" + "\t" + "加班时间" + "\t" + "在岗时长"
            + "\t" + "漏填日报" + "\t" + "上班打卡" + "\t" + "下班打卡" + "\t" + "迟到未请假" + "\t" + "加班串休" + "\n")]
    fill_value = table_dic.get("values")
    workday = 0
    external_work = float(0)
    holiday_time = 0
    work_at_weekend = []
    for item in fill_value:
        log.d("work_item: ", item)

        # 当日多条记录
        if len(item) != 13:
            # 当日多条记录
            if len(item) == 10 and item[4] == '' and item[7] == '':
                if item[1] == "事假" or item[1] == "病假":
                    holiday_time += float(item[5])
                last_item = print_lst[len(print_lst) - 1].split("\t")
                current_day_total = float(item[5]) + float(last_item[3])
                current_holiday_type = item[1] if last_item[1] == "" else last_item[1]
                current_holiday_time = item[5]
                last_external_work_time = float(last_item[4])

                log.d("current_holiday_time 1", current_holiday_time)
                if last_item[1] != "":
                    current_holiday_type = last_item[1] + "+" + item[1]
                    current_holiday_time = f"{last_item[2]} + {item[5]} = {float(last_item[2]) + float(item[5])}"
                    current_day_total += float(last_item[2])

                external_work = external_work - last_external_work_time + current_day_total - 8
                new_item_string = last_item[0] + "\t" + current_holiday_type + "\t" + current_holiday_time \
                                  + "\t" + last_item[3] \
                                  + "\t" + str("%.2f" % (current_day_total - 8)) \
                                  + "\t" + last_item[5] \
                                  + "\t" + str(
                    "%.2f" % (0 if 8 - float(current_day_total) < 0 else 8 - float(current_day_total))) \
                                  + "\t" + last_item[7] \
                                  + "\t" + last_item[8] \
                                  + "\t" + last_item[9] \
                                  + "\t" + last_item[10]
                print_lst[len(print_lst) - 1] = new_item_string + "\n"
                if item[0] != "请假" and delay_map.get(item[0], 0) - float(item[5]) <= 0:
                    delay_map[item[0]] = 0
                log.d("latest_item", new_item_string)
                # print("item", item)
            continue
        # 请假在上
        if item[5] == '':
            workday += 1
            if item[2] == "事假" or item[2] == "病假":
                holiday_time += float(item[6])
            current_external_work_time = 0 if (float(item[7]) + float(item[6]) - 8) < 0 else float(item[7]) + float(
                item[6]) - 8
            external_work += current_external_work_time
            log.d("current_external_work_time", current_external_work_time)
            log.d("external_work", external_work)
            total_work = float(item[7]) + float(item[6])
            standard_time = 0 if 8 - total_work < 0 else 8 - float(total_work)

            print_lst.append(str(item[0] + "\t" + item[2] + "\t" + item[6] + "\t" + item[7]
                                 + "\t" + str("%.2f" % current_external_work_time)
                                 + "\t" + item[8]
                                 + "\t" + str("%.2f" % standard_time)
                                 + "\t" + clock_in[item[0]]
                                 + "\t" + clock_go_home[item[0]]
                                 + "\t" + str("" if delay_map.get(item[0], 0) - float(
                item[6]) <= 0 else f"迟到了,要请假{delay_map.get(item[0], 0)}小时")
                                 + "\t" + vacations_map[item[0]]
                                 + "\n"))
            if delay_map.get(item[0], 0) - float(item[6]) <= 0:
                delay_map[item[0]] = 0
        else:
            this_date = item[0].split("-")
            year = int(this_date[0])
            month = int(this_date[1])
            day = int(this_date[2])
            work_date = datetime.date(year, month, day)
            log.info(work_date)
            # 周末或假期上班
            if not weekdays.is_workday(work_date):
                external_work += float(item[7])
                print_lst.append(str(item[0] + "\t" + "" + "\t" + "" + "\t" + item[7] + "\t" + item[7]
                                     + "\t" + item[7] + "\t" + str("%.2f" % (float(item[8]) - float(item[7])))
                                     + "\t" + clock_in[item[0]]
                                     + "\t" + clock_go_home[item[0]]
                                     + "\t" + str(
                    "" if delay_map.get(item[0], 0) == 0 else f"迟到了,要请假{delay_map.get(item[0], 0)}小时")
                                     + "\t" + vacations_map[item[0]]
                                     + "\n"))
                work_at_weekend.append(item[0])
                log.info("date in holiday")
            # 工作日
            else:
                workday += 1
                external_work += float("%.2f" % (0 if float(item[7]) - 8 < 0 else float(item[7]) - 8))
                print_lst.append(
                    str(item[0] + "\t" + "" + "\t" + "" + "\t" + item[7]
                        + "\t" + str("%.2f" % (0 if float(item[7]) - 8 < 0 else float(item[7]) - 8)))
                    + "\t" + item[8]
                    + "\t" + str("%.2f" % (0 if 8 - float(item[7]) < 0 else 8 - float(item[7])))
                    + "\t" + clock_in[item[0]]
                    + "\t" + clock_go_home[item[0]]
                    + "\t" + str(
                        "" if delay_map.get(item[0], 0) == 0 else f"迟到了,要请假{delay_map.get(item[0], 0)}小时")
                    + "\t" + vacations_map[item[0]]
                    + "\n")
                log.info("date in workday")

    log.d("workday", workday)

    log.d("external_work ", str("%.2f" % external_work))
    log.d("holiday_time", holiday_time)
    log.d("external_work: ", external_work)
    holiday_hour = external_work // 20 * 8
    log.d("holiday_hour: ", holiday_hour)
    log.info(print_lst)
    expect_worktime = len(weekdays.get_workdays_by_month(input_month)) * 8
    delay_time_total = 0
    for value in delay_map.values():
        delay_time_total += value
    log.d("delay_time_total: ", delay_time_total)
    # 可串休是固定的
    # 5 剩余串休 = 可串休 - 已请假 - 预计请假
    # 6 扣工资工时 = 0 if 剩余串休 > 0 else 0 - 剩余串休
    # 7 预计迟到请假是固定的
    # 8 请假时间预算 = 已请假 + 预计迟到
    field_item_5_temp = holiday_hour - holiday_time - delay_time_total
    field_item_5 = float("%.2f" % (0 if field_item_5_temp < 0 else field_item_5_temp))
    log.d("field_item_5_temp: ", field_item_5_temp)
    log.d("field_item_5: ", field_item_5)

    calculate_header = ["当前负荷", "预计加班时间", "已加班", "可串休", "已请假", "预计请假工时", "请假总预算", "剩余串休", "扣工资工时"]
    calculate_value = [str("%.3f" % float(external_work / expect_worktime + 1)), "",
                       str("%.2f" % external_work), holiday_hour, holiday_time,
                       str(delay_time_total),
                       str("%.2f" % (delay_time_total if holiday_time == 0 else holiday_time + delay_time_total)),
                       str(field_item_5),
                       str("%.2f" % (0 if holiday_hour - field_item_5 > 0 else abs(holiday_hour - field_item_5)))]

    return [print_lst, calculate_header, calculate_value, work_at_weekend]


"""
loss_work_time = {'2024-01-04': ['8.1'], '2024-01-05': ['8.81'], '2024-01-08': ['1.88']}

"""
def calculate_loss_time(loss_work_time):
    if loss_work_time == {}:
        log.info("没有需要填写的日报")
        return []

    chooses = list(loss_work_time.keys())
    log.info(chooses)

    input_date = weekdays.get_first_and_end_day_by_month(validate_input_result)
    # 如果是当前月，最后一个未填日报一定是当天，因此默认 -1 ，不是当月不减
    if input_date[0].month == weekdays.get_current_month():
        chooses = chooses[:len(chooses) - 1]

    return chooses


def log_work_time(local_browser, chooses):
    log.d("_chooses", chooses)
    while len(chooses) != 0:
        all_issues_url = """https://redmine-pa.mxnavi.com/issues?c%5B%5D=project&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=subject&f%5B%5D=status_id&f%5B%5D=assigned_to_id&f%5B%5D=project.status&op%5Bassigned_to_id%5D=%3D&op%5Bproject.status%5D=%3D&op%5Bstatus_id%5D=o&set_filter=1&sort=priority%3Adesc%2Cupdated_on%3Adesc&v%5Bassigned_to_id%5D%5B%5D=me&v%5Bproject.status%5D%5B%5D=1&v%5Bstatus_id%5D%5B%5D="""
        local_browser.get(all_issues_url)
        time.sleep(1)

        if len(chooses) > 1:
            log.info_out(" ".join([f"{index}.{chooses[index]} " for index in range(len(chooses))]))
            what_input = input("请选择填写日报日期序号(按非数字键退出)：")
            if not what_input.isdigit():
                log.info("非数字， 退出")
                return 0
            choose_index = eval(what_input)
            if choose_index not in range(len(chooses)):
                log.info_out("请输入有效的序号")
                continue

            log.info_out(f"您选择的序号是：{choose_index}")
        else:
            choose_index = 0
            log.info_out(f"继续填写{chooses[0]}的日报")

        issue_id = input("请输入要登记工时的任务id：")
        url = f"https://redmine-pa.mxnavi.com/issues/{issue_id}/time_entries/new"
        local_browser.get(url)

        date_input = local_browser.find_element(By.ID, "time_entry_spent_on")
        utils.use_js_change_value(local_browser, "time_entry_spent_on", chooses[choose_index])
        time.sleep(1.5)

        work_hours_input = local_browser.find_element(By.ID, "time_entry_hours")
        comments_input = local_browser.find_element(By.ID, "time_entry_comments")
        day_logged_time_info = local_browser.find_element(By.ID, "day_logged_time")
        commit_button = local_browser.find_element(By.NAME, "commit")
        continue_button = local_browser.find_element(By.NAME, "continue")

        day_logged_time = day_logged_time_info.text
        logged_time = day_logged_time[day_logged_time.index(": ") + 2:day_logged_time.index(","):]
        total_time = day_logged_time[day_logged_time.index("间：") + 2:day_logged_time.index("(单位")]
        log.info_out(day_logged_time)

        input_work_hours = input("请输入要登记的时间(可空，填入全部在岗时间)：")
        input_work_comments = input("请输入要登记的注释（可空）：")
        if input_work_hours == "":
            residue_time = float(total_time) - float(logged_time)
            if residue_time < 0:
                log.info_out("日报已填写")
                continue
            input_work_hours = str("%.2f" % (float(total_time) - float(logged_time)))

        if date_input:
            work_hours_input.send_keys(input_work_hours)
            comments_input.send_keys(input_work_comments)
            if eval(input_work_hours) < float(total_time):
                continue_button.click()
            else:
                commit_button.click()

        time.sleep(2)
        residue_time = float("%.2f" % 0 if (float(total_time) - float(logged_time) - float(input_work_hours)) <= 0
                             else float(total_time) - float(logged_time) - float(input_work_hours))

        if residue_time == 0:
            chooses.pop(choose_index)

        if len(chooses) == 0 and residue_time == 0:
            log.info_out("日报填写完成")
            return 1
        else:
            is_goon = input("是否继续填写日报 Y/N")
            if is_goon == "Y" or is_goon == "y":
                continue
            else:
                log.info_out("日报填写完成，结束运行")
                return 1
    else:
        return 0


def show_work_report(work_list, worktime_by_days_dict, work_at_weekend):
    # print(work_list)
    tb = ptb.PrettyTable()
    # 表头
    tb.field_names = work_list[0].replace("\n", "").split("\t")
    # 表数据
    new_list = work_list[1::]
    rows = []
    external_work = 0
    for item in new_list:
        field_item = item.replace("\n", "").split("\t")
        log.info(field_item)
        lst = [field_item[0], field_item[1], field_item[2], field_item[3], field_item[4], field_item[5], field_item[6],
               field_item[7], field_item[8], field_item[9], field_item[10]]
        log.info(lst)
        actual_time = field_item[5] if field_item[5] > field_item[3] else field_item[3]
        if field_item[2] != "":
            # 算假期
            if "=" in field_item[2]:
                _external = eval(field_item[2].split("= ")[1]) + eval(actual_time) - 8
            else:
                _external = eval(field_item[2]) + eval(actual_time) - 8
        else:
            # 周末
            if field_item[0] in work_at_weekend:
                _external = eval(actual_time)
            else:
                _external = eval(actual_time) - 8

        external_work += 0 if _external < 0 else _external

        rows.append(lst)
        date_date = field_item[0].split("-")
        date = datetime.date(int(date_date[0]), int(date_date[1]), int(date_date[2]))
        if field_item[6] != "" and field_item[6] != "0.00":
            remain_work_time = float(field_item[5]) - float(field_item[3])
            if remain_work_time < float(field_item[6]):
                log.info_out(f"{field_item[0]} 是请假了吗？记得请假哦")
                vacations_map[field_item[0]] = f"{field_item[0]} 总工时不足，记得请假哦"
                lst[10] = f"{field_item[0]} 总工时不足，记得请假哦" if lst[10] == "" else lst[10] + "\n" + f"{field_item[0]} 总工时不足，记得请假哦"
            elif float(remain_work_time) > 0.2:
                loss_work_time_dict[field_item[0]] = [field_item[2], field_item[3], field_item[5]]

        if len(worktime_by_days_dict) != 0:
            worktime_by_days_dict.pop(date.strftime("%Y-%m-%d"))

    if len(worktime_by_days_dict) != 0:
        for key in worktime_by_days_dict.keys():
            # 当周末加班但是没填工时时，应该作为候选
            # if key in work_at_weekend:
            #     continue
            value = worktime_by_days_dict[key]
            if value == '0.0' and not weekdays.is_workday(key):
                continue
            loss_list = [key, "", "", "", "", value, value, clock_in.get(key, ""), clock_go_home.get(key, ""),
                         str("" if delay_map.get(key, 0) == 0 else f"迟到了,要请假{delay_map.get(key, 0)}小时"), vacations_map.get(key, "")]
            loss_work_time_dict[key] = [value]

            if weekdays.is_workday(key):
                _external = eval(value) - 8
            else:
                _external = eval(value)

            external_work += 0 if _external < 0 else _external
            rows.append(loss_list)

    rows.sort(key=lambda i: i[0], reverse=False)
    tb.add_rows(rows)
    log.info_out("请查看：")
    log.info_out(tb)
    sorted_vacations_map = dict(sorted(vacations_map.items(), key=lambda i: i[0]))
    datas = {
        tb.field_names[0]: list(item[0] for item in rows),
        tb.field_names[1]: list(item[1] for item in rows),
        tb.field_names[2]: list(item[2] for item in rows),
        tb.field_names[3]: list(eval(item[3]) if item[3] != "" else 0 for item in rows),
        tb.field_names[4]: list(eval(item[4]) if item[4] != "" else 0 for item in rows),
        tb.field_names[5]: list(eval(item[5]) if item[5] != "" else 0 for item in rows),
        tb.field_names[6]: list(eval(item[6]) if item[6] != "" else 0 for item in rows),
        tb.field_names[7]: list(clock_in_time for clock_in_time in clock_in.values()),
        tb.field_names[8]: list(go_home for go_home in clock_go_home.values()),
        tb.field_names[9]: list(delay_time for delay_time in delay_map.values()),
        tb.field_names[10]: list(vacation for vacation in sorted_vacations_map.values())
    }

    return external_work, datas


def show_work_report_analysis(work_total):
    tb_total = ptb.PrettyTable()
    tb_total.field_names = ["当前负荷", "预计加班时间", "已加班", "可串休", "已请假", "预计请假工时", "请假总预算", "剩余串休", "扣工资工时"]
    tb_total.add_row(work_total)
    log.info_out(tb_total)
    return {
        tb_total.field_names[0]: [work_total[0]],
        tb_total.field_names[1]: [work_total[1]],
        tb_total.field_names[2]: [work_total[2]],
        tb_total.field_names[3]: [work_total[3]],
        tb_total.field_names[4]: [work_total[4]],
        tb_total.field_names[5]: [work_total[5]],
        tb_total.field_names[6]: [work_total[6]],
        tb_total.field_names[7]: [work_total[7]],
        tb_total.field_names[8]: [work_total[8]]
    }


def get_external_worktime(worktime_by_days_dict):
    total = 0
    for key in worktime_by_days_dict.keys():
        total += 0 if eval(worktime_by_days_dict[key]) - 8 < 0 else eval(worktime_by_days_dict[key]) - 8
    return total


def parse_args():
    parser = argparse.ArgumentParser(description='这是一个示例程序')

    # 添加参数
    parser.add_argument('--log', type=int, help='一个整数', default=0)
    # 解析参数
    args = parser.parse_args()
    # 使用参数
    return args.log


def calculate_leave_time():
    delay_number = 2
    clock_in_time_str = "09:00:00"
    clock_in_standard_time = datetime.datetime.strptime(clock_in_time_str, "%H:%M:%S")
    for key, value in clock_in.items():
        if value == "-":
            log.info("无打卡记录")
            delay_map[key] = 0
            continue
        value_to_time = datetime.datetime.strptime(value, "%H:%M:%S")
        knock_off_time = value_to_time + datetime.timedelta(hours=8)
        knock_off_map[key] = knock_off_time
        if value_to_time > clock_in_standard_time:
            diff = value_to_time - clock_in_standard_time
            log.info("相差{}分".format(diff.seconds // 60))
            delay_minutes = diff.seconds / 60
            if 0 < diff.seconds < 60:
                delay_map[key] = 0
            elif 1 < delay_minutes <= 30 and delay_number != 0:
                delay_number -= 1
                delay_map[key] = 0
                vacations_map[key] = f"迟到不足30分钟，迟到次数还剩{delay_number}"
            elif 1 < delay_minutes <= 60:
                delay_map[key] = 1
            else:
                quotient, remainder = divmod(delay_minutes - 60, 30)
                log.d("quotient", quotient)
                log.d("remainder", remainder)
                if remainder != 0 and quotient != 0:
                    delay_map[key] = quotient * 0.5 + 0.5 + 1
                elif remainder == 0 and quotient != 0:
                    delay_map[key] = quotient + 0.5 + 1
                else:
                    delay_map[key] = 0.5 + 1
                vacations_map[key] = f"迟到超过30分钟，要请假{delay_map[key]}小时"
        else:
            delay_map[key] = 0


def calculate_vacation():
    go_home_21_str = "21:00:00"
    go_home_21_time = datetime.datetime.strptime(go_home_21_str, "%H:%M:%S")
    go_home_22_str = "22:00:00"
    go_home_22_time = datetime.datetime.strptime(go_home_22_str, "%H:%M:%S")
    go_home_24_str = "00:00:00"
    go_home_24_time = datetime.datetime.strptime(go_home_24_str, "%H:%M:%S")
    go_home_4_str = "04:00:00"
    go_home_4_time = datetime.datetime.strptime(go_home_4_str, "%H:%M:%S")
    for key, value in clock_go_home.items():
        if value == '-':
            log.info("无打卡记录")
            continue
        # 日期
        leave_day = value.split(" ")[0]
        # 时间字符串
        time_to_leave = value.split(" ")[1]
        # 转换成可比较的时间
        value_to_time = datetime.datetime.strptime(time_to_leave, "%H:%M:%S")
        # 第二天离开
        if not leave_day == key:
            if value_to_time > go_home_4_time:
                vacations_map[key] = "打车可报销\n明天可串休8h"
            elif value_to_time > go_home_24_time:
                vacations_map[key] = "打车可报销\n明天可串休3h"
        else:
            if go_home_21_time < value_to_time < go_home_22_time:
                vacations_map[key] = "打车可报销"
            elif value_to_time > go_home_22_time:
                vacations_map[key] = "打车可报销\n明天可串休1h"
            else:
                vacations_map[key] = vacations_map[key] if vacations_map.get(key, "") != "" else ""
        clock_go_home[key] = value.split(" ")[1]


# ios 运行可能要在mac上运行pyinstaler
# windows
#  ..\python_workspace\Scripts\pyinstaller.exe -F .\work_report.py
#  --add-binary "chromedriver.exe;." --add-binary "chromedriver_116.exe;."
#  --add-binary "chromedriver_115.exe;."
if __name__ == '__main__':
    loss_work_time_dict = {}
    # log = Log(parse_args())
    log = Log(0)
    clock_in = {}
    clock_go_home = {}
    delay_map = {}
    knock_off_map = {}
    vacations_map = {}

    try:
        while True:
            year_month = input("请输入要查询的年月份(例如2023.8或8，仅查询当年月份，可空，默认为当月)")
            validate_input_result = weekdays.in_three_month(year_month)
            if validate_input_result is None:
                log.info_out("仅支持查询近3月日报,请重新输入")
            else:
                break

        login_result = m_browser.auto_login(log, validate_input_result)
        if login_result is None:
            log.info_out("浏览器加载失败，结束运行")
            sys.exit()

        browser, origin_url = login_result[0], login_result[1]
        log.info_out("页面加载中，请稍后...")

        # 好像只能这样了，请假的
        work_time_by_days_dict = get_time_at_company(validate_input_result)
        log.info_out("在岗时间统计完成")
        # work_time_by_days_dict = {'2023-09-01': '8.33', '2023-09-02': '0.0', '2023-09-03': '0.0', '2023-09-04': '10.15', '2023-09-05': '11.73', '2023-09-06': '7.61', '2023-09-07': '5.48', '2023-09-08': '8.08', '2023-09-09': '0.0', '2023-09-10': '0.0', '2023-09-11': '2.41'}
        work_time_dict = get_work_time(origin_url)
        log.info_out("统计已登记日报完成")
        # print(work_time_dict)
        work_time_info, work_time_header, work_time_value, work_weekend = total_time_to_file(work_time_dict, validate_input_result)
        log.info_out("表格制作完成\n\n")
        _external_work, _datas = show_work_report(work_time_info, work_time_by_days_dict, work_weekend)
        # print(table_csv_string)
        # print(_external_work)
        # print(work_time_value)
        work_time_value[1] = "%.2f" % _external_work
        _datas_analysis = show_work_report_analysis(work_time_value)
        # print("%.2f" % _external_work)
        # print(work_time_value)
        # write_to_file(table_csv_string, calculate_header, calculate_value)
        # write_to_excel(_datas, _datas_analysis)
        # write_to_file(work_time_info, work_time_header, work_time_value)

        # work_list = ['日期\t请假类型\t请假时间\t工时\t加班时间\t在岗时长\t漏填日报\n', '2023-08-01\t\t\t11.4\t3.40\t11.41\t0.00\n', '2023-08-02\t串休假\t1.0\t8.1\t1.10\t8.1\t0.00\n', '2023-08-03\t\t\t8.0\t0.00\t8.03\t0.00\n', '2023-08-04\t\t\t9.18\t1.18\t9.18\t0.00\n', '2023-08-07\t\t\t8.0\t0.00\t8.03\t0.00\n', '2023-08-08\t\t\t8.15\t0.15\t8.15\t0.00\n', '2023-08-09\t\t\t11.0\t3.00\t11.05\t0.00\n', '2023-08-10\t\t\t8.3\t0.30\t8.33\t0.00\n', '2023-08-11\t事假\t1.0\t7.5\t0.50\t4.55\t0.00\n', '2023-08-14\t\t\t12.0\t4.00\t12.06\t0.00\n', '2023-08-15\t串休假\t1.0\t8.2\t1.20\t8.25\t0.00\n', '2023-08-16\t\t\t8.3\t0.30\t8.36\t0.00\n', '2023-08-17\t事假\t1.0\t7.6\t0.60\t7.66\t0.00\n', '2023-08-18\t\t\t8.0\t0.00\t8.05\t0.00\n', '2023-08-19\t\t\t2.0\t2.0\t\t\n', '2023-08-21\t\t\t9.1\t1.10\t9.13\t0.00\n', '2023-08-22\t事假\t1.0\t9.16\t2.16\t9.16\t0.00\n', '2023-08-23\t\t\t8.0\t0.00\t8.05\t0.00\n', '2023-08-24\t\t\t8.0\t0.00\t8.05\t0.00\n', '2023-08-25\t事假\t5.0\t3.0\t0.00\t3.0\t0.00\n', '2023-08-28\t\t\t8.1\t0.10\t8.11\t0.00\n', '2023-08-29\t\t\t8.1\t0.10\t8.16\t0.00\n', '2023-08-30\t年假\t1.0\t0.0\t0.00\t7.33\t7.00\n']
        # show_work_report(work_list)

        loss_time = calculate_loss_time(loss_work_time_dict)
        # print(loss_time)
        if len(loss_time) != 0:
            log_result = log_work_time(browser, loss_time)

            if log_result != 0:
                re_cat = input("是否重新查看工作报告：Y/N")
                if re_cat == "Y" or re_cat == "y":
                    work_time_by_days_dict = get_time_at_company(validate_input_result)

                    work_time_dict = get_work_time(origin_url)

                    work_time_info, work_time_header, work_time_value, work_weekend = total_time_to_file(work_time_dict,
                                                                                                         validate_input_result)
                    _external_work, _datas = show_work_report(work_time_info, work_time_by_days_dict, work_weekend)
                    work_time_value[1] = "%.2f" % _external_work

                    # print(table_csv_string)
                    _datas_analysis = show_work_report_analysis(work_time_value)
                    # write_to_file(table_csv_string, calculate_header, calculate_value)
                    # write_to_file(work_time_info, work_time_header, work_time_value)
        log.d("_datas", _datas)
        m_write.write_to_excel(log, _datas, _datas_analysis)
        log.info_out("完成")
        browser.quit()
    except Exception as e:
        print("出现异常：", e)
        log.info(e)
        log_file = open("error.log", "a+")
        now = datetime.datetime.now()
        error_message = traceback.format_exc()
        log.info_out_to_file(now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3], error_message, log_file)
        log_file.close()

    while True:
        input_string = input("输入Enter退出")
        if input_string + "1" != "":
            sys.exit()


# 测试代码
# test_url()
# log = Log(1)
# clock_in = {}
# clock_go_home = {}
# delay_map = {}
# knock_off_map = {}
# clock_in = {"2023-12-01": "2023-12-01 08:57:27", "2023-12-02": "2023-12-02 09:07:27"}
# clock_in = {
#     "2023-12-01": "08:57:27",
#     "2023-12-04": "09:05:21",
#     "2023-12-05": "08:55:18",
#     "2023-12-06": "08:52:34",
#     "2023-12-07": "09:36:05",
#     "2023-12-08": "08:51:02",
#     "2023-12-11": "08:55:39",
#     "2023-12-12": "09:14:17",
#     "2023-12-13": "08:53:38",
#     "2023-12-14": "09:39:50",
#     "2023-12-15": "11:28:55",
#     "2023-12-18": "08:57:19",
#     "2023-12-19": "09:14:46",
#     "2023-12-20": "08:54:08",
#     "2023-12-21": "09:07:06"
# }
# work_days = weekdays.get_days_until_today_with_month(12)
# for workday in work_days:
#     find_work_time(1, workday)
# calculate_leave_time()
