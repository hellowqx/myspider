from fake_useragent import UserAgent

from bs4 import BeautifulSoup
from lxml import html
import requests

headers={"Accept":"*/*",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9",
"Connection":"keep-alive",
"Cookie":"yfx_c_g_u_id_10000042=_ck18112417462715517983830318101; VISITED_MENU=%5B%228528%22%5D; yfx_f_l_v_t_10000042=f_t_1543052787379__r_t_1543052787379__v_t_1543053062127__r_c_0",
"Host":" query.sse.com.cn",
"Referer":"http://www.sse.com.cn/assortment/stock/list/share/",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
         }
#返回页面和相册连接
def docss(url):
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    htmls=response.text
    docs=html.etree.HTML(htmls)
    return docs


url='http://query.sse.com.cn/security/stock/getStockListData2.do?&jsonCallBack=jsonpCallback62148&isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage=1&pageHelp.pageSize=25&pageHelp.pageNo=1&_=1543053062672'

docs=docss(url)

title=docs.xpath("//div[@id='j-smartSpec']/text()")
print(title)