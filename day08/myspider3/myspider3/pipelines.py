# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class Myspider3Pipeline(object):


    def process_item(self, item, spider):
        # sql='insert into job(name,company,salary,addr,times,phone,intro,com_info) values(%s,%s,%s,%s,%s,%s,%s,%s)'
        # self.cursor.execute(sql,(item["name"],item["company"],item["salary"],item["addr"],item["times"],item["phone"],item["intro"],item["com_info"]))
        # self.connt.commit()
        return item


    # def open_spider(self,item):
    #
    #     self.connt=pymysql.connect(
    #         host='localhost',
    #         user='root',
    #         password='root',
    #         port=3306,
    #         db='spider',
    #         charset='utf8',
    #
    #     )
    #
    #
    #     self.cursor=self.connt.cursor()
    #
    #
    #
    # def close_spider(self,item):
    #     self.connt.commit()
    #     self.cursor.close()
    #     self.connt.close()
    #



