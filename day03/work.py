from fake_useragent import UserAgent
from lxml import html
import time
import pymysql
import requests
import chardet
ua=UserAgent()

#获取登录页面数据
login_url = "http://www.renren.com/PLogin.do"
headers={'User-Agent':ua.random,
         # 'Referer':'http://follow.renren.com/list/968836401/pub/v7',
         # 'Cookies':'anonymid=jor07f1n-y3ieri; depovince=HEN; _r01_=1; ick_login=34527c7d-f7e3-4aa2-adae-415642c8767d; ick=b0d96011-cd91-4317-a2d8-2dd680118f31; t=a18d75d0ef442e643b665a2e1923c87a1; societyguester=a18d75d0ef442e643b665a2e1923c87a1; id=968836401; xnsid=ca41b56f; XNESSESSIONID=62aee16216d9; jebecookies=2cf55aaa-efac-4dad-acaf-6419c5c5bcfc|||||; ch_id=10016; JSESSIONID=abcTnGrL863Yz6Hl9V1Cw; jebe_key=73566578-425c-416d-a454-44831e44bb0a%7C19b7eaa2f045298656e4d0b6686cdf0e%7C1542795027270%7C1%7C1542795027473; wp_fold=0; Hm_lvt_966bff0a868cd407a416b4e3993b9dc8=1542795096; _ga=GA1.2.1269493477.1542795097; _gid=GA1.2.14545837.1542795097; _ga=GA1.3.1269493477.1542795097; _gid=GA1.3.14545837.1542795097; Hm_lpvt_966bff0a868cd407a416b4e3993b9dc8=1542795150; ver=7.0; loginfrom=null; wp=0; vip=1; __utma=151146938.1269493477.1542795097.1542800819.1542800819.1; __utmc=151146938; __utmz=151146938.1542800819.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'

         }
authentication={'email':17637938180,'password':'222888'}
session=requests.session()
response=session.post(login_url,headers=headers,data=authentication)
response.encoding='utf-8'
content=response.text

data=dict()

#插入数据库
def insertinfo(data):
    connect=pymysql.Connect(
        host='localhost',
        port='3306',
        user='root',
        password='root',
        db='spider',
        charset='utf8',
    )

    cursor=connect.cursor()
    sql="INSERT INTO renren(name,sex,birth,job,add)  VALUES ('%s','%s','%s','%s','%s')"
    cursor.execute(sql,(data['name'],data['sex'],data['birth'],data['job'],data['add']))
    connect.commit()
    print('写入成功')
    #游标关闭
    cursor.close()
    connect.close()

#得到网页
def get_html(url):
    headers={'User-Agent':ua.random}
    req=session.get(url,headers=headers,cookies=response.cookies)
    req.encoding='utf-8'
    content=req.text
    docs=html.fromstring(content)
    return docs

#得到个人信息
def get_info(docs):
    allinfo=docs.xpath("//div[@id='profile_wrapper']")
    for i in allinfo:

    # print(i.xpath('string(.)').strip())
        name=i.xpath(".//div[@id='cover']/div[@class='cover-bg']/h1[@class='avatar_title no_auth']/text()")
        name = name if len(name) > 0 else None
        job=i.xpath(".//li[@class='work']/span/text()")
        job= job if len(job) >0 else None
        sex=i.xpath(".//li[@class='birthday']/span[1]/text()")
        sex = sex if len(sex) > 0 else None
        birth=i.xpath(".//li[@class='birthday']/span[2]/text()")
        birth = birth if len(birth) > 0 else None
        add=i.xpath(".//ul/li[@class='address']/text()")
        add = add if len(add) > 0 else None

        data['job']=job[0].strip()
        data['name']=name[0].strip()
        data['add']=add[0].strip()
        data['birth']=birth[0].strip()
        data['sex']=sex[0].strip()
        # print(data)
        # insertinfo(data)

        # 关注我的人的链接
        careme_url = docs.xpath('//li[@class="nf-group-item"]/a[text()="关注"]/@href')

        docs1 = get_html(careme_url)
        link1 = docs1.xpath("//div[@class='info']/a[@class='name']/@href")
        link1 = link1 if len(careme_url) > 0 else None
        #我关注的人
        mycare_url=docs1.xpath("//div[@class='follow_tab clearfix']//li[5]/a/@href")[0]
        docs2 = get_html(mycare_url)
        link2 = docs2.xpath("//div[@class='info']/a[@class='name']/@href")
        link2 = link2 if len(mycare_url) > 0 else None

        #个人所有人的连接
        links=link1+link2
        return links,data


#通过连接得到个人信息 和 所有连接

def all(url):
    docs=get_html(url)
    alls=get_info(docs)
    return alls



personal_url="http://www.renren.com/profile"
a=all(personal_url)
print(a[0],a[1])





#获取别人的信息
def get_info1(docs):
    allinfo=docs.xpath("//div[@id='profile_wrapper']")
    for i in allinfo:

    # print(i.xpath('string(.)').strip())
        name=i.xpath(".//div[@id='cover']/div[@class='cover-bg']/h1[@class='avatar_title no_auth']/text()")
        name = name if len(name) > 0 else None
        job=i.xpath(".//li[@class='work']/span/text()")
        job= job if len(job) >0 else None
        sex=i.xpath(".//li[@class='birthday']/span[1]/text()")
        sex = sex if len(sex) > 0 else None
        birth=i.xpath(".//li[@class='birthday']/span[2]/text()")
        birth = birth if len(birth) > 0 else None
        add=i.xpath(".//ul/li[@class='address']/text()")
        add = add if len(add) > 0 else None

        data['job']=job[0].strip()
        data['name']=name[0].strip()
        data['add']=add[0].strip()
        data['birth']=birth[0].strip()
        data['sex']=sex[0].strip()
        # print(data)
        # insertinfo(data)

        # 关注他的人的链接
        careme_url = docs.xpath('//ul[@class="nf-group-list"]//a[text()="关注"]/@href')
        docs1 = get_html(careme_url)
        link1 = docs1.xpath("//ul[@id='follow_list']/li/div[@class='info']/a[@class='name']/@href")
        link1 = link1 if len(careme_url) > 0 else None

        #他关注的人的连接
        mycare_url=docs1.xpath("//div[@class='module border']/div[@class='follow_tab clearfix']/ul/li[2]/a/@href")[0]
        docs2 = get_html(mycare_url)
        link2 = docs2.xpath("//ul[@id='follow_list']/li/div[@class='info']/a[@class='name']")
        link2 = link2 if len(mycare_url) > 0 else None

        #他的所有人的连接
        links=link1+link2
        return links,data