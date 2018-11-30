from fake_useragent import UserAgent
from lxml import html
import time
import pymysql
import requests

ua=UserAgent()

#登录
def login_(login_url):

    headers={'User-Agent':ua.random,
             # 'Referer':'http://follow.renren.com/list/968836401/pub/v7',
             # 'Cookies':'anonymid=jor07f1n-y3ieri; depovince=HEN; _r01_=1; ick_login=34527c7d-f7e3-4aa2-adae-415642c8767d; ick=b0d96011-cd91-4317-a2d8-2dd680118f31; t=a18d75d0ef442e643b665a2e1923c87a1; societyguester=a18d75d0ef442e643b665a2e1923c87a1; id=968836401; xnsid=ca41b56f; XNESSESSIONID=62aee16216d9; jebecookies=2cf55aaa-efac-4dad-acaf-6419c5c5bcfc|||||; ch_id=10016; JSESSIONID=abcTnGrL863Yz6Hl9V1Cw; jebe_key=73566578-425c-416d-a454-44831e44bb0a%7C19b7eaa2f045298656e4d0b6686cdf0e%7C1542795027270%7C1%7C1542795027473; wp_fold=0; Hm_lvt_966bff0a868cd407a416b4e3993b9dc8=1542795096; _ga=GA1.2.1269493477.1542795097; _gid=GA1.2.14545837.1542795097; _ga=GA1.3.1269493477.1542795097; _gid=GA1.3.14545837.1542795097; Hm_lpvt_966bff0a868cd407a416b4e3993b9dc8=1542795150; ver=7.0; loginfrom=null; wp=0; vip=1; __utma=151146938.1269493477.1542795097.1542800819.1542800819.1; __utmc=151146938; __utmz=151146938.1542800819.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'

             }
    authentication={'email':17637938180,'password':'222888'}
    session=requests.session()
    response=session.post(login_url,headers=headers,data=authentication)
    response.encoding='utf-8'
    content=response.text
    return session,response

###################################################

# #插入数据库
# def insertinfo(data):
#
#     connect=pymysql.Connect(
#         host='localhost',
#         port='3306',
#         user='root',
#         password='root',
#         db='spider',
#         charset='utf8',
#     )
#
#     cursor=connect.cursor()
#     sql="INSERT INTO renren(name,sex,birth,job,add)  VALUES ('%s','%s','%s','%s','%s')"
#     cursor.execute(sql,(data['name'],data['sex'],data['birth'],data['job'],data['add']))
#     connect.commit()
#     print('写入成功')
#     #游标关闭
#     cursor.close()
#     connect.close()

# #得到网页
def get_html(url):
    session,response=login_("http://www.renren.com/PLogin.do")
    headers={'User-Agent':ua.random}
    req=session.get(url,headers=headers,cookies=response.cookies)
    req.encoding='utf-8'
    content=req.text
    docs=html.fromstring(content)
    #返回可以被xpath解析的对象
    return docs

# #得到个人信息
# def get_info_personal(docs):
def get_info(docs):
    data=dict()
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
        # insertinfo(data)

        # 关注我的人的链接
        careme_url = docs.xpath('//li[@class="nf-group-item"]/a[text()="关注"]/@href')[0]
        docs1 = get_html(careme_url)
        link1 = docs1.xpath("//div[@class='info']/a[@class='name']/@href")
        link1 = link1 if len(link1) >0 else None

        #我关注的人
        mycare_url=docs1.xpath("//div[@class='follow_tab clearfix']//li[5]/a/@href")[0]
        docs2 = get_html(mycare_url)
        link2 = docs2.xpath("//div[@class='info']/a[@class='name']/@href")
        link2 = link2 if len(link2) > 0 else None


        #个人所有人的连接
        return link1,link2,data



