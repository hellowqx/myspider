from urllib import request,parse
import chardet,re,time
from fake_useragent import UserAgent
i=input('请输入翻译内容：')
salt=str(int(time.time()*1000 ))
ua=UserAgent()
# 翻译客户端
client = "fanyideskweb"
# 加密秘钥
key = "sr_3(QOHT)L2dx#uuGR@r"

import hashlib

src = client + i + salt + key
sign = hashlib.md5(src.encode("utf-8"))
form_data={
'i':i,
'from':'AUTO',
'to':'AUTO',
'smartresult':'dict',
'client':'fanyideskweb',
'salt':salt,
'sign':sign.hexdigest(),
'doctype':'json',
'version':'2.1',
'keyfrom':'fanyi.web',
'action':'FY_BY_REALTIME',
'typoResult':'false',
}
#设置请求头
headers={
    # 'User-Agent': ua.random,
    'Cookie': 'OUTFOX_SEARCH_USER_ID=1997907455@10.168.8.76; JSESSIONID=aaaMbrOrSN0Nv9P4ciWCw; OUTFOX_SEARCH_USER_ID_NCOO=918660913.8410245; ___rl__test__cookies=1542700699923',
    'Origin':'http://fanyi.youdao.com',
    'Proxy-Connection':'keep-alive',
    'Referer':'http://fanyi.youdao.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',

}
target_url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
#包装请求头
req=request.Request(target_url,data=parse.urlencode(form_data,encoding='utf-8').encode('utf-8'),headers=headers)
#正常请求
response=request.urlopen(req)
html=response.read()
#数据解码处理
encoding=chardet.detect(html).get('encoding')
html=html.decode(encoding,'ignore')
print(html)
