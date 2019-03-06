# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
class Crawlcfedu61Pipeline(object):
    def process_item(self, item, spider):
        with open('CfEdu61.csv',"a",encoding='utf-8',newline="") as f:
            csv_writer = csv.writer(f)
            new_item = []
            new_item.append(item['rank'])
            new_item.append(item['name'])
            new_item.append(item['number_solved'])
            new_item.append(item['penalty'])
            new_item.append(item['success_hacks']+'/'+item['fail_hacks'])
            for i in range(len(item['time_detail'])):
                new_item.append(item['problems_detail'][i]+'/'+item['time_detail'][i])
            csv_writer.writerow(new_item)
        return item
