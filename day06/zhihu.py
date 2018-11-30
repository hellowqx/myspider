import urllib
from fake_useragent import UserAgent
import requests,json
from lxml import html

headers={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    'Cookie':'_zap=f23a0290-4555-414f-a5d8-2774ca160bd8; _xsrf=DtFHjrT3OSVI0dK5RUH34HiIPFt4KpWb; d_c0="AKDi6wuSkw6PTvMe4R6WbFaLrkEt9KqOgxg=|1543201456"; q_c1=01c9a08e878b45b096858a291a21f89c|1543201483000|1543201483000; tst=f; l_n_c=1; n_c=1; auth_type=cXFjb25u|1543203719|11f2a083750f3def759c871d0cde825321a73763; token="MzJGRTUxNDgxQ0NBNUQ3RUUwOTc5NENBMDFFMjkyRTU=|1543203719|6894e8009aa67272257a33167860f8ae05449f2d"; client_id="QUVEOUI4QUYyNUNCNDVDNEQ5NDU0MkFCNkY5QTg4RUY=|1543203719|35d908918758e13fced35817cdaebf741a7af52c"; tgw_l7_route=bc9380c810e0cf40598c1a7b1459f027; cap_id="NzNkNjI3Yjg4YzliNDNmNWFiNGQ5MTAyMjNhYTM5ZTE=|1543211427|fd3f94c96471ca97a7c62624d8fca3ffec80f3c8"; r_cap_id="OTdhYzUzNDg0MDVjNGRiY2ExZmVkMGNmZmVkNTI0NjQ=|1543211427|3b53145c181b3b949f5f6d25add416d41d9d30de"; l_cap_id="MGVlYWM1NDgxYmUzNDI5MmJjOTE2MzdmNWFlZTMzMDQ=|1543211427|53f44279c783adb74be4500d70d9d439fcfafe5b"; capsion_ticket="2|1:0|10:1543211441|14:capsion_ticket|44:OTE3Mjg2MTcwMzU3NDBlN2FiNmU0YjU5OGY1OWRhNjk=|04f8c117636ded47620e80fa015c381d92246761e16fd2b53d364b3027b343a6"; z_c0="2|1:0|10:1543211487|4:z_c0|92:Mi4xYkNReEJ3QUFBQUFBb09MckM1S1REaVlBQUFCZ0FsVk4zOWZvWEFEejZZQU5MLURfbGNUQjdxSzlCT3g0ZFBGY0tR|f1de7246638f085fa7b965652ea5a39acbf8fb2fc7229315157c4b137fe26794',
    'authority':'zhihu-web-analytics.zhihu.com',
    'Referer':'http://www.zhihu.com/',


}
data={
    'email':'741599771@qq.com',
    'password':'wswqx2288',
    'rememberme':'true'
}


url='https://www.zhihu.com/people/kaifulee/followers'

def download(url):
    if url is None:
        return None

    try:
        session=requests.session()
        response=session.get(url,headers=headers,data=data)
        response.encoding='utf-8'

        if (response.status_code==200):
            return response.text
    except:
        return None
#
# def parse(response):
#     try:
#         print(response)
#         json_body=json.loads(response);
#         josn_data=json_body['data']
#
#         for item in josn_data:
#             if (not old_url_tokens.__contains__(item['url_token'])):
#                 if (not new_url_tokens.__len__()<2000):
#                     new_url_tokens.add(item['url_token'])
#
#             if (not saved_users_set.__contains__(item['url_token']))
#                 jj=json.dumps(item)
#                 save(item['url_token'],jj)
#                 saved_users_set.add(item['url_token'])
#         if (not json_body['paging']['is_end']):
#             next_url=json_body['paging']['next']
#             response2=download(next_url)
#             parse(response2)
#
#     except:
#         print('parse fail')


print(download(url))