# #获取别人的信息
# def get_info_other(docs):
def get_info1(docs):
    data=dict()
    allinfo=docs.xpath("//div[@id='profile_wrapper']")
    for i in allinfo:

        # print(i.xpath('string(.)').strip())
        name=i.xpath(".//div[@id='cover']/div[@class='cover-bg']/h1[@class='avatar_title no_auth']/text()")
        name = name[0].strip() if len(name) > 0 else None
        job=i.xpath(".//li[@class='work']/span/text()")
        job= job[0].strip() if len(job) >0 else None
        sex=i.xpath(".//li[@class='birthday']/span[1]/text()")
        sex = sex[0].strip() if len(sex) > 0 else None
        birth=i.xpath(".//li[@class='birthday']/span[2]/text()")
        birth = birth[0].strip() if len(birth) > 0 else None
        add=i.xpath(".//ul/li[@class='address']/text()")
        add = add[0].strip() if len(add) > 0 else None
        #
        data['job']=job
        data['name']=name
        data['add']=add
        data['birth']=birth
        data['sex']=sex

        # insertinfo(data)

        # 关注他的人的链接
        careme_url = docs.xpath('//ul[@class="nf-group-list"]//a[text()="关注"]/@href')[0]
        docs1 = get_html(careme_url)
        link1 = docs1.xpath("//ul[@id='follow_list']/li/div[@class='info']/a[@class='name']/@href")
        link1 = link1 if len(careme_url) > 0 else None

        #他关注的人的连接
        mycare_url=docs1.xpath("//div[@class='module border']/div[@class='follow_tab clearfix']/ul/li[2]/a/@href")[0]
        docs2 = get_html(mycare_url)
        link2 = docs2.xpath("//ul[@id='follow_list']/li/div[@class='info']/a[@class='name']/@href")
        link2 = link2 if len(link2) > 0 else None

        #他的所有人的连接
        return link1,link2,data

set1=set()
def main(url, type=0):

    # 请求目标url地址指向的网页，转换成xpath对象
    docs = get_html(url)
    # 采集目标数据
    alls = get_info(docs) if type == 0 else get_info1(docs)


    # print(alls[0]) #todo 关注我的人的主页链接
    print(alls[1]) #todo 我关注的人的主页链接
    print(alls[2]) #todo 我关注的人的主页链接

    # 采集我关注的人  没有关注的人停止？
    # if alls[1] and len(alls[1]) > 0:
    #     for i in alls[1]:
    #         set1.add(i)
    # print(set1,1111111111)
    # # for i in set1:
    # #     main(i, 1)
    #

    #
    # # 采集我关注我的人
    if alls[1] and len(alls[1]) > 0:
        for i in alls[1]:
            print(i,1111111111111111111)
            if len(i)>0:
                main(i,1)
            else:
                pass


if __name__ == '__main__':
    url="http://www.renren.com/profile"
    main(url)


'''
1. 用户登录[需要封装]
2. 数据转换[url地址-> xpath对象]
3. 获取数据[通过指定的xpath语法获取指定的数据]【函数简化(参数控制功能)】

class RenrenSpider():
    # 人人网用户数据爬虫程序
    
    def __init__(self, username, userpass):
        self.username = username
        self.userpass = userpass
        self.cookie = self.__login()
        self.html_data = None
        
    def __login(self):
        # 完成用户的登录认证
        return cookie
    
    def parse(self,url):
        # 解析指定的url地址，采集目标数据的函数：公开方法
        # 获取目标数据
        html_data = __get_html(url)
        # 转换数据
        x_data = __convert_data(html_data)
        # 获取数据
        name, like, liked = self.__get_personal_info()        
        # 数据持久化
        对象方法调用
    
    def __get_html(self, url):
        # 采集目标数据
        html_data = requests.get(url....
        return html_data
    
    def __convert_data(self, html_data):
        # 将html字符串转换成xpath对象
        return xpath_data
    
    def __get_personal_info(self):
        # 通过xpath进行筛选目标数据
        name = self.__get_personal_name('...')
        like = self.__get_personal_like('...')
        liked = self.__get_personal_liked('...')
        
        return name, like, liked
    
    def __get_personal_name(self, xpath_):
        # 获取目标用户数据
        return name
    
    def __get_personal_like(self, xpath_):
        # 获取关注的人的链接集合
        return like_links_set
        
    def __get_personal_liked(self, xpath_):
        # 获取我关注的人的链接集合
        return liked_links_set

class DataHelper():
    pass
    
    
if __name__ == "__main__":
    spider = RenrenSpider('username', 'password')
    spider.parse("http://www.renren.com")
'''