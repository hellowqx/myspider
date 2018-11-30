import random
import re
from urllib import request
from fake_useragent import UserAgent
import chardet


import pymysql


ua=UserAgent()
base_url="http://finance.eastmoney.com/news/"
target_url=request.Request('http://finance.eastmoney.com/news/cgsxw.html')
target_url.add_header('User-agent',ua.random)
headers={'User-agent': ua.random}
response=request.urlopen(target_url)
# myheader=request.ProxyHandler({'http':'106.75.169.71:3128'})
# myopen=request.build_opener(myheader)
# response=myopen.open(target_url)
html=response.read()
encoding=chardet.detect(html).get('encoding')
html=html.decode(encoding,'ignore')

news=re.findall(r'<div[^>]class="text\s+text-no-img">\s+<p[^>]class="title">\s+<a[^>]href=".*?"\s+target="_blank">\s+(.*?)\s+</a>\s+</p>\s+<p[^>]class="info".*?>\s+(.*?)\s+</p>\s+<p\s+class="time">\s+(.*?)\s+</p>\s+</div>',html,re.S)
for i in news:
    print(i[0])
    print(i[1])
    print(i[2])


spider_con = pymysql.connect(host='127.0.0.1', port=3306,
                                     database='spider', user='root', password='root', charset='utf8')

cursor = spider_con.cursor()

while True:
    next_page = re.findall(r'25</a>\s*<a\s+href="(.*?)".*?class="page-btn">下一页</a>', html)
    print(next_page)
    if len(next_page) <= 0:
        print("数据采集完毕")
        break

    req=request.Request(base_url+next_page[0],headers=headers)

    response=request.urlopen(req)

    html=response.read()
    encoding = chardet.detect(html).get('encoding')
    html = html.decode(encoding, 'ignore')

    news = re.findall(
        r'<div[^>]class="text\s+text-no-img">\s+<p[^>]class="title">\s+<a[^>]href=".*?"\s+target="_blank">\s+(.*?)\s+</a>\s+</p>\s+<p[^>]class="info".*?>\s+(.*?)\s+</p>\s+<p\s+class="time">\s+(.*?)\s+</p>\s+</div>',
        html, re.S)

    for new in news:
        print(new[0])
        print(new[1])
        print(new[2])
        sql= "INSERT INTO news(title, connet,time) VALUES('{}', '{}', '{}')".format(new[0], new[1], new[2])
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            spider_con.commit()

        except:
            # 如果发生错误则回滚
            spider_con.rollback()

        # 关闭数据库连接


        spider_con.close()



