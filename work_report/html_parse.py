from lxml import etree

from bs4 import BeautifulSoup

string = """
<!DOCTYPE html>

<html lang="zh">
<head>
<meta charset="utf-8"/>
<meta content="IE=edge" http-equiv="X-UA-Compatible"/>
<title>美行项目管理平台</title>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<meta content="Redmine" name="description">
<meta content="issue,bug,tracker" name="keywords"/>
<meta content="authenticity_token" name="csrf-param"/>
<meta content="HLNMgPYlsFQbkxpo6bT1+LEXuVN3sDbDdKtwPmOKRI76y+idozw54ilC3LYNT3s+srvIpB7xgAIg3KWHMv11eQ==" name="csrf-token"/>
<link href="/favicon.ico?1653026646" rel="shortcut icon"/>
<link href="/stylesheets/jquery/jquery-ui-1.12.1.css?1653026646" media="all" rel="stylesheet"/>
<link href="/stylesheets/tribute-5.1.3.css?1653026646" media="all" rel="stylesheet"/>
<link href="/themes/circle/stylesheets/application.css?1653026646" media="all" rel="stylesheet"/>
<link href="/stylesheets/responsive.css?1653026646" media="all" rel="stylesheet"/>
<script src="/javascripts/jquery-3.5.1-ui-1.12.1-ujs-5.2.4.5.js?1653026646"></script>
<script src="/javascripts/jquery-migrate-3.3.2.min.js?1653026646"></script>
<script src="/javascripts/tribute-5.1.3.min.js?1653026646"></script>
<script src="/javascripts/tablesort-5.2.1.min.js?1653026646"></script>
<script src="/javascripts/tablesort-5.2.1.number.min.js?1653026646"></script>
<script src="/javascripts/application.js?1653026646"></script>
<script src="/javascripts/responsive.js?1653026646"></script>
<script>
//<![CDATA[
$(window).on('load', function(){ warnLeavingUnsaved('若离开当前页面，则该页面内未保存的内容将丢失。'); });
//]]>
</script>
<script src="/themes/circle/javascripts/theme.js?1653026646"></script>
<script>
//<![CDATA[
rm = window.rm || {};rm.AutoComplete = rm.AutoComplete || {};rm.AutoComplete.dataSources = '{"issues":"/issues/auto_complete?q=","wiki_pages":"/wiki_pages/auto_complete?q="}';
//]]>
</script>
<link href="/plugin_assets/redmine_agile/stylesheets/redmine_agile.css?1693801927" media="screen" rel="stylesheet"/> <link href="/plugin_assets/redmine_audit_series/stylesheets/audit_series.css?1693801927" media="screen" rel="stylesheet"/> <link href="/plugin_assets/redmine_banner/stylesheets/banner.css?1693801927" media="screen" rel="stylesheet"/><script src="/plugin_assets/redmine_banner/javascripts/banner.js?1693801927"></script> <link href="/plugin_assets/redmine_issue_badge/stylesheets/style.css?1693801927" media="screen" rel="stylesheet"/> <link href="/plugin_assets/redmine_issue_templates/stylesheets/issue_templates.css?1693801927" media="screen" rel="stylesheet"/> <link href="/plugin_assets/redmine_people/stylesheets/redmine_people.css?1693801927" media="screen" rel="stylesheet"/> <link href="/plugin_assets/redmine_crm/stylesheets/money.css?1693801926" media="screen" rel="stylesheet"/> <link href="/plugin_assets/redmine_searchable_selectbox/stylesheets/select2.min.css?1693801927" media="screen" rel="stylesheet"/><link href="/plugin_assets/redmine_searchable_selectbox/stylesheets/searchable_selectbox.css?1693801927" media="screen" rel="stylesheet"/><script src="/plugin_assets/redmine_searchable_selectbox/javascripts/select2.full.min.js?1693801927"></script><script src="/plugin_assets/redmine_searchable_selectbox/javascripts/searchable_selectbox.js?1693801927"></script>
<!-- page specific tags -->
<style type="text/css">
  .from-table
  {
    overflow-y: visible;
  }
  .from-table,.data-table
  {
    clear:left;
  }

  .from-table table td,.data-table table td
  {
    background: #F8FCF8;
    border:1px #c0c0c0 solid;
    text-align: center;
    padding:5px 3px;
    word-break: break-all;

  }

  .from-table table th,.data-table table th{
    font-size: 11px;
  }

  .from-table table th,.data-table table th
  {
    background: #cbd9d9;
    border:1px #c0c0c0 solid;
    text-align: center;
    padding:5px 3px;
    word-break: break-all;
  }
  .from-table table,.data-table table
  {
    border-collapse: collapse;
    border:1px solid #c0c0c0
  }
  .test{
    color: red;
  }

</style>
<script>
//<![CDATA[
var datepickerOptions={dateFormat: 'yy-mm-dd', firstDay: 0, showOn: 'button', buttonImageOnly: true, buttonImage: '/images/calendar.png?1653026646', showButtonPanel: true, showWeek: true, showOtherMonths: true, selectOtherMonths: true, changeMonth: true, changeYear: true, beforeShow: beforeShowDatePicker};
//]]>
</script><script src="/javascripts/i18n/datepicker-zh-CN.js?1653026646"></script> <link href="/plugin_assets/redmineup_tags/stylesheets/redmine_tags.css?1693801927" media="screen" rel="stylesheet"/>
<script src="/plugin_assets/redmineup_tags/javascripts/redmine_tags.js?1693801927"></script>
<script src="/plugin_assets/redmine_crm/javascripts/select2.js?1693801926"></script><link href="/plugin_assets/redmine_crm/stylesheets/select2.css?1693801926" media="screen" rel="stylesheet"/><script src="/plugin_assets/redmine_crm/javascripts/select2_helpers.js?1693801926"></script>
</meta></head>
<body class="theme-Circle has-main-menu controller-cardinfos action-index avatars-off">
<div id="wrapper">
<div class="flyout-menu js-flyout-menu">
<div class="flyout-menu__search">
<form accept-charset="UTF-8" action="/search" method="get" name="form-2098b439"><input name="utf8" type="hidden" value="✓"/>
<label class="search-magnifier search-magnifier--flyout" for="flyout-search">⚲</label>
<input class="small js-search-input" id="flyout-search" name="q" placeholder="搜索" type="text"/>
</form> </div>
<div class="flyout-menu__avatar flyout-menu__avatar--no-avatar">
<a href="/people/1541">wangleic</a>
</div>
<h3>项目</h3>
<span class="js-project-menu"></span>
<h3>一般</h3>
<span class="js-general-menu"></span>
<span class="js-sidebar flyout-menu__sidebar"></span>
<h3>简介</h3>
<span class="js-profile-menu"></span>
</div>
<div id="wrapper2">
<div id="wrapper3">
<div id="top-menu">
<div id="account">
<ul><li><a class="my-account" href="/my/account">我的帐号</a></li><li><a class="logout" data-method="post" href="/logout" rel="nofollow">退出</a></li></ul> </div>
<div id="loggedas">登录为 <a href="/people/1541">wangleic</a></div>
<ul><li><a class="home" href="/">主页</a></li><li><a class="my-page" href="/my/page">我的工作台</a></li><li><a class="projects" href="/projects">项目</a></li><li><a class="help" href="https://www.redmine.org/guide">帮助</a></li></ul></div>
<div id="header">
<a class="mobile-toggle-button js-flyout-menu-toggle-button" href="#"></a>
<div id="quick-search">
<form accept-charset="UTF-8" action="/search" method="get" name="form-7d88ab85"><input name="utf8" type="hidden" value="✓"/>
<input name="scope" type="hidden"/>
<label for="q">
<a accesskey="4" href="/search">搜索</a>:
        </label>
<input accesskey="f" class="small" data-auto-complete="true" id="q" name="q" size="20" type="text"/>
</form> <div class="drdn" id="project-jump"><span class="drdn-trigger">选择一个项目...</span><div class="drdn-content"><div class="quick-search"><input autocomplete="off" class="autocomplete" data-automcomplete-url="/projects/autocomplete.js?jump=cardinfos" id="projects-quick-search" name="q" type="text" value=""/></div><div class="drdn-items projects selection"><strong>最近使用</strong><a href="/projects/cp100004-honda-tsu3-0-04-tsu?jump=cardinfos" title="CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)"><span style="padding-left:0px;">CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)</span></a><a href="/projects/cp100003-honda-ota-tsu-2023-cr-01-ota-202306?jump=cardinfos" title="CP100003.Honda_三菱电机_TSU3.0-OTA-TSU_功能进化_2023+(CR)01.OTA(202306)"><span style="padding-left:0px;">CP100003.Honda_三菱电机_TSU3.0-OTA-TSU_功能进化_2023+(CR)01.OTA(202306)</span></a><a href="/projects/cp100001-honda-04-hondaapp?jump=cardinfos" title="CP100001.Honda_HMCT_CONNECT4.5_EV功能进化Demo+04.HondaAPP功能开发"><span style="padding-left:0px;">CP100001.Honda_HMCT_CONNECT4.5_EV功能进化Demo+04.HondaAPP功能开发</span></a><strong>所有的项目</strong><a href="/projects/cp100001-honda-04-hondaapp?jump=cardinfos" title="CP100001.Honda_HMCT_CONNECT4.5_EV功能进化Demo+04.HondaAPP功能开发"><span style="padding-left:0px;">CP100001.Honda_HMCT_CONNECT4.5_EV功能进化Demo+04.HondaAPP功能开发</span></a><a href="/projects/cp100003-honda-ota-tsu-2023-cr-01-ota-202306?jump=cardinfos" title="CP100003.Honda_三菱电机_TSU3.0-OTA-TSU_功能进化_2023+(CR)01.OTA(202306)"><span style="padding-left:0px;">CP100003.Honda_三菱电机_TSU3.0-OTA-TSU_功能进化_2023+(CR)01.OTA(202306)</span></a><a href="/projects/cp100003-honda-2023-cr-02-ota-202312?jump=cardinfos" title="CP100003.Honda_三菱电机_TSU3.0-OTA-TSU_功能进化_2023+(CR)02.OTA(202312)"><span style="padding-left:0px;">CP100003.Honda_三菱电机_TSU3.0-OTA-TSU_功能进化_2023+(CR)02.OTA(202312)</span></a><a href="/projects/cp100004-honda-tsu3-0-04-tsu?jump=cardinfos" title="CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)"><span style="padding-left:0px;">CP100004.Honda_海纳新思_TSU3.0维护项目+04.量产后维护(TSU)</span></a><a href="/projects/cp100005-honda-cabincontrol4-0?jump=cardinfos" title="CP100005.Honda_CabinControl4.0_阿尔派_量产后维护"><span style="padding-left:0px;">CP100005.Honda_CabinControl4.0_阿尔派_量产后维护</span></a><a href="/projects/cp100006-honda_cabincontrol4-0?jump=cardinfos" title="CP100006.Honda_CabinControl4.0_海纳新思_量产后维护"><span style="padding-left:0px;">CP100006.Honda_CabinControl4.0_海纳新思_量产后维护</span></a><a href="/projects/ot050001?jump=cardinfos" title="OT050001.技术中心"><span style="padding-left:0px;">OT050001.技术中心</span></a></div><div class="drdn-items all-projects selection"><a href="/projects?jump=cardinfos">所有的项目</a></div></div></div>
</div>
<h1>美行项目管理平台</h1>
<div class="tabs" id="main-menu">
<ul><li><a class="mx-cardinfo" href="/cardinfos">打卡记录相关</a></li><li><a class="workreport-audit" href="/workreports">日报相关</a></li></ul>
<div class="tabs-buttons" style="display:none;">
<button class="tab-left" onclick="moveTabLeft(this); return false;"></button>
<button class="tab-right" onclick="moveTabRight(this); return false;"></button>
</div>
</div>
</div>
<div class="nosidebar" id="main">
<div id="sidebar">
</div>
<div id="content">
<fieldset>
<fieldset>
<legend><h3 style="margin-top: 10px;">在岗工时统计规则</h3></legend>
<div class="from-table">
<pre class="test" style="margin-top: 10px;">  *1.上午从8：30开始计算在岗工时，中午午休时间（12：00～13：00）不作为在岗工时，计算时会自动扣除</pre>
<pre class="test" style="margin-top: 10px;">  *2.在岗期间，离开公司的工时，不作为在岗工时，计算时会自动扣除</pre>
</div>
</fieldset>
<!-- 查询 -->
<form accept-charset="UTF-8" action="/selectcardinfo" id="cardinfo_list_form" method="get" name="cardinfo_list_form-bc92f640"><input name="utf8" type="hidden" value="✓"/>
<fieldset>
<legend><h3 style="margin-top: 10px;">打卡记录查询</h3></legend>
<div class="from-table">
<table style="margin-top: 1px;width: 100%;">
<tr>
<td align="center">
            查询时间 :
            <input name="code" type="hidden" value="M000761"/>
<input id="event_time_" name="event_time[]" size="15" type="date" value="2023-09-08"/>
<script>
//<![CDATA[
$(function() { $('#event_time').addClass('date').datepickerFallback(datepickerOptions); });
//]]>
</script>
<input data-disable-with="查询" name="commit" type="submit" value="查询"/>
</td>
</tr>
</table>
</div>
</fieldset>
</form>
<fieldset>
<legend><h3 style="margin-top: 10px;">打卡记录列表详细,总工时：  7.95</h3> </legend>
<div class="data-table">
<table id="workreport-table" style="margin-top: 1px;width: 100%;">
<thead>
<tr>
<th align="center" width="20%"> 员工姓名</th>
<th align="center" width="60%"> 打卡记录</th>
<th align="center" width="20%"> 进出</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center" valign="middle">
              王磊C
            </td>
<td align="center" valign="middle">
              2023-09-08 09:08:11
            </td>
<td align="center" valign="middle">
               进门
            </td>
</tr>
<tr>
<td align="right" colspan="2">
              在岗时间：(H小时：M分钟)
            </td>
<td align="left" colspan="1" valign="middle">
              7.95
            </td>
</tr>
</tbody>
</table>
</div>
</fieldset>
</fieldset>
<div style="clear:both;"></div>
</div>
</div>
<div id="footer">
    Powered by <a href="https://www.redmine.org/">Redmine</a> © 2006-2021 Jean-Philippe Lang
</div>
</div>
<div id="ajax-indicator" style="display:none;"><span>载入中...</span></div>
<div id="ajax-modal" style="display:none;"></div>
</div>
</div>
<script>
//<![CDATA[
setSelect2Filter('people', {"format_state":"formatStateWithAvatar","min_input_length":1,"url":"/people/new/autocomplete_for_manager"});
//]]>
</script>
<script>
//<![CDATA[
setSelect2Filter('issue_tags', {"url":"http://redmine-pa.mxnavi.com/auto_completes/redmine_tags"});
//]]>
</script>
</body>
</html>
"""

resp_html = etree.HTML(string)
resp_list = resp_html.xpath("//table[@id='workreport-table']/tbody")
for item in resp_list:
    trs = item.findall("tr")
    trs_len = len(trs)
    target_time = trs[trs_len - 1].xpath("./td[2]/text()")[0].replace(" ", "").replace("\n", "")

    print(target_time)
