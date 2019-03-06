# IntroductionOfScrapy
介绍Scrapy基础用法及简单应用

以下均在终端下运行..

## 安装scrapy

* windows：pip install scrapy

  linux：apt-get install python-scrapy
## 创建scrapy项目

* scrapy startproject yourProjectName

  cd yourProjectName

  scrapy genspider yourSpiderName allowedDomain

## 爬虫项目主要文件

* scrapy.cfg : 定义爬虫设置文件的位置[settings] 和 项目名称[deploy]
* __init__.py : 将上级目录模块化
* items.py : 为要爬取内容占位，比如要爬取名字，则有name = scrapy.Field()
* pipelines.py : 爬虫爬取后具体如何处理item，每个item会单独处理，打印或写入文件等
* settings.py : 爬虫配置设置如user_agent以及遵守的规则等
* yourSpiderName.py : 爬虫爬取部分，GET成功返回200相应后从response解析html，支持css和xpath

## 调试网页

* scrapy shell crawledWebsite

  content = response.xpath(...)

  subContent = content.css(...)

## 编写后运行

* scrapy crawl yourSpiderName

# 爬取codeforces编程网站第 Educational Codeforces Round 61 (Rated for Div. 2) 场的排名、得分情况
网址：https://codeforces.com/contest/1132/standings

## 创建scrapy项目

* scrapy startproject crawlCfEdu61

  cd crawlCfEdu61

  scrapy genspider cfspider codeforces.com

## 编写items.py
* 我们要爬取的数据有排名/名字/解决问题数/罚时/hack次数/各个题的尝试次数及正确解题的时间

* rank = scrapy.Field() 

    name = scrapy.Field() 

    number_solved = scrapy.Field()

    penalty = scrapy.Field()

    success_hacks = scrapy.Field()

    fail_hacks = scrapy.Field()

    time_detail = scrapy.Field()

    problems_detail = scrapy.Field()

## settings.py修改

* USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0'
* ROBOTSTXT_OBEY = False

## 编写pipelines.py

* def process_item(self, item, spider):

​        with open('CfEdu61.csv',"a",encoding='utf-8',newline="") as f:

​            csv_writer = csv.writer(f)

​            new_item = []

​            new_item.append(item['rank'])

​            new_item.append(item['name'])

​            new_item.append(item['number_solved'])

​            new_item.append(item['penalty'])

​            new_item.append(item['success_hacks']+'/'+item['fail_hacks'])

​            for i in range(len(item['time_detail'])):

​                new_item.append(item['problems_detail'][i]+'/'+item['time_detail'][i])

​            csv_writer.writerow(new_item)

​        return item

## 编写spider.py

* start_urls为list类型，设置为要爬取的网页链接

* parse返回item的list，每个item为一个字典，通过key来访问

* 网页的response可以进行css、xpath解析获取所需数据

  查找css/xpath的小技巧，在火狐浏览器中按F12调试，点击检查的小箭头后，找到所需数据，点击并右击代码部分，点复制，可以选择复制css/xpath

* cmd模式下调试：

  scrapy shell https://codeforces.com/contest/1132/standings

  persons = response.css('tr[participantid]')

  print(persons[0])						

  输出：

  <Selector xpath='descendant-or-self::tr[@participantid]' data='<tr participantid="23513496">\r\n    <td>\r'>

  now = persons[0]

  name = now.xpath('./td[2]/a/text()')[0].extract().strip()

  print(name)

  输出：

  V--gLaSsH0ldEr593--V

## 运行爬虫

* scrapy crawl cfspider

## 处理数据

* 爬虫爬取页面没有先后顺序，所以要对rank进行升序

* 新建process.py，用pandas处理

* pandas排序部分：

  #header表示列索引，设置为None，即不把数据作为索引，names表示以names为列索引

  pd.read_csv(file_name,header=None,names=names)

  #对rank升序排序

  data.sort_values(by=['rank'],ascending=True)

  #重置行索引为升序自然数

  new_data.reset_index(drop=True)

  #写入新文件

  new_data.to_csv('../sorted.csv')


