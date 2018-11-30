# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MyspiderPipeline(object):

    def process_item(self, item, spider):
        sql='insert into test(name,price) value(%s,%s)'
        self.cursor.execute(sql,(item['name'],item['price']))
        self.connt.commit()

        return item



#爬虫程序启动时值执行一次
    def open_spider(self,spider):
        self.connt=pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='test_scrapy',
            port=3306,
            charset='utf8',
        )
        self.cursor=self.connt.cursor()

#关闭时只执行一次
    def close_spider(self,spider):
        self.connt.commit()
        self.cursor.close()
        self.connt.close()