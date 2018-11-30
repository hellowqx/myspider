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
def insert(time,title,content,links):
    try:
        conn = pymysql.connect(host="localhost", port=3306,
                               database="spider",
                               user="root", password="root", charset="utf8")
        cursor = conn.cursor()
        sql='INSERT INTO gameinfo(time,title,content,links) values("{}","{}","{}","{}")'.format(time,title,content,links)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        print('写入成功')

    except Exception as e :
        print(e)



gamehtml=get_html('http://www.ali213.net/news/game/')
base='http://www.ali213.net/news/game/'
docs=html.etree.HTML(gamehtml)

comments=docs.xpath('//div[@class="n_lone"]')
for i in comments:

    title=i.xpath('h2[@class="lone_t"]/a/text()') if len(i) >0 else None
    for j in title:
        print(j)
        

    # content=i.xpath('.//div[@class="lone_f_r_t"]/text()') if len(content) >0 else None
    # print(content)
    #
    # times=i.xpath('.//div[@class="lone_f_r_f"]/span[1]/text()') if len(times) >0 else None
    # print(times)
    # links=i.xpath('h2[@class="lone_t"]/a/@href') if len(links) >0 else None
    # insert(times[0],content[0],times[0],links[0])
# #首页数据
# for i in range(len(titles)):
#     insert(times[i].xpath('string(.)').strip(),titles[i].xpath('string(.)').strip(),
#            content[i].xpath('string(.)').strip(),links[i].strip())
#
#
# while True:
#     next_page=docs.xpath('//div[@class="p_bar"]//a[text()="下页"]/@href')
#     if len(next_page)<=0:
#         print('采集完毕')
#         break
#
#     next_url=base+next_page[0]
#     print(next_url)
#     gamehtml=get_html(next_url)
#     docs=html.etree.HTML(gamehtml)
#     titles = docs.xpath('//h2[@class="lone_t"]/a')
#     content = docs.xpath('//div[@class="lone_f_r_t"]')
#     times = docs.xpath('//div[@class="lone_f_r"]/div[2]//span[1]')
#     links = docs.xpath('//h2[@class="lone_t"]/a/@href')
#     for i in range(len(titles)):
#         insert(times[i].xpath('string(.)').strip(), titles[i].xpath('string(.)').strip(),
#                content[i].xpath('string(.)').strip(), links[i].strip())
#



#   insert(times[i].xpath('string(.)').strip(), titles[i].xpath('string(.)').strip(),
# IndexError: list index out of range