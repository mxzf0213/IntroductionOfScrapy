# IntroductionOfScrapy
介绍Scrapy基础用法及简单应用

以下均在终端下运行..

##安装scrapy
* windows：pip install scrapy
  linux：apt-get install python-scrapy
  
##创建scrapy项目
* scrapy startproject yourProjectName
* cd yourProjectName
* scrapy genspider yourSpiderName allowedDomain

##爬虫项目主要文件
* scrapy.cfg : 定义爬虫设置文件的位置[settings] 和 项目名称[deploy]
* __init__.py : 将上级目录模块化
* items.py : 为要爬取内容占位，比如要爬取名字，则有name = scrapy.Field()
* pipelines.py : 爬虫爬取后具体如何处理item，每个item会单独处理，打印或写入文件等
* settings.py : 爬虫配置设置如user_agent以及遵守的规则等
* yourSpiderName.py : 爬虫爬取部分，GET成功返回200相应后从response解析html，支持css和xpath

##调试网页
* scrapy shell crawledWebsite
  content = response.xpath(...)
  subContent = content.css(...)

##编写后运行
* scrapy crawl yourSpiderName

#爬取codeforces编程网站第 Educational Codeforces Round 61 (Rated for Div. 2) 场的排名、得分情况
网址：https://codeforces.com/contest/1132/standings

##创建scrapy项目
* scrapy startproject crawlCfEdu61
  cd crawlCfEdu61
  scrapy genspider cfspider codeforces.com

#编写items.py
* rank = scrapy.Field()
    name = scrapy.Field()
    number_solved = scrapy.Field()
    penalty = scrapy.Field()
    success_hacks = scrapy.Field()
    fail_hacks = scrapy.Field()
    time_detail = scrapy.Field()
    problems_detail = scrapy.Field()
