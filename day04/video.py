from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,Integer,String,Text,Float
from sqlalchemy.orm import sessionmaker
from fake_useragent import UserAgent
ua=UserAgent()
from bs4 import BeautifulSoup
from lxml import html
import requests
import os,time
from io import BytesIO
from PIL import Image
import re
import threading


base_path='./pic3/'
headers={'User-agent':ua.random}
base_url='https:'


class Spider(object):
    def __init__(self):
        self.headers=headers
        self.offset=1


    def start_work(self,url):
        print("正在爬取第%s页>>>>>>>>" % self.offset)
        self.offset += 1
        response=requests.get(url,headers=self.headers)
        response.encoding='utf-8'
        htmls=response.text
        docs = html.etree.HTML(htmls)

        video_src=docs.xpath("//div[@class='video-play']/video/@src")
        video_title=docs.xpath("//a[@class='shade-box']/span[@class='video-title']/text()")
        next_page=docs.xpath("//div[@class='pagelist']/a[@class='next']/@href")
        next_url=base_url+next_page[0]
        print(next_url,'网页地址')
        #爬取完毕
        if len(next_page) <=0:
            return


        self.write_file(video_title,video_src)
        self.start_work(next_url)

    def write_file(self,video_title,video_src):
        if os.path.exists(base_path) ==False:
            os.makedirs(base_path)
        for src,title in zip(video_src,video_title):
            print(base_url+src,'视频地址')
            response=requests.get(base_url+src,headers=self.headers)
            file_name=title+'.mp4'
            file_name=''.join(file_name.split('/'))

            print('正在下载%s'% file_name)
            time.sleep(0.5)
            with open(base_path+ file_name,'wb') as f :
                f.write(response.content)


if __name__ == '__main__':
    url='https://ibaotu.com/shipin/7-5026-0-0-0-1.html'
    spider=Spider()
    # for i in range(0,3):
    spider.start_work(url)
        # t=threading.Thread(target=spider.start_work,args=(url))
        # t.start()












