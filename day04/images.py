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
folder_path='./pic/'


def docss(url):
    headers={'User-agent':ua.random}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    htmls=response.text
    docs=html.etree.HTML(htmls)
    return docs



def core(url):
    docs = docss(url)
    alls=docs.xpath("//img/@src")

    if os.path.exists(folder_path)==False:
        os.makedirs(folder_path)
    for index,i in enumerate(alls):

        if i:
            html =requests.get(i)
            image_name=str(time.time())+'.jpg'
            print(image_name)
            image=Image.open(BytesIO(html.content))
            image.save(folder_path+image_name)
            print('第%d张图片下载完毕'%(index+1))
            time.sleep(0.2)

    print('本页采集完毕')
    return docs

if __name__ == '__main__':
    base_url = 'http://www.umei.cc'
    url = 'http://www.umei.cc/tags/mote.htm'
    docs =docss(url)
    core(url)

    while True:
        next_page = docs.xpath("//div[@class='NewPages']/ul/li/a[text()='下一页']/@href")
        print(next_page)
        if len(next_page) > 0:
            next_url = base_url + next_page[0]
            print(next_url)
            docs = core(next_url)

        else:
            print('采集完毕_______________________________________________')
            break