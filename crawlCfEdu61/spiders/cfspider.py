# -*- coding: utf-8 -*-
import scrapy
from crawlCfEdu61.items import Crawlcfedu61Item

class CfspiderSpider(scrapy.Spider):
    name = 'cfspider'
    allowed_domains = ['codeforces.com']
    #是否显示打星
    postParams = "?action=toggleShowUnofficial&newShowUnofficialValue=true"
    start_urls = []

    for i in range(1,36):
        start_urls.append("https://codeforces.com/contest/1132/standings/page/"+str(i)+postParams)
    def parse(self, response):
        persons = response.css('tr[participantid]')
        items = []
        for each in persons:
            item = Crawlcfedu61Item()
            item['rank'] = each.xpath('./td[1]/text()')[0].extract().strip()
            item['name'] = each.xpath('./td[2]/a/text()')[0].extract().strip()
            item['number_solved'] = each.xpath('./td[3]/text()')[0].extract().strip()
            item['penalty'] = each.xpath('./td[4]/text()')[0].extract().strip()
            item['success_hacks'] = ''
            item['fail_hacks'] = ''
            for i in range(1,3):
                try:
                    hacks = each.xpath('./td[5]/span['+str(i)+']/text()')[0].extract().strip()
                    if hacks[0]=='+':
                        item['success_hacks'] = hacks
                    else:
                        item['fail_hacks'] = hacks
                except:
                    pass
            item['problems_detail'] = []
            item['time_detail'] = []
            for i in range(6,13):
                try:
                    try_cnt = each.xpath('./td[' + str(i) + ']/span[1]/text()')[0].extract().strip()
                    if try_cnt[0] == '+':
                        item['problems_detail'].append(try_cnt)
                        item['time_detail'].append(each.xpath('./td[' + str(i) + ']/span[2]/text()')[0].extract().strip())
                    else:
                        item['problems_detail'].append(try_cnt)
                        item['time_detail'].append('')
                except:
                    item['problems_detail'].append('')
                    item['time_detail'].append('')
            items.append(item)
        return items

