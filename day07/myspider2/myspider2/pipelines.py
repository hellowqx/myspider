# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Myspider2Pipeline(object):
    def process_item(self, item, spider):
        sql='insert into animal(name,intro,link) values(%s,%s,%s)'
        self.cursor.execute(sql,(item['name'],item['intro'],item['link']))
        self.conn.commit()
        return item



    def open_spider(self,item):
        self.conn= pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            charset='utf8',
            db='spider'
        )
        self.cursor=self.conn.cursor()



    def close_spider(self,):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()