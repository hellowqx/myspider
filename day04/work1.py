import requests
from fake_useragent import UserAgent
from lxml import html
from bs4 import BeautifulSoup

from sqlalchemy import create_engine,Column, Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import  declarative_base
import sqlacodegen
ua=UserAgent()

#使用declarative_base创建对象基类
Base=declarative_base()
#定义表对象
class User(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True,autoincrement=True)
    author = Column(String(20))
    content = Column(String(255))


def insert_info(data):
    engine=create_engine('mysql+pymysql://root:root@localhost:3306/spider',encoding='utf-8')
    #创建session对象 绑定engine连接
    Session=sessionmaker(bind=engine)

    Base.metadata.create_all(engine) ######?
    session=Session()

    # _user=User(data)
    session.add(data)
    session.commit()
    print('储存成功')
    session.close()

def soups(url):
    headers={
        'User-agent':ua.random,
    }

    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    htmls=response.text
    htmls=(htmls.replace('<br>','')).replace('<br/>','')
    soup=BeautifulSoup(htmls,'lxml')
    return soup




#获取下一页
base_url='https://www.qiushibaike.com'
def next_pages(url):
    soup = soups(url)
    next_page = soup.select('span[class="next"]')[0].parent['href']
    if len(next_page) > 0:
        return next_page
    else:
        print('采集完毕++++++++++++++++++++++++++++++++++')

#主函数
def core(url):
    soup=soups(url)
    author=soup.select('h2')
    author = author if len(author) > 0 else None
    print(len(author))


    content =soup.select('div[class="content"] > span')
    content=content if len(content) >0 else None
    print(len(content))

    while 1:
        next_page = next_pages(url)
        next_urls = base_url+next_page
        #热门页第13页停止
        print(next_page)
        if len(next_page) > 0 and next_page !='/week/':
            print(next_urls)
            for i in author:
                list.append(i)
            data=User(author=i.string.strip(),content=i.string.strip())
            #     insert_info(data)
            # print('11111111111111111')
            core(next_urls)

        break

if __name__ == '__main__':

    core('https://www.qiushibaike.com')



