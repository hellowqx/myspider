import lxml,chardet
from lxml import html
from urllib import request,parse
import pymysql
from fake_useragent import UserAgent


#获取页面
ua=UserAgent()
def get_html(target_url):
    headers={'User-Agent':ua.random}
    req=request.Request(target_url,headers=headers)
    response=request.urlopen(req).read()
    decodeing=chardet.detect(response).get('encoding')
    html=response.decode(decodeing,'ignore')
    return html

#插入数据
def insert(time,title):
    try:
        conn = pymysql.connect(host="localhost", port=3306,
                               database="spider",
                               user="root", password="root", charset="utf8")
        cursor = conn.cursor()
        sql='INSERT INTO info(time,title) values("{}","{}")'.format(time,title)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        print('写入成功')

    except Exception as e :
        print(e)

htmls=get_html('http://www.cei.gov.cn//defaultsite/s/column/4028c7ca-37115425-0137-115605c5-000f_2018.html?articleListType=1&coluOpenType=1')
docs=html.etree.HTML(htmls)
title=docs.cssselect('.list_word_1 li a')
time=docs.cssselect('.list_word_1 li em')
for i in range(len(title)):
    print(time[i].xpath('string(.)').strip(), title[i].xpath('string(.)').strip())
    insert(time[i].xpath('string(.)').strip(), title[i].xpath('string(.)').strip())

while True:

    next_url=docs.xpath('//p[@class="fr"]/a[text()="下一页"]/@href')

    if len(next_url)<=0:
        print('数据采集完毕')
        break
    htmls=get_html(next_url[0])
    print(next_url[0],111111111)
    docs = html.etree.HTML(htmls)
    title = docs.cssselect('.list_word_1 li a')
    time = docs.cssselect('.list_word_1 li em')
    for i in range(len(title)):

        print(time[i].xpath('string(.)').strip(), title[i].xpath('string(.)').strip())
        insert(time[i].xpath('string(.)').strip(),title[i].xpath('string(.)').strip())


