import re,requests

from lxml import html

import chardet
from fake_useragent import UserAgent
ua=UserAgent()
#表单数据
form_data=dict()
news_url='http://www.chemdatas.com/News/ENewsC.aspx'
#请求头
headers={
    'User-agent':ua.random,}

response=requests.get(news_url,headers=headers)
response.encoding='utf-8'

docs=html.fromstring(response.text)

title=docs.xpath("//table[@id='ctl00_ContentPlaceHolder1_GridView1']//tr/td/a/text()")
# print(title)

while True:
    # next_page=docs.xpath("//table[@id='ctl00_ContentPlaceHolder1_GridView1']//tr/td//tr/td/a/@href")
    # for i in next_page:
    #     next=re.findall(r'Page\$\d+',i)[0]
    #
    #     break

    for j in range(1,42):
        form_data['__EVENTTARGET'] = "ctl00$ContentPlaceHolder1$GridView1"
        form_data['__VIEWSTATEENCRYPTED'] = ""
        form_data['__EVENTARGUMENT'] ='Page$'+str(j)
        form_data['__VIEWSTATE'] = docs.xpath("//*[@id='__VIEWSTATE']/@value")[0]
    response=requests.post(news_url,headers=headers,data=form_data)
    response.encoding='utf-8'

    content=response.text
    print(content)
    break