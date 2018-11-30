import time
from selenium import webdriver
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,Integer,String,Text,Float
from sqlalchemy.orm import sessionmaker




# 创建无界面浏览器对向
def make_chrome():
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    chrome = webdriver.Chrome(options=options)
    return chrome





#sqlalchemy
Base=declarative_base()
class Table(Base):
    __tablename__='lunwen'

    id=Column(Integer,primary_key=True,autoincrement=True)
    title=Column(String(255))
    times=Column(String(255))


def insert(data):
    engine=create_engine('mysql+pymysql://root:root@localhost:3306/spider',encoding='utf-8')
    Session=sessionmaker(bind=engine)

    Base.metadata.create_all(engine)
    session = Session()

    session.add(data)
    session.commit()
    print('存储成功')
    session.close()

#下一页数据获取
def next_info(titles,timess):
    while True:
        #每页的文章
        for title,times in zip(titles,timess):
            time.sleep(1)
            print(times.text,title.text)
            data = Table(title=title.text,times=str(times.text))
            insert(data)

        print('本页采集完毕')
        try:
            next_page=chrome.find_element_by_xpath("//div[@class='conl']/table//tr[31]/td/table[@id='Table1']/tbody/tr/td/a[text()='下一页']")
            print(next_page.get_attribute('href'))
        except:
            print('没有下一页了')
            next_page = None
        #判断下一页存在
        if next_page is not None:
            next_page.click()
            titles = chrome.find_elements_by_xpath("//div[@class='conl']/table/tbody/tr/td[1]/a")
            timess = chrome.find_elements_by_xpath("//div[@class='conl']/table/tbody/tr/td[2]")

        else:
            break


#总期刊类型
if __name__ == '__main__':
    chrome=make_chrome()
    base_url = 'http://www.congwen.net'
    chrome.get(base_url)
    #点击导航栏论文
    daohang = chrome.find_element_by_xpath("//div[@id='nav']/ul/li[3]/a")
    daohang.click()

    alls = chrome.find_elements_by_xpath("//div[@class='conl']/table/tbody/tr/td/table/tbody/tr/td/div[1]/div[1]/a")
    #循环外部所有期刊内容
    for i in range(len(alls)):
        chrome.get(alls[i].get_attribute('href'))
        titles=chrome.find_elements_by_xpath("//div[@class='conl']/table/tbody/tr/td[1]/a")
        timess=chrome.find_elements_by_xpath("//div[@class='conl']/table/tbody/tr/td[2]")
        next_info(titles,timess)
        print('此类论文采集完毕————————————————————————————')
        chrome.get('http://www.congwen.net/Art.asp?c_id=41')
        alls = chrome.find_elements_by_xpath("//div[@class='conl']/table/tbody/tr/td/table/tbody/tr/td/div[1]/div[1]/a")


    chrome.close()
    chrome.quit()







# 60分钟3000条左右  睡眠1s