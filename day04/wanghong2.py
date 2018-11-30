from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,Integer,String,Text,Float
from sqlalchemy.orm import sessionmaker
from fake_useragent import UserAgent
ua=UserAgent()
from bs4 import BeautifulSoup
import requests


Base=declarative_base()
class Table(Base):
    __tablename__='wanghong'

    id=Column(Integer,primary_key=True,autoincrement=True)
    nickname=Column(String(20))
    fans=Column(String(20))
    weibo=Column(String(20))


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



def a(url):
    soup = soups(url)
    alls=soup.find_all('tr')
    for i in alls:
        nickname=i.select('span')
        if len(nickname) == 0:
            pass
        else:
            fans=i.select('td:nth-of-type(3)')
            weibo = i.select('td:nth-of-type(4)')
            data=Table(nickname=nickname[0].string,fans=fans[0].string,weibo=weibo[0].string)
            # insert(data)
            return soup


if __name__ == '__main__':
    base_url = 'http://www.wanghong100.com'
    url = 'http://www.wanghong100.com/wanghong'
    soup = soups(url)

    while True:
        next_page = soup.select('a[class="next"]')
        if len(next_page) > 0:
            next_url = base_url + next_page[0]['href']
            print(next_url)
            soup = a(next_url)

        else:
            print('采集完毕')
            break