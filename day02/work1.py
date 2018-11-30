import lxml,chardet
from lxml import html
from urllib import request,parse
import pymysql
from fake_useragent import UserAgent


#
# html1=get_html('http://www.jokeji.cn/jokehtml/mj/2018111811582915.htm')
# htmls=get_html('http://www.jokeji.cn/list.htm')
# docs=html.etree.HTML(htmls)
# docs1=html.etree.HTML(html1)
# content=docs1.xpath('//span[@id="text110"]')
# target_data=docs.xpath('//b//a[@href]')
# # for i in target_data:
# #     print(i.xpath('string(.)').strip())
# next=docs1.xpath('//div[@class="zw_page1"]/a/@href')
# print(next)
# for i in content:
#     print(i.xpath('string(.)').strip())


# htmls=get_html('http://sydw.huatu.com/')
# docs=html.fromstring(htmls)
# time=docs.cssselect('.listSty01 li time')
# print(time)
# print(time[0].xpath('string(.)'))


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
def insert(time,title,address):
    try:
        conn = pymysql.connect(host="localhost", port=3306,
                               database="spider",
                               user="root", password="root", charset="utf8")
        cursor = conn.cursor()
        sql='INSERT INTO news(time,title,address) values("{}","{}","{}")'.format(time,title,address)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        print('写入成功')

    except Exception as e :
        print(e)

base_url='http://sydw.huatu.com'
htmls=get_html('http://sydw.huatu.com/ha/zhaopin/')
docs=html.etree.HTML(htmls)


times=docs.xpath('//ul[@class="listSty01"]/li/time')
addresss=docs.xpath('//ul[@class="listSty01"]/li/lm/a')
titles=docs.xpath('//ul[@class="listSty01"]/li/a')

#首页数据写入
for i in range(len(times)):
    # insert(times[i].xpath('string(.)').strip(), titles[i].xpath('string(.)').strip(),
    #        addresss[i].xpath('string(.)').strip())
    print('写入成功')


while True:
    #下一页
    next_url = docs.xpath('//li/a[text()="下一页"]/@href')
    if len(next_url)<=0:
        print('采集数据完毕')
        break
    next_urls=base_url+next_url[0]
    print(next_url,1111111111)
    htmls=get_html(next_urls)
    docs = html.etree.HTML(htmls)
    # times = docs.xpath('//ul[@class="listSty01"]/li/time')
    # addresss = docs.xpath('//ul[@class="listSty01"]/li/lm/a')
    # titles = docs.xpath('//ul[@class="listSty01"]/li/a')
    # for i in range(len(times)):
    #
    #     # insert(times[i].xpath('string(.)').strip(),titles[i].xpath('string(.)').strip(),addresss[i].xpath('string(.)').strip())
    #     print('写入成功')




