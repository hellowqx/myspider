from urllib import request,parse
from fake_useragent import UserAgent
import chardet
import re
import random

ua=UserAgent()
headers={'User-agent':ua.random}
target_url='http://www.89178.com/cyxc/?sec=2.d351866.1527043566.81.2.0&uckloadid=HdE8TB.39a2798&Sid=52&JJID=B58b3cf912e457597700639&mediaid=1&idzt=31509'
response=request.Request(target_url,headers=headers)
#自定义代理对象
# myheader=request.ProxyHandler({'http':'121111'})
# myopen=request.build_opener(myheader)

html=request.urlopen(response)
html=html.read()
encoding=chardet.detect(html).get('encoding')
html=html.decode(encoding,'ignore')

info=re.findall(r'<li>\s+<a.*?title="(.*?)">\s+<img.*?></a>.*?<div[^>]+class="xx-touzi clearfix zoom">\s+<em>.*?<i>(.*?)</i>人</em>.*?<span class="tr-money">(.*?)</span></div></li>',html,re.S)
print(info)



# def connectDB(self):
#     host = "localhost"
#     dbName = "spider"
#     user = "root"
#     password = "root"
#     # 此处添加charset='utf8'是为了在数据库中显示中文，此编码必须与数据库的编码一致
#     db = pymysql.connect(host, user, password, dbName, charset='utf8')
#     cursorDB = db.cursor()
#     return cursorDB
#
#
#  #数据插入表中
# def inserttable(self,insertTable,insertTime,insertTitle,insertaddress):
#
#     insertContentSql="INSERT INTO "+insertTable+"(time,title,addess)VALUES("+insertTime+" , "+insertTitle+" , "+insertaddress+")"
#     DB_insert=self.connectDB()
#     cursor_insert=DB_insert.cursor()
#     cursor_insert.execute(insertContentSql,(insertTime,insertTitle,insertaddress))
#     DB_insert.commit()
#     DB_insert.close()
#     print('inert contents to  '+insertTable+' successfully')
