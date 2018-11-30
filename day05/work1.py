from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,Integer,String,Text,Float
from sqlalchemy.orm import sessionmaker
from fake_useragent import UserAgent
ua=UserAgent()
from bs4 import BeautifulSoup
import requests


Base=declarative_base()
class Table(Base):
    __tablename__='test1'

    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(20))
    price=Column(String(20))


def insert(data):
    engine=create_engine('mysql+pymysql://root:root@localhost:3306/spider',encoding='utf-8')
    Session=sessionmaker(bind=engine)

    Base.metadata.create_all(engine)
    session = Session()

    session.add(data)
    session.commit()
    print('存储成功')
    session.close()



def soups(url):
    headers={'User-agent':ua.random}
    response=requests.get(url,headers=headers)
    response.encoding='gb2312'
    htmls=response.text
    soup=BeautifulSoup(htmls,'lxml')
    return soup


# print(soups('https://car.autohome.com.cn/price/list-0-101-0-0-0-0-0-0-0-0-0-0-0-0-0-1.html'))


base_url='https://car.autohome.com.cn'
url='https://car.autohome.com.cn/price/list-0-101-0-0-0-0-0-0-0-0-0-0-0-0-0-1.html'



# def next_pages(url):
#     soup = soups(url)
#     next_page = soup.select('a[class="page-item-next"]')
#     if len(next_page) > 0:
#         next_page=next_page[0]['href']
#     return next_page




