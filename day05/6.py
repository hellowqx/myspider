from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,Integer,String,Text,Float
from sqlalchemy.orm import sessionmaker
from fake_useragent import UserAgent
ua=UserAgent()
from bs4 import BeautifulSoup
import requests,re


Base=declarative_base()
class Table(Base):
    __tablename__='python_info'

    id=Column(Integer,primary_key=True,autoincrement=True)
    title=Column(String(20))
    content=Column(Text)


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
    response.encoding='utf-8'
    htmls=response.text
    soup=BeautifulSoup(htmls,'lxml')
    return soup


base_url='http://www.wanghong100.com'
url='https://www.cnblogs.com/cate/python/'

soup=soups(url)
alls=soup.find_all(attrs={'class':'post_item_body'})
for i in alls:
    title=i.select('a[class="titlelnk"]')[0].string
    content=i.find(re.compile('<p[^>]+class="post_item_summary">\s+<a.*?>.*?</a>(.*?)</p>'))
    print(content)
#         data=Table(nickname=nickname[0].string,fans=fans[0].string,weibo=weibo[0].string)
#         insert(data)
#
#
# while True:
#     next_page=soup.select('a[class="next"]')
#     if len(next_page)>0:
#         next_url=base_url+next_page[0]['href']
#         print(next_url)
#         soup=soups(next_url)
#         alls = soup.find_all('tr')
#         for i in alls:
#             nickname = i.select('span')
#             if len(nickname) == 0:
#                 pass
#             else:
#                 fans = i.select('td:nth-of-type(3)')
#                 weibo = i.select('td:nth-of-type(4)')
#                 data = Table(nickname=nickname[0].string, fans=fans[0].string, weibo=weibo[0].string)
#                 insert(data)
#
#     else:
#         print('采集完毕')
#         break



