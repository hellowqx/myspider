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
folder_path='./pic2/'
headers={'User-agent':ua.random}
#返回页面和相册连接
def docss(url):
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    htmls=response.text
    docs=html.etree.HTML(htmls)
    alllinks = docs.xpath("//ul/li/a[@class='TypeBigPics']/@href")
    return docs,alllinks



#页面所有相册的链接
def core1(url):
    docs,alllinks=docss(url)
    if os.path.exists(folder_path) == False:
        os.makedirs(folder_path)
    return alllinks

#保存图片并返回 页面和 本相册base地址
def pic_in(url2):
    docs=docss(url2)[0]
    base_ = re.findall(r'(h.*?/)\d+.*?.htm', url2)[0]
    # print(base_,'相册内部的基础地址')

    #进入相册页面下载图片的连接
    try:
        link=docs.xpath("//div[@id='ArticleId22']/p/a/img/@src")[0]
    except Exception as e :
        print(e,'查找图片链接方式2')
        link=docs.xpath("//div[@id='ArticleId0']/p/a/img/@src")[0]

    if link:
        html =requests.get(link)
        image_name=str(time.time())+'.jpg'
        # print(image_name)
        try:
            image=Image.open(BytesIO(html.content))
            image.save(folder_path+image_name)
        except:
            pass
            # print('第%d张图片下载完毕'%(index+1))
        time.sleep(0.2)
        print('本页采集完毕')


        return docs, base_

def xiazaixiangce(alllinks):
    for i in alllinks:
        print(i,'相册主地址')
        docs,base_=pic_in(i)
        while True:
            try:
                next_pages = docs.xpath("//div[@class='NewPages']/ul/li/a[text()='下一页']/@href")[0]
                # print(next_pages)
                if len(next_pages) > 1 :
                    #相册内部下一页
                    next_urls = base_ + next_pages
                    print(next_urls,'相册内部每张图片地址')
                    docs,base_=pic_in(next_urls)

                else:
                    print('本相册下载完毕————————————')
                    break
            except:
                pass


def core(url):
    docs = docss(url)[0]
    alls=docs.xpath("//ul/li/a[@class='TypeBigPics']/img/@src")
    return docs

if __name__ == '__main__':
    base_url = 'http://www.umei.cc'
    url = 'http://www.umei.cc/tags/mote_3.htm'
    docs =docss(url)[0]
    #第一页
    alllinks=core1(url)
    xiazaixiangce(alllinks)

    while True:

            next_page = docs.xpath("//div[@class='NewPages']/ul/li/a[text()='下一页']/@href")
            # print(next_page)
            if len(next_page) > 0:
                try:
                    next_url = base_url + next_page[0]
                    print(next_url)
                    #更新有下一页的页面
                    docs = docss(next_url)[0]
                    alllinks=core1(next_url)
                    xiazaixiangce(alllinks)
                except Exception as e :
                    print(e,'错误222222')
                    xiazaixiangce(alllinks)



            else:
                print('采集完毕_______________________________________________')
                break



